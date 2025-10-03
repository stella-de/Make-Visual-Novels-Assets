init python:


    from renpy.uguu import GL_MIRRORED_REPEAT, GL_CLAMP_TO_EDGE,GL_REPEAT
    repeat = (GL_REPEAT, GL_REPEAT)
    mirror = (GL_MIRRORED_REPEAT, GL_MIRRORED_REPEAT)



    backgroundCommonVars = """
    varying vec2 v_uv;
    uniform vec2 res0;
    uniform sampler2D tex0;
    uniform float u_time;
    attribute vec2 a_tex_coord;
    varying vec2 v_tex_coord;
    """

    ActionCommonVars ="""
    uniform float u_lod_bias;
    uniform sampler2D tex0;
    uniform sampler2D u_texture;
    uniform float u_time;
    varying vec2 v_tex_coord;
    uniform vec4 u_glow_color;     
    uniform vec4 u_end_color;
    uniform float u_glow_intensity; 
    uniform float u_glow_radius;   
    uniform vec2 u_model_size;      
    varying vec2 v_uv;             
    attribute vec2 a_tex_coord;  
    """

    #Ghost effect too?  Save for Horror pack?

    hsvFunctions = """
    vec3 rgb2hsv(vec3 c) {
    vec4 K = vec4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
    vec4 p = mix(vec4(c.bg, K.wz), vec4(c.gb, K.xy), step(c.b, c.g));
    vec4 q = mix(vec4(p.xyw, c.r), vec4(c.r, p.yzx), step(p.x, c.r));


    float d = q.x - min(q.w, q.y);
    float e = 1.0e-10;
    return vec3(abs(q.z + (q.w - q.y) / (6.0 * d + e)), d / (q.x + e), q.x);
    }


    vec3 hsv2rgb(vec3 c) {
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
    }
    """

    mangaDeluxVars = """
    uniform vec4 u_manga_dark_color;
    uniform vec4 u_manga_light_color;
    uniform float u_manga_intensity;
    uniform float u_state;
        """
    
    mangaDeluxStyleShader="""
        vec4 col = gl_FragColor;
        if (col.a == 0.0) discard;
        vec3 hsv = rgb2hsv(col.rgb);
        if (hsv.z < u_manga_intensity || hsv.y < 0.0025) {  // Adjust the thresholds as needed
        col *= u_manga_dark_color;
        } else {
        col= u_manga_light_color;
        }
        gl_FragColor = mix(gl_FragColor, col, u_state);
    """

    AperlinShaderVars = """
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

    ActionPerlinFragment = """
    vec4 text_color = gl_FragColor; 
    vec4 glow_color = vec4(0.0);
    float frame = floor(u_time * (u_fps));
    vec2 uv = v_uv;
    vec2 distort = Noise2D(uv * u_scale, frame * u_speed);
    distort = distort * 2.0 - 1.0; 
    distort = smoothstep(u_minSmooth, u_maxSmooth, distort);  
    vec2 invertDistort = Noise2D(uv * u_flipScale, frame * u_flipSpeed);
    float frameMod = step(mod(frame, 2.0), 0.01);
    invertDistort = (invertDistort * (1.0-frameMod)) + ((1.0-invertDistort) * frameMod);
    invertDistort = invertDistort * 2.0 - 1.0;  
    vec2 distortedUV = uv + distort * (u_warpIntensity * 0.0001) + invertDistort * (u_flipIntensity * 0.0001);
    vec4 color = texture2D(tex0, distortedUV, u_lod_bias);
    const float MAX_LOOPS = 100.0;
    for (float x = 0.0; x <= MAX_LOOPS; x++) {
        if((u_glow_radius * 2.0) - (x*u_glow_radius*0.25) <= 0.0) break;
        for (float y = 0.0; y <= MAX_LOOPS; y++) {
            if((u_glow_radius * 2.0) - (y*u_glow_radius*0.25) <= 0.0) break;
            float offx = u_glow_radius - distance((u_glow_radius * 2.0), x*u_glow_radius*0.25);
            float offy = u_glow_radius - distance((u_glow_radius * 2.0), y*u_glow_radius*0.25);
            vec2 offset = vec2(offx, offy) / u_model_size;
            glow_color += texture2D(tex0, distortedUV + offset).a * mix(u_glow_color, u_end_color,1.0 - v_uv.y);
        }
    }
    //Rimlight Calcs

    vec4 origin_color = texture2D(tex0, uv, u_lod_bias);
    float a0 = origin_color.a;
    float a1 = texture2D(tex0, uv + vec2(0.008, 0.0)).a;
    float a2 = texture2D(tex0, uv - vec2(0.008, 0.0)).a;
    float a3 = texture2D(tex0, uv + vec2(0.0, 0.008)).a;
    float a4 = texture2D(tex0, uv - vec2(0.0, 0.008)).a;
    float alpha_gradient = max(
        abs(a0 - a1),
        max(abs(a0 - a2),
        max(abs(a0 - a3),
            abs(a0 - a4)))
    );
    float glow_width = 1.0; //Knob, maybe?
    float edge_glow = smoothstep(0.0, glow_width, alpha_gradient);
    float dist_to_rim = distance(uv, vec2(0.5,0.5));
    float rim_falloff = smoothstep(0.5 * 0.7, 0.5, dist_to_rim);
    float feather = smoothstep(0.0, 3.0, edge_glow);
    float falloff = pow(feather * (1.0 - rim_falloff), 0.5); // This and feathering need knobs.
    vec4 rim_light = mix(u_glow_color, u_end_color, falloff) * falloff * 2.0; 
    vec4 rim_color = (origin_color + rim_light);

    glow_color /= (4.0 * u_glow_radius * u_glow_radius);
    vec4 final = mix(rim_color, (glow_color * u_glow_intensity), 1.0 - text_color.a);
    gl_FragColor = final+rim_light;  
    """
    
    
    """
    vec2 uv = v_tex_coord;
    vec4 origin_color = texture2D(tex0, uv, u_lod_bias);
    float a0 = origin_color.a;
    float a1 = texture2D(tex0, uv + vec2(0.008, 0.0)).a;
    float a2 = texture2D(tex0, uv - vec2(0.008, 0.0)).a;
    float a3 = texture2D(tex0, uv + vec2(0.0, 0.008)).a;
    float a4 = texture2D(tex0, uv - vec2(0.0, 0.008)).a;
    float alpha_gradient = max(
        abs(a0 - a1),
        max(abs(a0 - a2),
        max(abs(a0 - a3),
            abs(a0 - a4)))
    );
    float glow_width = 1.0; //Knob, maybe?
    float edge_glow = smoothstep(0.0, glow_width, alpha_gradient);
    float dist_to_rim = distance(uv, vec2(0.5,0.5));
    float rim_falloff = smoothstep(0.5 * 0.7, 0.5, dist_to_rim);
    float feather = smoothstep(0.0, 3.0, edge_glow);
    float falloff = pow(feather * (1.0 - rim_falloff), 0.5); // This and feathering need knobs.
    vec3 rim_light = glow_color * falloff * u_glow_intensity; 
    vec3 rim_color = (origin_color.rgb + rim_light)
    
    """

    AperlinFunctions = """
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
        q.y = Perlin(uv + 1.0);
        vec2 r = vec2(0.0);
        r.x = Perlin( uv + 1.0*q + vec2(1.7,9.2)+ 0.15 * frame );
        r.y = Perlin( uv + 1.0*q + vec2(8.3,2.8)+ 0.126 * frame);
        return clamp(r, 0.0, 1.0);
    }
    """

    hsvRGB ="""
    vec3 hsv_to_rgb(float h) {
        float r = abs(h * 6.0 - 3.0) - 1.0;
        float g = 2.0 - abs(h * 6.0 - 2.0);
        float b = 2.0 - abs(h * 6.0 - 4.0);
    return clamp(vec3(r, g, b), 0.0, 1.0);
    }
