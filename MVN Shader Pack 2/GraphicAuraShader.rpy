init -1500 python:
    from renpy.uguu import GL_MIRRORED_REPEAT, GL_CLAMP_TO_EDGE,GL_REPEAT
    mirror = (GL_CLAMP_TO_EDGE, GL_CLAMP_TO_EDGE)
    GraphicAuraVars ="""
    uniform float u_lod_bias;
    uniform sampler2D tex0;
    uniform sampler2D tex1;
    uniform vec2 res0;
    uniform vec2 res1;
    uniform float u_time;
    varying vec2 v_tex_coord;
    uniform vec4 u_glow_color;     
    uniform vec4 u_end_color;
    uniform float u_glow_intensity; 
    uniform float u_glow_radius;   
    uniform vec2 u_model_size;      
    varying vec2 v_uv;             
    attribute vec2 a_tex_coord;   
    uniform float u_warpIntensity;
    uniform float u_flipIntensity;
    uniform float u_speed;
    uniform float u_scale;
    uniform float u_flipScale;
    uniform float u_flipSpeed;
    uniform float u_fps;
    uniform float u_minSmooth;
    uniform float u_maxSmooth;
    """

    GraphicAuraFragmentShader = """    
    vec4 text_color = texture2D(tex0, v_uv);
    vec4 glow_color = vec4(0.0,0.0,0.0,0.0);
    float frame = floor(u_time * (u_fps));
    vec2 uv = v_uv;
    vec2 distort = Noise2D(uv * u_scale, frame * u_speed);
    distort = distort * 2.0 - 1.0; 
    distort = smoothstep(u_minSmooth, u_maxSmooth, distort);  
    vec2 invertDistort = Noise2D(uv * u_flipScale, frame * u_flipSpeed);
    float frameMod = step(mod(frame, 2), 0.01);
    invertDistort = (invertDistort * (1-frameMod)) + ((1-invertDistort) * frameMod);
    invertDistort = invertDistort * 2.0 - 1.0;  
    vec2 distortedUV = uv + distort * (u_warpIntensity * 0.0001) + invertDistort * (u_flipIntensity * 0.0001);
    vec4 color = texture2D(tex0, distortedUV, u_lod_bias);
    for (float x = -u_glow_radius; x <= u_glow_radius; x += u_glow_radius / 4.0) {
        for (float y = -u_glow_radius; y <= u_glow_radius; y += u_glow_radius / 4.0) {
            vec2 sliding_offset = vec2(x, y) / u_model_size;
            vec2 offset = vec2(x, y+u_time*-0.01*u_model_size) / u_model_size;
            vec4 glow_base = texture2D(tex1, distortedUV+offset);
            float base_luminosity = max(max(glow_base.r,glow_base.g),glow_base.b);
            glow_base = vec4(base_luminosity);
            vec4 aura_map = texture2D(tex1, distortedUV + sliding_offset);
            float luminosity = max(max(aura_map.r,aura_map.g),aura_map.b); 
            aura_map.rgba = vec4(luminosity);
            vec4 treatment = mix(u_glow_color, u_end_color,1.0 - v_uv.y);
            glow_color += (aura_map * treatment);
            // 
        }
    }
    vec4 glow_base = texture2D(tex1, v_uv); 
    glow_color /= (4.0 * u_glow_radius * u_glow_radius);
    // vec4 final = text_color + (glow_color * u_glow_intensity);
    vec4 final = glow_color * u_glow_intensity;
    //final.a = glow_base.a;
    gl_FragColor = ((final) * (1 - text_color.a)) + text_color;  
    
    """

    perlinFunctions = """
     float rand(vec2 c)
    {
        return fract(sin(dot(c.xy, vec2(12.9898, 78.233))) *
                        43758.5453123);
    }

    float Perlin(vec2 x)
    {  
        vec2 index = floor(x);
        vec2 fractal = fract(x);
        
        float a = rand(index);
        float b = rand(index + vec2(1.0, 0.0));
        float c = rand(index + vec2(0.0, 1.0));
        float d = rand(index + vec2(1.0, 1.0));
        
        vec2 blur = fractal * fractal * (3.0 - 2.0 * fractal);
        return mix(a, b, blur.x) +
            (c - a) * blur.y * (1.0 - blur.x) +
            (d - b) * blur.x * blur.y;
    }

    vec2 Noise2D(vec2 uv, float frame)
    {
    
        vec2 q = vec2(0.0);
        q.x = Perlin(uv);
        q.y = Perlin(uv + 1);
        vec2 r = vec2(0.0);
        r.x = Perlin( uv + 1.0*q + vec2(1.7,9.2)+ 0.15 * frame );
        r.y = Perlin( uv + 1.0*q + vec2(8.3,2.8)+ 0.126 * frame);
        return clamp(r, 0.0, 1.0);
    }
    """


    renpy.register_shader("MakeVisualNovels.GraphicAura",
        variables=GraphicAuraVars,
        vertex_functions="",
        fragment_functions=perlinFunctions,   
        vertex_300="""
        v_uv = a_tex_coord;
        """,
        fragment_300=GraphicAuraFragmentShader         
)

    testvars ="""
    uniform float u_lod_bias;
    uniform sampler2D tex0;
    uniform sampler2D tex1;
    uniform float u_time;
    uniform vec2 res0;
    uniform vec2 res1;
    varying vec2 v_uv; 
    attribute vec2 a_tex_coord;
    """

    test2DFragShader = """
    vec2 offset = vec2(0, u_time*0.05);
    vec4 result = texture2D(tex0,  v_uv);
    vec4 normals = texture2D(tex1, v_uv + offset);
    result.rgba *= normals.r;
    gl_FragColor = result;
    """

    renpy.register_shader("MakeVisualNovels.Test2DNormals",
        variables=testvars,
         vertex_300="""
        v_uv = a_tex_coord;
        """,
        fragment_300=test2DFragShader
    )

transform GraphicAura(child):
    Model().shader('MakeVisualNovels.GraphicAura').texture(child, main=True, fit=True).texture('images/tieredaura.png', fit=False)
    gl_texture_wrap_tex1 mirror
    u_minSmooth (0.0)
    u_maxSmooth (1.0)
    u_warpIntensity (1000.0)
    u_speed (0.5)
    u_scale (15.0)
    u_flipIntensity (10.0)
    u_flipSpeed (30.15)
    u_flipScale (10.0)
    u_end_color (0.8,0.8,0.0,0.8)
    u_glow_color (0.8,0.0,0.8,0.8)
    u_glow_intensity (1.5)
    u_glow_radius (4.0)
    u_fps (60.0)
    pause 0
    repeat
    