init -1500 python:

    TcommonVars ="""
    uniform float u_lod_bias;
    
    uniform sampler2D tex0;
    uniform sampler2D u_texture;
    uniform float u_time;
    varying vec2 v_tex_coord;
    """

    TwarpFragmentShader = """
    vec4 text_color = texture2D(tex0, v__uv);
    vec4 glow_color = vec4(0.0);
    float frame = floor(u_time * (u__fps));
    vec2 uv = v__uv;
    vec2 distort = Noise2D(uv * u__scale, frame * u__speed);
    distort = distort * 2.0 - 1.0; 
    distort = smoothstep(u__minSmooth, u__maxSmooth, distort);  
    vec2 invertDistort = Noise2D(uv * u__flipScale, frame * u__flipSpeed);
    float frameMod = step(mod(frame, 2), 0.01);
    invertDistort = (invertDistort * (1-frameMod)) + ((1-invertDistort) * frameMod);
    invertDistort = invertDistort * 2.0 - 1.0;  
    vec2 distortedUV = uv + distort * (u__warpIntensity * 0.0001) + invertDistort * (u__flipIntensity * 0.0001);
    vec4 color = texture2D(tex0, distortedUV, u_lod_bias);
    const float MAX_LOOPS = 100.0;
    for (float x = 0.0; x <= MAX_LOOPS; x++) {
        if((u__glow_radius * 2.0) - (x*u__glow_radius*0.25) <= 0.0) break;
        for (float y = 0.0; y <= MAX_LOOPS; y++) {
            if((u__glow_radius * 2.0) - (y*u__glow_radius*0.25) <= 0.0) break;
            float offx = u__glow_radius - distance((u__glow_radius * 2.0), x*u__glow_radius*0.25);
            float offy = u__glow_radius - distance((u__glow_radius * 2.0), y*u__glow_radius*0.25);
            vec2 offset = vec2(offx, offy) / u_model_size;
            glow_color += texture2D(tex0, distortedUV + offset).a * mix(u__glow_color, u__end_color,1.0 - v__uv.y);
        }
    }

    glow_color /= (4.0 * u__glow_radius * u__glow_radius);
    vec4 final = text_color + (glow_color * u__glow_intensity);
    gl_FragColor = final;  
    """

    hsvRGB ="""
    vec3 hsv_to_rgb(float h) {
        float r = abs(h * 6.0 - 3.0) - 1.0;
        float g = 2.0 - abs(h * 6.0 - 2.0);
        float b = 2.0 - abs(h * 6.0 - 4.0);
    return clamp(vec3(r, g, b), 0.0, 1.0);
    }
"""

    TwarpFragmentAdjustableDemo= """
    vec4 text_color = texture2D(tex0, v__uv);
    vec4 glow_color = vec4(0.0);
    float frame = floor(u_time * (u__fps));
    vec2 uv = v__uv;
    vec2 distort = Noise2D(uv * u__scale, frame * u__speed);
    distort = distort * 2.0 - 1.0; 
    distort = smoothstep(u__minSmooth, u__maxSmooth, distort);  
    vec2 invertDistort = Noise2D(uv * u__flipScale, frame * u__flipSpeed);
    float frameMod = step(mod(frame, 2.0), 0.01);
    invertDistort = (invertDistort * (1-frameMod)) + ((1-invertDistort) * frameMod);
    invertDistort = invertDistort * 2.0 - 1.0;  
    vec2 distortedUV = uv + distort * (u__warpIntensity * 0.0001) + invertDistort * (u__flipIntensity * 0.0001);
    vec4 color = texture2D(tex0, distortedUV, u_lod_bias);
    
    
    vec4 rainbowColorA = vec4(hsv_to_rgb(mod(u_time * 0.1, 1.0)),0.7);  
    vec4 rainbowColorB = vec4(hsv_to_rgb(mod(u_time * 0.1 + 0.33, 1.0)), 0.8);  
    float mix_factor = mod(v__uv.y * 0.02 + v__uv.y * 0.02, 1.0);
   
   
   const float MAX_LOOPS = 100.0;
    for (float x = 0.0; x <= MAX_LOOPS; x++) {
        if((u__glow_radius * 2.0) - (x*u__glow_radius*0.25) <= 0.0) break;
        for (float y = 0.0; y <= MAX_LOOPS; y++) {
            if((u__glow_radius * 2.0) - (y*u__glow_radius*0.25) <= 0.0) break;
            float offx = u__glow_radius - distance((u__glow_radius * 2.0), x*u__glow_radius*0.25);
            float offy = u__glow_radius - distance((u__glow_radius * 2.0), y*u__glow_radius*0.25);
            vec2 offset = vec2(offx, offy) / u_model_size;
        
       
        float mix_factor = mod(v__uv.y + x*u__glow_radius*0.25 * 0.02 + y*u__glow_radius*0.25 * 0.02, 1.0);
        vec4 final_glow_color = mix(rainbowColorA, rainbowColorB, mix_factor * (sin(u_time * 0.5) * 0.5 + 0.5)); 

        // Apply to glow
        glow_color += texture2D(tex0, distortedUV + offset).a * final_glow_color;
    }
}
    
    glow_color /= (4.0 * u__glow_radius * u__glow_radius);
    vec4 final = text_color + (glow_color * u__glow_intensity);
    gl_FragColor = final;  
    """
    

    TperlinShaderVars = """
    uniform float u__warpIntensity;
    uniform float u__flipIntensity;
    uniform float u__speed;
    uniform float u__scale;
    uniform float u__flipScale;
    uniform float u__flipSpeed;
    uniform float u__fps;
    uniform float u__minSmooth;
    uniform float u__maxSmooth;
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
        q.y = Perlin(uv + 1.0);
        vec2 r = vec2(0.0);
        r.x = Perlin( uv + 1.0*q + vec2(1.7,9.2)+ 0.15 * frame );
        r.y = Perlin( uv + 1.0*q + vec2(8.3,2.8)+ 0.126 * frame);
        return clamp(r, 0.0, 1.0);
    }
    """

    TperlinGlowVars = """
    uniform vec4 u__glow_color;     
    uniform vec4 u__end_color;
    uniform float u__glow_intensity; 
    uniform float u__glow_radius;   
    uniform vec2 u_model_size;      
    varying vec2 v__uv;             
    attribute vec2 a_tex_coord;     
    """

    

    renpy.register_textshader("GhostWrite",
        variables=TcommonVars+TperlinShaderVars+TperlinGlowVars,
        vertex_functions="",
        fragment_functions=perlinFunctions,
        vertex_300="""
        v__uv = a_tex_coord;
        """,
        redraw=0.0, #This is important
        fragment_300=TwarpFragmentShader,
        u__fps= 15.0,
        u__minSmooth= 0.0, 
        u__maxSmooth= 0.5, 
        u__warpIntensity= 300.0,
        u__speed= -1.55,
        u__scale= 1.55,
        u__flipIntensity= 1.0,
        u__flipSpeed= 1.0,
        u__flipScale= 1.0,
        u__end_color="#00880066",
        u__glow_color="#00000000",    
        u__glow_intensity=5.0,      
        u__glow_radius=4.0         
)

    renpy.register_textshader("BurningForBigText",
        variables=TcommonVars+TperlinShaderVars+TperlinGlowVars,
        vertex_functions="",
        fragment_functions=perlinFunctions,
       
        vertex_300="""
        v__uv = a_tex_coord;
        """,
        redraw=0.0,
        fragment_300=TwarpFragmentShader,
        u__fps= 60.0,
        u__minSmooth= 0.0, 
        u__maxSmooth= 0.5, 
        u__warpIntensity= 50.0,
        u__speed= 0.15,
        u__scale= 25.0,
        u__flipIntensity= 0.0,
        u__flipSpeed= 1.0,
        u__flipScale= 1.0,
        u__end_color="#BBBB0066",
        u__glow_color="#BB0000FF",    
        u__glow_intensity=5.0,      
        u__glow_radius=4.0         
)

    renpy.register_textshader("BurningForSmallText",
        variables=TcommonVars+TperlinShaderVars+TperlinGlowVars,
        vertex_functions="",
        fragment_functions=perlinFunctions,  
        vertex_300="""
        v__uv = a_tex_coord;
        """,
        redraw=0.0,
        fragment_300=TwarpFragmentShader,
        u__fps= 60.0,
        u__minSmooth= 0.0, 
        u__maxSmooth= 0.0, 
        u__warpIntensity= 50.0,
        u__speed= 0.15,
        u__scale= 5.0,
        u__flipIntensity= 0.0,
        u__flipSpeed= 1.0,
        u__flipScale= 1.0,
        u__end_color="#BBBB0066",
        u__glow_color="#BB0000FF",    
        u__glow_intensity=5.0,      
        u__glow_radius=4.0         
)

    renpy.register_textshader("BlueBurnBig",
        variables=TcommonVars+TperlinShaderVars+TperlinGlowVars,
        vertex_functions="",
        fragment_functions=perlinFunctions,
       
        vertex_300="""
        v__uv = a_tex_coord;
        """,
        redraw=0.0,
        fragment_300=TwarpFragmentShader,
        u__fps= 60.0,
        u__minSmooth= 0.0, 
        u__maxSmooth= 0.5, 
        u__warpIntensity= 50.0,
        u__speed= 0.15,
        u__scale= 25.0,
        u__flipIntensity= 0.0,
        u__flipSpeed= 1.0,
        u__flipScale= 1.0,
        u__end_color="#00BBBB66",
        u__glow_color="#0000BBFF",    
        u__glow_intensity=5.0,      
        u__glow_radius=4.0         
)

    renpy.register_textshader("BlueBurnSmall",
        variables=TcommonVars+TperlinShaderVars+TperlinGlowVars,
        vertex_functions="",
        fragment_functions=perlinFunctions,  
        vertex_300="""
        v__uv = a_tex_coord;
        """,
        redraw=0.0,
        fragment_300=TwarpFragmentShader,
        u__fps= 60.0,
        u__minSmooth= 0.0, 
        u__maxSmooth= 0.0, 
        u__warpIntensity= 50.0,
        u__speed= 0.15,
        u__scale= 5.0,
        u__flipIntensity= 0.0,
        u__flipSpeed= 1.0,
        u__flipScale= 1.0,
        u__end_color="#00BBBB66",
        u__glow_color="#0000BBFF",    
        u__glow_intensity=5.0,      
        u__glow_radius=4.0         
)


    renpy.register_textshader("AdjustableBurnDemo",
        variables=TcommonVars+TperlinShaderVars+TperlinGlowVars,
        vertex_functions="",
        fragment_functions=perlinFunctions+hsvRGB,  
        vertex_300="""
        v__uv = a_tex_coord;
        """,
        redraw=0.0,
        fragment_300=TwarpFragmentAdjustableDemo,
        u__fps= 60.0,
        u__minSmooth= 0.0, 
        u__maxSmooth= 0.5, 
        u__warpIntensity= 50.0,
        u__speed= 0.55,
        u__scale= 25.0,
        u__flipIntensity= 0.0,
        u__flipSpeed= 1.0,
        u__flipScale= 1.0,
        u__end_color="#BBBB0066", #lmao I'm lazy
        u__glow_color="#BB0000FF",    
        u__glow_intensity=4.0,      
        u__glow_radius=7.0         
)


    
    #Good, Low radius + Higher intensity for a sharper negative space text.
    #Could use directional settings.
    #Animation could be really cool.
    renpy.register_textshader(
    "HollowGlow",

    variables="""
    uniform vec4 u__glow_color;     
    uniform vec4 u__end_color;
    uniform float u__glow_intensity;
    uniform float u__glow_radius;
    uniform vec2 u_model_size; 
    varying vec2 v__uv;        
    attribute vec2 a_tex_coord;
    """,

    vertex_300="""
    v__uv = a_tex_coord;
    """,

    fragment_300="""
    vec4 text_color = texture2D(tex0, v__uv);
    vec4 glow_color = vec4(0.0);
    const float MAX_LOOPS = 100.0;
    for (float x = 0.0; x <= MAX_LOOPS; x++) {
        if((u__glow_radius * 2.0) - (x*u__glow_radius*0.25) <= 0.0) break;
        for (float y = 0.0; y <= MAX_LOOPS; y++) {
            if((u__glow_radius * 2.0) - (y*u__glow_radius*0.25) <= 0.0) break;
            float offx = u__glow_radius - distance((u__glow_radius * 2.0), x*u__glow_radius*0.25);
            float offy = u__glow_radius - distance((u__glow_radius * 2.0), y*u__glow_radius*0.25);
            vec2 offset = vec2(offx, offy) / u_model_size;
            glow_color += texture2D(tex0, v__uv + offset) * mix(u__glow_color, u__end_color,max(1.0 - v__uv.x,1.0 - v__uv.y));
        }
    }
    glow_color /= (4.0 * u__glow_radius * u__glow_radius);    
    vec4 final = text_color + (glow_color * u__glow_intensity);
    vec4 hollowfinal=  (text_color + glow_color * u__glow_intensity) * (1.0- text_color.a);
    gl_FragColor = hollowfinal;
    """,
    u__end_color="#FF00FF",
    u__glow_color="#FFFF00",    
    u__glow_intensity=5.0,      
    u__glow_radius=3.0,         
)
    #Could use directional settings.
    renpy.register_textshader(
    "gradientglow",
    variables="""
    uniform vec4 u__glow_color;     
    uniform vec4 u__end_color;
    uniform float u__glow_intensity;
    uniform float u__glow_radius;   
    uniform vec2 u_model_size;      
    varying vec2 v__uv;             
    attribute vec2 a_tex_coord;     
    """,
    vertex_300="""
    v__uv = a_tex_coord;
    """,
    fragment_300="""
   
    vec4 text_color = texture2D(tex0, v__uv);
    vec4 glow_color = vec4(0.0);
    const float MAX_LOOPS = 100.0;
    for (float x = 0.0; x <= MAX_LOOPS; x++) {
        if((u__glow_radius * 2.0) - (x*u__glow_radius*0.25) <= 0.0) break;
        for (float y = 0.0; y <= MAX_LOOPS; y++) {
            if((u__glow_radius * 2.0) - (y*u__glow_radius*0.25) <= 0.0) break;
            float offx = u__glow_radius - distance((u__glow_radius * 2.0), x*u__glow_radius*0.25);
            float offy = u__glow_radius - distance((u__glow_radius * 2.0), y*u__glow_radius*0.25);
            vec2 offset = vec2(offx, offy) / u_model_size;
            glow_color += texture2D(tex0, v__uv + offset) * mix(u__glow_color, u__end_color,max(1.0 - v__uv.x,1.0 - v__uv.y));
        }
    }
    glow_color /= (4.0 * u__glow_radius * u__glow_radius);
    vec4 final = text_color + (glow_color * u__glow_intensity) ;
    gl_FragColor = final;
    """,
    u__end_color="#FF00FF",
    u__glow_color="#FFFF00",    # Default glow color (White)
    u__glow_intensity=3.0,      # Default glow intensity
    u__glow_radius=6.0,         # Default glow radius
)



    renpy.register_textshader(
    "Glow",
    variables="""
    uniform vec4 u__glow_color;    
    uniform float u__glow_intensity;
    uniform float u__glow_radius;  
    uniform vec2 u_model_size;      
    varying vec2 v__uv;             
    attribute vec2 a_tex_coord;     
    """,

    vertex_300="""
    
    v__uv = a_tex_coord;
    """,

    fragment_300="""
    
    vec4 text_color = texture2D(tex0, v__uv);
    vec4 glow_color = vec4(0.0);
    const float MAX_LOOPS = 100.0;
    for (float x = 0.0; x <= MAX_LOOPS; x++) {
        if((u__glow_radius * 2.0) - (x*u__glow_radius*0.25) <= 0.0) break;
        for (float y = 0.0; y <= MAX_LOOPS; y++) {
            if((u__glow_radius * 2.0) - (y*u__glow_radius*0.25) <= 0.0) break;
            float offx = u__glow_radius - distance((u__glow_radius * 2.0), x*u__glow_radius*0.25);
            float offy = u__glow_radius - distance((u__glow_radius * 2.0), y*u__glow_radius*0.25);
            vec2 offset = vec2(offx, offy) / u_model_size;
            glow_color += texture2D(tex0, v__uv + offset) * u__glow_color;
        }
    }

    glow_color /= (4.0 * u__glow_radius * u__glow_radius);
    gl_FragColor = text_color + glow_color * u__glow_intensity;
    """,

    u__glow_color="#FFFFFF",    # Default glow color (White)
    u__glow_intensity=2.0,      # Default glow intensity
    u__glow_radius=5.0,         # Default glow radius
)


    """
    

    for (float x = -u__glow_radius; x <= MAX_LOOPS; x += u__glow_radius / 4.0) {
        if(u__glow_radius - x <= 0.0) break;
        for (float y = -u__glow_radius; y <= MAX_LOOPS; y += u__glow_radius / 4.0) {
            if(u__glow_radius - y <= 0.0) break;
            vec2 offset = vec2(x, y) / u_model_size;
            glow_color += texture2D(tex0, v__uv + offset) * u__glow_color;
        }
    }
    """


    renpy.register_textshader(
        "RedAlert",
        variables="""
        uniform vec4 u__color;         
        uniform float u__softness;     
        uniform float u__width;        
        uniform float u__angle;        
        uniform float u__intensity;    
        uniform float u__duration;     
        uniform float u__delay;        
        uniform float u_time;          
        varying vec2 v__uv;            
        attribute vec2 a_tex_coord;    
        """,
        vertex_300="""
        v__uv = a_tex_coord;
        """,
        fragment_300="""
        vec4 text_color = texture2D(tex0, v__uv);
        float progress = mod(max(0.0, u_time - u__delay), u__duration) / u__duration;
        float sweep = progress - 0.5;
        
        float distance = abs((v__uv.x-sweep)-(v__uv.y+sweep));
        float intensity = u__intensity * distance;
        vec4 newcolor = ((intensity * u__color) * text_color.a);
        text_color = mix(text_color,newcolor, progress);
        gl_FragColor = text_color;
        """,
        u__color="#FF0000",      
        u__intensity=1.0,        
        u__duration=1.0,         
        u__delay=1.0,            
        redraw = 0.0
    )

    renpy.register_textshader(
        "Prey",
        variables="""
        uniform vec4 u__color;           
        uniform float u__softness;       
        uniform float u__width;          
        uniform vec2 u__start_pos;       
        uniform vec2 u__end_pos;         
        uniform float u__intensity;      
        uniform float u__duration;       
        uniform float u__delay;          
        uniform float u_time;            
        varying vec2 v__uv;              
        attribute vec2 a_tex_coord;      
        """,

        vertex_300="""
        v__uv = a_tex_coord;
        """,

        fragment_300="""
        float total_loop_time = u__duration + u__delay;
        float loop_time = mod(u_time, total_loop_time);
        float active_time = clamp(loop_time / u__duration, 0.0, 1.0);
        vec2 sweep_center = mix(u__start_pos, u__end_pos, active_time);
        float distance = length(v__uv - sweep_center);
        float sweep_effect = smoothstep(
            -u__width - u__softness,
            -u__width,
            distance
        ) - smoothstep(
            u__width,
            u__width + u__softness,
            distance
        );
        vec4 text_color = texture2D(tex0, v__uv);
        vec4 sweep_color = vec4(u__color.rgb * u__intensity, u__color.a * sweep_effect);
        gl_FragColor = mix(text_color, sweep_color, sweep_effect) * text_color.a;
        """,
        u__color="#770000",      # Default sweep color (Red)
        u__softness=0.1,        # Default softness
        u__width=0.50,            # Default width
        u__start_pos=(-1.0, 0.5), # Default starting position (bottom-left)
        u__end_pos=(2.0, 0.5),   # Default ending position (top-right)
        u__intensity=1.0,        # Default intensity
        u__duration=2.0,         # Duration of the sweep effect
        u__delay=1.0,            # Default delay between loops
        redraw= 0.0
    )

    renpy.register_textshader(
        "GoldSweep",
        variables="""
        uniform vec4 u__base_color;      
        uniform vec4 u__color;           
        uniform float u__softness;       
        uniform float u__width;          
        uniform vec2 u__start_pos;       
        uniform vec2 u__end_pos;         
        uniform float u__intensity;      
        uniform float u__duration;       
        uniform float u__delay;          
        uniform float u_time;            
        varying vec2 v__uv;              
        attribute vec2 a_tex_coord;      
        """,
        vertex_300="""
        
        v__uv = a_tex_coord;
        """,
        fragment_300="""
        float total_loop_time = u__duration + u__delay;
        float loop_time = mod(u_time, total_loop_time);
        float active_time = clamp(loop_time / u__duration, 0.0, 1.0);
        vec2 sweep_center = mix(u__start_pos, u__end_pos, active_time);
        float distance = length(v__uv - sweep_center);
        float sweep_effect = smoothstep(
            -u__width - u__softness,
            -u__width,
            distance
        ) - smoothstep(
            u__width,
            u__width + u__softness,
            distance
        );
        vec4 text_color = u__base_color * texture2D(tex0, v__uv).a;
        vec4 sweep_color = vec4(u__color.rgb * u__intensity, u__color.a * sweep_effect);
        gl_FragColor = mix(text_color, sweep_color, sweep_effect) * text_color.a;
        """,

        u__base_color= "#C4B454",
        u__color="#FFD700",      # Default sweep color (Red)
        u__softness=1.0,        # Default softness
        u__width=0.10,            # Default width
        u__start_pos=(-2.0, 0.5), # Default starting position (bottom-left)
        u__end_pos=(3.0, 0.5),   # Default ending position (top-right)
        u__intensity=50.0,        # Default intensity
        u__duration=5.0,         # Duration of the sweep effect
        u__delay=0.0,            # Default delay between loops
        redraw = 0.0
    )

    renpy.register_textshader(
        "ColorSweep",
        variables="""
        uniform vec4 u__color;           
        uniform float u__softness;       
        uniform float u__width;          
        uniform float u__angle;          
        uniform float u__direction;      
        uniform float u__intensity;      
        uniform float u__duration;       
        uniform float u__delay;          
        uniform float u_time;            
        varying vec2 v__uv;              
        attribute vec2 a_tex_coord;      
        """,
        vertex_300="""
        v__uv = a_tex_coord;
        """,
        fragment_300="""
        float radians = radians(u__angle);
        vec2 direction = vec2(cos(radians), sin(radians)) * u__direction;
        float overshoot = 2.0; 
        float normalized_time = mod(max(0.0, u_time - u__delay), u__duration) / u__duration;
        float sweep_pos = dot(v__uv, direction) - (normalized_time * (1.0 + overshoot)) + overshoot * 0.5;
        
        float sweep_effect = smoothstep(-u__width - u__softness, -u__width, sweep_pos) 
        - smoothstep(u__width, u__width + u__softness,  sweep_pos);
        vec4 text_color = texture2D(tex0, v__uv);
        vec4 sweep_color = vec4(u__color.rgb * u__intensity, u__color.a * sweep_effect);
        gl_FragColor = mix(text_color, sweep_color, sweep_effect) * text_color.a;"""
        ,
        u__color="#CC00FF",      # Default sweep color (Red)
        u__softness=0.15,         # Default softness
        u__width=0.0,            # Default width
        u__angle=0.0,            # Default angle (horizontal sweep)
        u__direction=1.0,        # Default direction (left-to-right)
        u__intensity=1.0,        # Default intensity
        u__duration=2.0,         # Default duration (2 seconds)
        u__delay=0.0,            # Default delay (no delay)
        redraw =0.0
    )

    renpy.register_textshader(
        "TextShadow",
        variables="""
        uniform vec4 u__shadow_color; 
        uniform vec2 u__offset; 
        uniform vec2 u_model_size;
        varying vec2 v__uv;       
        attribute vec2 a_tex_coord;
        """,
        vertex_300="""
        
        v__uv = a_tex_coord;
        """,
        fragment_300="""
        vec2 shadow_uv = v__uv + (u__offset / u_model_size);
        vec4 shadow_tex = texture2D(tex0, shadow_uv) * u__shadow_color;
        vec4 text_tex = texture2D(tex0, v__uv);
        gl_FragColor = shadow_tex + text_tex; 
        """,

        u__shadow_color="#000000",  
        u__offset=(5.0, -2.0), 
    )

    renpy.register_textshader(
        "3DText",
        variables="""
        uniform vec4 u__highlight_color;
        uniform vec4 u__shadow_color;  
        uniform vec2 u__offset; 
        uniform vec2 u_model_size;     
        varying vec2 v__uv;            
        attribute vec2 a_tex_coord;    
        """,

        vertex_300="""
        v__uv = a_tex_coord;
        """,

        fragment_300="""
        
        vec2 shadow_uv = v__uv + (u__offset / u_model_size);
        vec2 highlight_uv = v__uv + (-u__offset / u_model_size);

        
        vec4 shadow_tex = texture2D(tex0, shadow_uv) * u__shadow_color;
        vec4 highlight_tex = texture2D(tex0, highlight_uv) * u__highlight_color;
        
        vec4 text_tex = texture2D(tex0, v__uv);

        
        gl_FragColor = shadow_tex + text_tex + highlight_tex;
        """,
        u__highlight_color="#007700FF",
        u__shadow_color="#000000FF",
        u__offset=(5.0, -5.0)
    )

    renpy.register_textshader(
        "Gradient",
        variables="""
        uniform vec4 u__start_color;  
        uniform vec4 u__end_color;    
        uniform vec2 u_model_size;   
        varying vec2 v__uv;          
        attribute vec4 a_position;   
        """,
        vertex_300="""

        v__uv = a_position.xy / u_model_size.xy;
        """,

        fragment_300="""
        
        vec4 gradient_color = mix(u__start_color, u__end_color, v__uv.y);

        
        gl_FragColor = texture2D(tex0, v__uv) * gradient_color;
        """,

        u__start_color="#add8e6",  # Default Start Color (Light Blue)
        u__end_color="#FFFFFF",    # Default End Color (Black)
    )

    renpy.register_textshader(
        "RedactedSimple",
        variables="""
        uniform vec4 u__color;
        """,

        vertex_300="""
        """,

        fragment_300="""
               
        gl_FragColor = u__color;
        """,
        u__color="#FF0000FF"
    )

    renpy.register_textshader(
        "HighlightSimple",
        variables="""
        uniform vec4 u__highlightcolor;
        """,

        vertex_300="""
        """,

        fragment_300="""
        float highlight = 1.0 - gl_FragColor.a;       
        gl_FragColor = gl_FragColor + (highlight * u__highlightcolor);
        """,
        u__highlightcolor="#FBF719FF"
    )

    renpy.register_textshader(
        "HighlightRecolor",
        variables="""
        uniform vec4 u__highlightcolor;
        uniform vec4 u__textcolor;
        """,

        vertex_300="""
        """,

        fragment_300="""
        float highlight = 1.0 - gl_FragColor.a;  
        vec4 inverted = vec4((vec3(1.0) - gl_FragColor.rgb), gl_FragColor.a)*gl_FragColor.a; 
        gl_FragColor = u__textcolor + (highlight * u__highlightcolor);
        """,
        u__textcolor = "#000000FF",
        u__highlightcolor="#FBF719FF"
    )

    renpy.register_textshader(
    "Reversed",

    variables="""
    uniform vec2 res0;
    attribute vec4 a_text_pos_rect;

    """,  
    vertex_10="""
    gl_Position.x = (res0.x - gl_Position.x);
    """
)

    renpy.register_textshader(
    "Flipped",

    variables="""
    uniform vec2 res0;
    """,  
    vertex_10="""
    gl_Position.y = (res0.y - gl_Position.y);  
    """
)

    renpy.register_textshader(
    "Cthonic",

    variables="""
    uniform vec2 u_model_size;  // Model size for scaling
    varying vec2 v__uv;  // UV coordinates of the text
    attribute vec4 a_position;  // Position of the text glyph
    uniform sampler2D tex0; 
    """,

    vertex_300="""
    v__uv = a_position.xy / u_model_size.xy;
    """,

    fragment_functions="""
    float rand(vec2 co) {
        return fract(sin(dot(co.xy, vec2(12.9898, 78.233))) * 43758.5453);
    }
    """,

    fragment_300="""
    vec2 uv = v__uv;
    vec4 origin = texture2D(tex0, uv);
    uv.x = abs(0.5 - uv.x);
    vec4 backwards= texture2D(tex0, uv);
    uv.y = abs(0.5 - uv.y);
    vec4 invert = texture2D(tex0, uv);
    gl_FragColor =invert+origin+backwards;
    """,
)

    renpy.register_textshader(
    "CthonicJitter",

    variables="""
    uniform float u_time;
    uniform vec2 u_model_size;  // Model size for scaling
    varying vec2 v__uv;  // UV coordinates of the text
    attribute vec4 a_position;  // Position of the text glyph
    uniform sampler2D tex0; 
    """,

    vertex_300="""
    v__uv = a_position.xy / u_model_size.xy;
    """,

    fragment_functions="""
    float rand(vec2 co) {
        return fract(sin(dot(co.xy, vec2(12.9898, 78.233))) * 43758.5453);
    }
    """,

    fragment_300="""
    vec2 uv = v__uv;
    vec4 origin = texture2D(tex0, uv);

    float glitchOffset = mod(u_time, 0.2) < 0.1 ? 0.02 : 0.0;
    uv.x += glitchOffset * (fract(sin(u_time) * 1000.0) - 0.5);
    vec4 backwards = texture2D(tex0, vec2(abs(0.5 - uv.x), uv.y));
    uv.y += glitchOffset * (fract(cos(u_time) * 1000.0) - 0.5);
    vec4 invert = texture2D(tex0, vec2(abs(uv.x -0.5), abs(1.0 - uv.y)));

    gl_FragColor = invert + origin + backwards;
    """,
    redraw=0.0
)

    renpy.register_textshader(
    "RedactedGlitch",

    variables="""
    uniform float u_time;
    uniform vec2 u_model_size;  // Model size for scaling
    varying vec2 v__uv;  // UV coordinates of the text
    attribute vec4 a_position;  // Position of the text glyph
    uniform sampler2D tex0; 
    uniform float u__glitchFrequency;
    uniform float u__jitterFrequency;
    uniform float u__pulseDelay;
    uniform float u__cuts;
    uniform float u__minChaos;
    uniform float u__maxChaos;    
    uniform float u__jitterIntensity;
    """,

    vertex_300="""
    v__uv = a_position.xy / u_model_size.xy;
    """,

    fragment_functions="""
    float rand(vec2 co) {
        return fract(sin(dot(co.xy, vec2(12.9898, 78.233))) * 43758.5453);
    }
    """,

    fragment_300="""
    vec2 uv = v__uv;
    
    float glitchCut = mod(u_time, u__glitchFrequency) < 0.1 ? u__minChaos : u__maxChaos;
    float glitchPulse = mod(u_time, u__glitchFrequency*u__pulseDelay) < 0.1 ? 0.0 : u__minChaos; 
    vec2 grid = vec2(u__cuts, glitchCut+glitchPulse); // Divide into a grid
  
    vec2 cellID = floor(uv * grid);
    vec2 cellUV = fract(uv * grid);

    float offset = mod(sin(dot(cellID, vec2(12.9898, 78.233))) * 43758.5453, 1.0);
    vec2 shuffledCell = mod(cellID + vec2(offset, offset * 2.0), grid);

    vec2 newUV = (shuffledCell + cellUV) / grid;

    float glitchOffset = mod(u_time, u__jitterFrequency) < 0.1 ? u__jitterIntensity : 0.0;
    newUV.x += glitchOffset * (fract(sin(u_time) * 1000.0) - 0.5);
    newUV.y += glitchOffset * (fract(cos(u_time) * 1000.0) - 0.5);

    vec4 backwards = texture2D(tex0, vec2(abs(0.5 - newUV.x), newUV.y));
    vec4 invert = texture2D(tex0, vec2(newUV.x, abs(0.5 - newUV.y)));
    vec4 origin = texture2D(tex0, newUV);  
    gl_FragColor = invert + backwards + origin;
    """,
    u__glitchFrequency=0.5, #Time between glitch effects.
    u__pulseDelay=1.15, #Multiplier against the glitch frequency for the second layer of glitching.
    u__cuts= 50.0, #Number of horizontal slices made to the text.
    u__minChaos= 6.0, # The minimum number of slices
    u__maxChaos= 10.0, # The maximum number of slices.
    u__jitterFrequency= 0.3,  #Time between jitters.  
    u__jitterIntensity = 0.02, #Intensity of the jitter
    redraw=0.0
)

    renpy.register_textshader(
    "CthonicGlitch",

    variables="""
    uniform float u_time;
    uniform vec2 u_model_size;  // Model size for scaling
    varying vec2 v__uv;  // UV coordinates of the text
    attribute vec4 a_position;  // Position of the text glyph
    uniform sampler2D tex0; 
    uniform float u__glitchFrequency;
    uniform float u__jitterFrequency;
    uniform float u__pulseDelay;
    uniform float u__cuts;
    uniform float u__minChaos;
    uniform float u__maxChaos;    
    uniform float u__jitterIntensity;
    """,

    vertex_300="""
    v__uv = a_position.xy / u_model_size.xy;
    """,

    fragment_functions="""
    float rand(vec2 co) {
        return fract(sin(dot(co.xy, vec2(12.9898, 78.233))) * 43758.5453);
    }
    """,

    fragment_300="""
    vec2 uv = v__uv;
    
    float glitchCut = mod(u_time, u__glitchFrequency) < 0.1 ? u__minChaos : u__maxChaos;
    float glitchPulse = mod(u_time, u__glitchFrequency*u__pulseDelay) < 0.1 ? 0.0 : u__minChaos; 
    vec2 grid = vec2(u__cuts, glitchCut+glitchPulse); // Divide into a grid
  
    vec2 cellID = floor(uv * grid);
    vec2 cellUV = fract(uv * grid);

    float offset = mod(sin(dot(cellID, vec2(12.9898, 78.233))) * 43758.5453, 1.0);
    vec2 shuffledCell = mod(cellID + vec2(offset, offset * 2.0), grid);

    vec2 newUV = (shuffledCell + cellUV) / grid;

    float glitchOffset = mod(u_time, u__jitterFrequency) < 0.1 ? u__jitterIntensity : 0.0;
    newUV.x += glitchOffset * (fract(sin(u_time) * 1000.0) - 0.5);
    newUV.y += glitchOffset * (fract(cos(u_time) * 1000.0) - 0.5);

    vec4 backwards = texture2D(tex0, vec2(abs(0.5 - newUV.x), newUV.y));
    vec4 invert = texture2D(tex0, vec2(newUV.x, abs(0.5 - newUV.y)));
    vec4 origin = texture2D(tex0, uv);  
    gl_FragColor = invert + backwards + origin;
    """,
    u__glitchFrequency=0.5, #Time between glitch effects.
    u__pulseDelay=1.15, #Multiplier against the glitch frequency for the second layer of glitching.
    u__cuts= 50.0, #Number of horizontal slices made to the text.
    u__minChaos= 6.0, # The minimum number of slices
    u__maxChaos= 10.0, # The maximum number of slices.
    u__jitterFrequency= 0.3,  #Time between jitters.  
    u__jitterIntensity = 0.02, #Intensity of the jitter
    redraw=0.0
)

    renpy.register_textshader(
    "CthonicGlitchColor",

    variables="""
    uniform float u_time;
    uniform vec2 u_model_size;  // Model size for scaling
    varying vec2 v__uv;  // UV coordinates of the text
    attribute vec4 a_position;  // Position of the text glyph
    uniform sampler2D tex0; 
    uniform float u__glitchFrequency;
    uniform float u__jitterFrequency;
    uniform float u__pulseDelay;
    uniform float u__cuts;
    uniform float u__minChaos;
    uniform float u__maxChaos;    
    uniform float u__jitterIntensity;
    uniform vec4 u__firstColor;
    uniform vec4 u__secondColor;
    """,

    vertex_300="""
    v__uv = a_position.xy / u_model_size.xy;
    """,

    fragment_functions="""
    float rand(vec2 co) {
        return fract(sin(dot(co.xy, vec2(12.9898, 78.233))) * 43758.5453);
    }
    """,

    fragment_300="""
    vec2 uv = v__uv;
    
    float glitchCut = mod(u_time, u__glitchFrequency) < 0.1 ? u__minChaos : u__maxChaos;
    float glitchPulse = mod(u_time, u__glitchFrequency*u__pulseDelay) < 0.1 ? 0.0 : u__minChaos; 
    vec2 grid = vec2(u__cuts, glitchCut+glitchPulse); // Divide into a grid
  
    vec2 cellID = floor(uv * grid);
    vec2 cellUV = fract(uv * grid);

    float offset = mod(sin(dot(cellID, vec2(12.9898, 78.233))) * 43758.5453, 1.0);
    vec2 shuffledCell = mod(cellID + vec2(offset, offset * 2.0), grid);

    vec2 newUV = (shuffledCell + cellUV) / grid;

    float glitchOffset = mod(u_time, u__jitterFrequency) < 0.1 ? u__jitterIntensity : 0.0;
    newUV.x += glitchOffset * (fract(sin(u_time) * 1000.0) - 0.5);
    newUV.y += glitchOffset * (fract(cos(u_time) * 1000.0) - 0.5);

    vec4 backwards = u__firstColor * texture2D(tex0, vec2(abs(0.5 - newUV.x), newUV.y)).a;
    vec4 invert = u__secondColor * texture2D(tex0, vec2(newUV.x, abs(0.5 - newUV.y))).a;
    vec4 origin = texture2D(tex0, uv);  
    gl_FragColor = invert + backwards + origin;
    """,
    u__glitchFrequency=0.5, #Time between glitch effects.
    u__pulseDelay=1.15, #Multiplier against the glitch frequency for the second layer of glitching.
    u__cuts= 50.0, #Number of horizontal slices made to the text.
    u__minChaos= 6.0, # The minimum number of slices
    u__maxChaos= 10.0, # The maximum number of slices.
    u__jitterFrequency= 0.3,  #Time between jitters.  
    u__jitterIntensity = 0.02, #Intensity of the jitter
    u__firstColor="#880000FF",
    u__secondColor="#000088FF",
    redraw=0.0
)

    renpy.register_textshader(
    "Static",

    variables="""
    uniform float u_time; 
    uniform float u__intensity; 
    uniform float u__seed;  
    uniform vec2 u_model_size;  
    varying vec2 v__uv;  
    attribute vec4 a_position;  
    """,

    vertex_300="""
    v__uv = a_position.xy / u_model_size.xy;
    """,

    fragment_functions="""
    float rand(vec2 co) {
        return fract(sin(dot(co.xy, vec2(12.9898, 78.233))) * 43758.5453);
    }
    """,

    fragment_300="""
    vec2 uv = v__uv;
    vec4 text_color = texture2D(tex0, uv);
    float uv_offset = rand(uv + vec2(u_time, u__seed)) * u__intensity * 0.05;
    uv.x += uv_offset;
    uv.y += uv_offset;
    vec4 scrambled_color = texture2D(tex0, uv);

    // Apply scrambled symbol effect
    gl_FragColor = scrambled_color * text_color.a;
    """,

    u__intensity=0.6,
    u__seed=0.3  
)



    