"""
    radialEffectVars = """
    uniform float u_speed;
    """

    radialEffect = """
    // Convert texcoords from 0-1 range to -1 to +1 range
    vec2 p = -1.0 + 2.0 * v_tex_coord;

    vec3 color = vec3(0.0);
    vec2 d = (vec2(0.0, 0.0) - p) / 32.0;
    float w = 2.0;
    vec2 s = p;

    for (int i = 0; i < 32; i++)
    {
        //0.1 here is the speed.  For WHATEVER reason, I cannot get Model() to 
        //take a variable when I need to set the property of the texture to wrap.
        float time = 0.1 * u_time;
        vec2 q = sin(vec2(1.1, 1.2) * time + s);
        float a = atan(q.y, q.x);
        float r = sqrt(dot(q, q));
        vec2 uv = s * sqrt(1.0 + r*r);
        //uv += sin(vec2(0.0, 0.6) + vec2(1.0, 1.2) * time);

        vec3 res = texture2D(tex0, uv * 0.7).xyz;
        color += w * smoothstep(0.0, 1.0, res);
        w *= 0.85;
        s += d;
    }
    

    color = color * 3.5 / 32.0;

    gl_FragColor = vec4(color, 1.0);
    """
    eMistEffect= """
    vec2 p = -1.0 + 2.0 * v_tex_coord; // screen space from -1 to +1
    vec3 color = vec3(0.0);  
          

    vec2 d = normalize(vec2(0.0, 0.0) - p) * 0.02; // direction toward center, small step size
    float total = 0.0; // total brightness
    vec2 pos = p;      // current marching position

    for (int i = 0; i < 128; i++) {
        float density = sin(5.0*pos.x + u_time*0.2) * sin(5.0*pos.y + u_time*0.2);
        total += smoothstep(0.0, 1.0, density);
        pos += d;
    }

    total /= 128.0; // normalize total brightness

    color += vec3(total) * 1.5; // boost brightness

    gl_FragColor = vec4(color, 1.0);
    """

    flowVars ="""
    uniform float u_waves;
    uniform float u_complexity;
    uniform float u_blend;
    uniform float u_speed;
    uniform float u_yFreq;
    uniform float u_xFreq;
    uniform vec4 u_flowColor;
    """
    flowFragmentShader = """
    vec2 uv =  (u_complexity * v_uv - res0.xy) / min(res0.x, res0.y);
    for(float i = 1.0; i < u_waves; i++){
        uv.x += 0.6 / i * cos(i * u_yFreq * uv.y + u_time);
        uv.y += 0.6 / i * cos(i * u_xFreq * uv.x + u_time);
    }
    
    vec4 flow = vec4(vec3(u_flowColor.rgb)/abs(sin(u_time-uv.y-uv.x)),u_flowColor.a);
    vec4 color = texture2D(tex0, v_tex_coord);
    gl_FragColor = (u_blend * color) + flow;
    """

    overlayFlowFragmentShader = """
    vec2 uv =  (u_complexity * v_uv - res0.xy) / min(res0.x, res0.y);
    for(float i = 1.0; i < u_waves; i++){
        uv.x += 0.6 / i * cos(i * u_yFreq * uv.y + u_time);
        uv.y += 0.6 / i * cos(i * u_xFreq * uv.x + u_time);
    }
    
    vec4 flow = vec4(vec3(u_flowColor.rgb)/abs(sin(u_time-uv.y-uv.x)),u_flowColor.a);
    vec4 color = texture2D(tex0, v_tex_coord);
    gl_FragColor = color + (flow * color.a);
    """

    mappedflowVars ="""
    uniform sampler2D tex0;
    uniform sampler2D tex1;
    uniform float u_waves;
    uniform float u_complexity;
    uniform float u_blend;
    uniform float u_speed;
    uniform float u_yFreq;
    uniform float u_xFreq;
    uniform vec4 u_flowColor;
    varying vec2 v_tex_coord;
    attribute vec2 a_tex_coord;
    """

    mappedoverlayFlowFragmentShader = """   
    vec4 map = texture2D(tex1, v_tex_coord);
    vec2 uv =  (u_complexity * v_uv - res0.xy) / min(res0.x, res0.y);
    for(float i = 1.0; i < u_waves; i++){
        uv.x += 0.6 / i * cos(i * u_yFreq * uv.y + u_time);
        uv.y += 0.6 / i * cos(i * u_xFreq * uv.x + u_time);
    }
    
    vec4 flow = vec4(vec3(u_flowColor.rgb)/abs(sin(u_time-uv.y-uv.x)),u_flowColor.a);
    vec4 color = texture2D(tex0, v_tex_coord);
    gl_FragColor = color + (flow * map.a);
    """

    mappedShimmerVars ="""
    uniform sampler2D tex0;
    uniform sampler2D tex1;
    uniform vec2 u_model_size;
    uniform vec4 u_glow_color;
    uniform vec4 u_end_color;
    uniform float u_glow_radius;
    uniform float u_glow_intensity;
    varying vec2 v_tex_coord;
    attribute vec2 a_tex_coord;
    """

    mappedShimmer = """
    vec4 color = texture2D(tex0, v_tex_coord);
    vec4 glow_color = vec4(0.0);
    vec4 map = texture2D(tex1, v_tex_coord);
    for (float x = -u_glow_radius; x <= u_glow_radius; x += u_glow_radius / 4.0) {
        for (float y = -u_glow_radius; y <= u_glow_radius; y += u_glow_radius / 4.0) {
            vec2 offset = vec2(x, y) / u_model_size;
            glow_color += texture2D(tex0, v_tex_coord + offset) * mix(u_glow_color, u_end_color,max(1.0 - v_tex_coord.x,1.0 - v_tex_coord.y));
        }
    }
    glow_color /= (4.0 * u_glow_radius * u_glow_radius);
    vec4 final = color + (glow_color * u_glow_intensity);
    
    gl_FragColor = (color * (1.0 - map.a)) + ((final * map.a));

    """

    backgroundShaderCommonVars = """
    varying vec2 v_uv;
    uniform vec2 res0;
    uniform sampler2D tex0;
    uniform float u_time;
    attribute vec2 a_tex_coord;
    varying vec2 v_tex_coord;
    """

    procSmokeVars = """
    uniform float u_time;
    uniform vec4 u_smoke_color;
    uniform float u_scroll_speed;
    uniform float u_noise_scale;
    """

    procSmokeFunctions = """
mat2 rot(float a) {
    float s = sin(a), c = cos(a);
    return mat2(c, -s, s, c);
}

float hash(vec2 p) {
    return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453);
}

float noise(vec2 p) {
    vec2 i = floor(p);
    vec2 f = fract(p);
    float a = hash(i);
    float b = hash(i + vec2(1.0, 0.0));
    float c = hash(i + vec2(0.0, 1.0));
    float d = hash(i + vec2(1.0, 1.0));
    vec2 u = f * f * (3.0 - 2.0 * f);
    return mix(a, b, u.x) +
           (c - a) * u.y * (1.0 - u.x) +
           (d - b) * u.x * u.y;
}

float fbm(vec2 p) {
    float total = 0.0;
    float amp = 0.5;
    mat2 r = rot(0.5);
    for (int i = 0; i < 5; ++i) {
        total += amp * noise(p);
        p = r * p * 2.0;
        amp *= 0.5;
    }
    return total;
}
"""
    procSmokeFragment = """
vec2 uv = v_tex_coord;
uv.y += u_time * u_scroll_speed;
vec2 p = uv * u_noise_scale;
float smoke = fbm(p);
float fade = smoothstep(1.0,0.2, v_tex_coord.y);
float alpha = smoke * fade * u_smoke_color.a;
vec3 color = u_smoke_color.rgb * smoke;
gl_FragColor = vec4(color, alpha);
"""


    radialLinesVars = """
uniform float u_time;
uniform vec4 u_line_color;
uniform vec4 u_alt_color;
uniform float u_density;
uniform float u_thickness;
uniform float u_center_fade;
uniform float u_flicker_rate;
uniform vec2 u_model_size;
"""


    radialLinesFunctions = """
float rand(float x) {
    return fract(sin(x * 91.3458) * 47453.5453);
}
"""

    radialLinesFragment = """
        vec2 uv = v_tex_coord - 0.5;
float angle = atan(uv.y, uv.x);        
vec2 aspect_corrected_uv = uv;
aspect_corrected_uv.x *= u_model_size.x / u_model_size.y;
float radius = length(aspect_corrected_uv);

// Normalize angle to 0–2PI
float norm_angle = mod(angle + 3.14159, 6.28318);

// Line index
float line_index = floor(norm_angle * u_density);

// Random offset and width per line
float flicker_time = floor(u_time * u_flicker_rate);
float angle_seed = line_index + flicker_time;

float angle_offset = rand(angle_seed * 7.13) * (1.0 / u_density);
float angle_width  = mix(0.005, u_thickness, rand(angle_seed * 2.77));

// Recalculate band position with offset
float band_pos = fract(norm_angle * u_density - angle_offset);

// Inside angular region?
float in_band = step(1.0 - angle_width, band_pos);

// Enforce inner radius (shortened lines)
float radius_mask = step(u_center_fade, radius);

// Final shape mask
float shape = in_band * radius_mask;

// Alternate color between two
vec3 color_a = u_line_color.rgb;
vec3 color_b = u_alt_color.rgb;
vec3 stripe_color = mix(color_a, color_b, mod(line_index, 2.0));

// Flicker placeholder (not doing anything meaningful yet)
float flicker_phase = rand(line_index * 13.37);
float flicker = 0.8 + 0.2 * sin(u_time * 10.0 + flicker_phase * 6.28);

float alpha = shape * flicker * u_line_color.a;

gl_FragColor = vec4(stripe_color * alpha, alpha);



"""



    renpy.register_shader("MakeVisualNovels.ProcSmoke", variables=procSmokeVars+ActionCommonVars, fragment_300=procSmokeFragment, fragment_functions=procSmokeFunctions)
    renpy.register_shader("MakeVisualNovels.RadialSpeedLines", variables=radialLinesVars, fragment_300=radialLinesFragment, fragment_functions=radialLinesFunctions)
    renpy.register_shader("MakeVisualNovels.MangaDeluxe",
        variables=ActionCommonVars+mangaDeluxVars,   
        vertex_300="""
        v_uv = a_tex_coord;
        v_tex_coord = a_tex_coord;
        """,
        fragment_functions=hsvFunctions,
        fragment_300=mangaDeluxStyleShader         
)

    renpy.register_shader("MakeVisualNovels.Blazing",
        variables=ActionCommonVars+AperlinShaderVars,   
        vertex_300="""
        v_uv = a_tex_coord;
        v_tex_coord = a_tex_coord;
        """,
        fragment_functions=AperlinFunctions,
        fragment_300=ActionPerlinFragment         
)
    renpy.register_shader("MakeVisualNovels.EMist",
        variables=backgroundShaderCommonVars+radialEffectVars,   
        vertex_300="""
        v_tex_coord = a_tex_coord;
        """,
        fragment_300=eMistEffect         
)

    renpy.register_shader("MakeVisualNovels.Radial",
        variables=backgroundShaderCommonVars+radialEffectVars,   
        vertex_300="""
        v_tex_coord = a_tex_coord;
        """,
        fragment_300=radialEffect         
)

    renpy.register_shader("MakeVisualNovels.Flow",
        variables=backgroundShaderCommonVars+flowVars,   
        vertex_300="""
        v_uv = a_position.xy;
        """,
        fragment_300=flowFragmentShader         
)

    renpy.register_shader("MakeVisualNovels.OverlayFlow",
        variables=backgroundShaderCommonVars+flowVars,   
        vertex_300="""
        v_uv = a_position.xy;
        """,
        fragment_300=overlayFlowFragmentShader         
)

    renpy.register_shader("MakeVisualNovels.MappedFlow",
        variables=backgroundShaderCommonVars+mappedflowVars,   
        vertex_300="""
        v_uv = a_position.xy;
        v_tex_coord = a_tex_coord;
        """,
        fragment_300=mappedoverlayFlowFragmentShader         
)

    renpy.register_shader("MakeVisualNovels.MappedShimmer",
        variables=backgroundShaderCommonVars+mappedShimmerVars,   
        vertex_300="""
        v_uv = a_position.xy;
        v_tex_coord = a_tex_coord;
        """,
        fragment_300=mappedShimmer         
)