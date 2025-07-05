init python:
    from renpy.uguu import GL_MIRRORED_REPEAT, GL_CLAMP_TO_EDGE,GL_REPEAT
    repeat = (GL_REPEAT, GL_REPEAT)
    mirror = (GL_MIRRORED_REPEAT, GL_MIRRORED_REPEAT)


    backgroundShaderCommonVars = """
    varying vec2 v_uv;
    uniform vec2 res0;
    uniform sampler2D tex0;
    uniform float u_time;
    attribute vec2 a_tex_coord;
    varying vec2 v_tex_coord;
    """

    directionalVarsv1 = """
    uniform float u_angle;
    uniform float u_intensity;
    uniform float u_sharpness;
    uniform float u_scatter;
    uniform float u_frequency;
    """

    directionalVars = """
    uniform float u_angle;
    uniform float u_intensity;
    uniform float u_density1;
    uniform float u_density2;
    uniform float u_secondary_strength;
    uniform float u_spread;
    uniform float u_cutoff;
    uniform float u_falloff;
    uniform float u_edge_fade;
    uniform float u_speed;
    uniform float u_seed;
    uniform vec4 u_color;
    uniform vec2 u_origin;
    """

    directionalMaskedVars = """
    uniform float u_angle;
    uniform float u_intensity;
    uniform float u_density1;
    uniform float u_density2;
    uniform float u_secondary_strength;
    uniform float u_spread;
    uniform float u_cutoff;
    uniform float u_falloff;
    uniform float u_edge_fade;
    uniform float u_speed;
    uniform float u_seed;
    uniform vec4 u_color;
    uniform vec2 u_origin;
    uniform sampler2D tex1; //The mask
    """

    bokehVars = """
    uniform float u_time;            // Current time for animation
    uniform float u_density;         // Number of bokeh particles
    uniform vec2 u_speed;            // Drift speed as xy
    uniform float u_brightness;      // Overall brightness control
    uniform float u_scale_min;       // Minimum size of bokeh circles
    uniform float u_scale_max;       // Maximum size of bokeh circles
    uniform vec4 u_color1;           // First bokeh tint (e.g., soft pink)
    uniform vec4 u_color2;           // Second bokeh tint (e.g., warm yellow)
    uniform float u_circles;          //number of circles
    varying vec2 v_tex_coord;         //For solids, probably.
    attribute vec2 a_tex_coord;       //Also for solids
    uniform sampler2D tex0;           //Also probably for solids
    uniform float u_seed;
"""
    bokehFunc = """
    float rand(vec2 co) {
    return fract(sin(dot(co.xy, vec2(12.9898,78.233))) * 43758.5453);
}

// Smooth circular falloff. 0.5625 is 1080/1920
float circle(vec2 uv, vec2 pos, float size) {
    vec2 aspect = vec2(1.0, 0.5625); 
    vec2 adjusted = (uv - pos) * aspect;
    float d = length(adjusted);
    return smoothstep(size, size * 0.7, d);
}
"""

    bokehEffect= """
    vec4 base = texture2D(tex0, v_tex_coord);
    vec2 uv = v_tex_coord;
    vec4 color = vec4(0.0);
    
    for (int i = 0; i < u_circles; i++) {
        if (float(i) >= u_density) break;

        // Create a unique seed per bokeh
        float seed = float(i) * u_seed;
        // Position
        vec2 initPos = vec2(
            rand(vec2(seed+0.1, seed-0.5)),
            rand(vec2(seed, seed+0.5))
        );
        
        // Drift over time
        vec2 pos = initPos + vec2(
            sin(u_time * u_speed.x + seed) * 0.05,
            u_time * u_speed.y * rand(vec2(seed + 4.0, seed + 5.0))
        );
        
        // Wrap around screen (scrolling vertically)
        pos.y = mod(pos.y, 1.2) - 0.1;
        pos.x = mod(pos.x, 1.2) - 0.1;
        
        // size
        float size_ratio = float(i) / (u_circles - 1.0);
        float jitter = rand(vec2(seed + 6.5, seed + 7.5)) * 0.05; //For offsetting sizes
        size_ratio = clamp(size_ratio + jitter, 0.0, 1.0);
       
        
        // Pulsing (slight scale breathing)
        //float pulse = (sin(u_time * (0.5 + rand(vec2(u_seed + 8.0, u_seed + 9.0))) * 2.0) * 0.2 + 1.0);
        //scale *= pulse; // rather than adding directly
        float scale = mix(u_scale_min, u_scale_max, size_ratio);

        // Soft alpha falloff
        float alpha = circle(uv, pos, scale)*mix(u_color1.a,u_color2.a, rand(vec2(u_seed-float(i),u_seed+float(i))));

        // Color blending
        vec4 bokehColor = mix(u_color1, u_color2, rand(vec2(u_seed + 10.0, u_seed + 11.0)));

        color += bokehColor * alpha;
    }

    // Apply overall brightness
    gl_FragColor = vec4(base.rgb + color.rgb * u_brightness, base.a);

"""
## This gets added to the end of the above effect to rewrite how gl_FragColor gets calculated.
    bokehTransparentEffect="""
    gl_FragColor = vec4(color.rgb * u_brightness, clamp(length(color) * u_brightness, 0.0,color.a));
    """

    bloomVars = """
    uniform float u_bloom_threshold;   // brightness cutoff (e.g. 0.7)
    uniform float u_bloom_intensity;   // how strong the bloom is (e.g. 0.5)
    uniform float u_bloom_blur_size;   // pixel spread (e.g. 1.0 / 720.0)
    """

    bloomEffect = """
    vec2 blur_uv = v_tex_coord;
    vec4 bloom_base = gl_FragColor;

    vec3 bloomH = vec3(0.0);
    vec3 bloomV = vec3(0.0);
    float brightness;

    for (int i = -4; i <= 4; i++) {
        float fi = float(i);
        float offset = fi * u_bloom_blur_size;

        // Gaussian the hard way
        float weight = exp(-0.5 * (fi / 2.0) * (fi / 2.0));

        // Horizontal sample (needs something not conditional)
        vec3 sampleH = texture2D(tex0, blur_uv + vec2(offset, 0.0)).rgb;
        brightness = dot(sampleH, vec3(0.299, 0.587, 0.114));
        if (brightness > u_bloom_threshold) {
            bloomH += sampleH * weight;
        }


        // Vertical sample (needs something not conditional)
        vec3 sampleV = texture2D(tex0, blur_uv + vec2(0.0, offset)).rgb;
        brightness = dot(sampleV, vec3(0.299, 0.587, 0.114));
        if (brightness > u_bloom_threshold) {
            bloomV += sampleV * weight;
        }
    }

    vec3 bloom = (bloomH + bloomV) * 0.5;
    vec3 bloomcolor = bloom_base.rgb + bloom * u_bloom_intensity;
    gl_FragColor = vec4(clamp(bloomcolor, 0.0, 1.0), bloom_base.a);
"""
    vignetteVars = """
    uniform float u_vin_radius;        // Distance from center where vignette starts (e.g. 0.5)
    uniform float u_vin_softness;      // How gradual the falloff is (e.g. 0.3)
    uniform float u_vin_strength;      // How strong the vignette tint is (e.g. 0.5)
    uniform vec2  u_vin_center;        // Focus point (0.5, 0.5 = center of screen)
    uniform vec3  u_vin_tint; 
    """

    vignetteEffect = """
    vec2 vin_uv = v_tex_coord;
    float vin_dist = distance(vin_uv, u_vin_center);
    float vignette = smoothstep(u_vin_radius - u_vin_softness, u_vin_radius, vin_dist);
    vec4 base = gl_FragColor;
    vec3 vin_color = mix(base.rgb, u_vin_tint, vignette * u_vin_strength);
    gl_FragColor = vec4(vin_color, base.a);
"""
    
    blissFadeVars= """
    uniform float u_bfe_progress;   // 0.0 to 1.0, controls fade strength
    uniform vec3 u_bfe_tint;       // tint color (usually white or pink)
    """

    blissFadeEffect = """
    vec2 bfe_uv = v_tex_coord;
    vec4 bfe_base = gl_FragColor;
    // Expose image more as progress increases
    vec3 bfe_brightened = bfe_base.rgb + vec3(u_bfe_progress * 2.0); // push brightness
    bfe_brightened = clamp(bfe_brightened, 0.0, 1.0);
    // Blend into tint color based on progress (stronger at higher u_progress)
    vec3 bfe_color = mix(bfe_brightened, u_bfe_tint, pow(u_bfe_progress, 2.0)); // soft curve
    gl_FragColor = vec4(bfe_color, bfe_base.a);
"""
    
    # Should probably just add the existing random
    glintFunctions = """
float rand(vec2 co){
    return fract(sin(dot(co, vec2(12.9898,78.233))) * 43758.5453);
}

vec3 tempToRGB(float t){
    t = clamp(t, 0.25, 1.0);
    return mix(vec3(1.0,0.6,0.3), vec3(0.6,0.8,1.0), t);
}

float airyWithArms(vec2 pos, float radius){
    float d = length(pos) / radius;
    float airy = 1.0 / pow(d + 0.0001, 3.0);
    vec2 armspace1 = pos * vec2(10.0, 0.5);
    vec2 armspace2 = pos * vec2(0.5, 10.0);

    float d1 = max(length(armspace1), 0.01) * 150.0; // no / radius
    float d2 = max(length(armspace2), 0.01) * 150.0;

    float arms = ((1.0 / pow(d1, 3.0)) + (1.0 / pow(d2, 3.0)));
    return airy + 0.5 * arms;
}
"""

    glintVars = """
uniform float u_time;
uniform float u_glint_count;
uniform float u_glint_size;
uniform float u_glint_brightness;
uniform float u_glint_speed;
uniform vec3 u_glint_color;
"""

    glintEffect = """
vec2 uv = v_tex_coord;
vec3 outColour = vec3(0.0);
float outAlpha = 0.0;

for(int i = 0; i < 128; i++){
    if(float(i) >= u_glint_count) break;

    float seed = float(i) * 37.191;

    vec2 basePos = vec2(
        rand(vec2(seed, seed * 1.33)),
        rand(vec2(seed * 2.11, seed + 5.0))
    );

    float angle = rand(vec2(seed + 21.0, seed + 22.0)) * 6.2831;
    vec2 dir = vec2(cos(angle), sin(angle));
    vec2 drift = dir * u_time * u_glint_speed;

    vec2 p = mod(basePos + drift, 1.0);

    float sizeVar = mix(0.8, 1.2, rand(vec2(seed + 7.0, seed + 9.0)));
    float radius = u_glint_size * sizeVar;
    float T = rand(vec2(seed + 13.0, seed + 17.0));
    vec3 starRGB = tempToRGB(T);
    float twinkle = 0.6 + 0.4 * sin(u_time * 1.7 + seed);

    vec2 aspect = vec2(1.0, 0.5625);
    vec2 pos = (uv - p) * aspect;

    float intensity = airyWithArms(pos, radius) * twinkle;

    outColour += u_glint_color * intensity * u_glint_brightness;
    outAlpha += intensity * 0.5;
}

outColour = clamp(outColour, 0.0, 1.0);
outAlpha = clamp(outAlpha, 0.0, 1.0);
gl_FragColor = vec4(outColour, outAlpha);
"""


    starsFunctions = """
float rand(vec2 co){
    return fract(sin(dot(co, vec2(12.9898,78.233))) * 43758.5453);
}

vec3 tempToRGB(float t){
    t = clamp(t, 0.25, 1.0);
    return mix(vec3(1.0,0.6,0.3), vec3(0.6,0.8,1.0), t);
}

float airyWithArms(vec2 pos, float radius){
    float d = length(pos) / radius;
    float airy = 1.0 / pow(d + 0.0001, 3.0);
    float d1 = length(pos * vec2(50.0, 0.5)) / radius;
    float d2 = length(pos * vec2(0.5, 50.0)) / radius;
    float arms = (1.0 / pow(d1 + 0.0001, 3.0)) + (1.0 / pow(d2 + 0.0001, 3.0));
    return airy + 0.5 * arms;
}
"""

    starsVars = """
uniform float u_time;
uniform float u_star_count;
uniform float u_star_size;
uniform float u_star_brightness;
"""

    starsEffect = """
vec2 uv = v_tex_coord;
vec3 outColour = vec3(0.0);
float outAlpha = 0.0;

for(int i = 0; i < 128; i++){
    if(float(i) >= u_star_count) break;

    float seed = float(i) * 37.191;
    vec2 p = vec2(
        rand(vec2(seed, seed * 1.33)),
        rand(vec2(seed * 2.11, seed + 5.0))
    );

    float sizeVar = mix(0.8, 1.2, rand(vec2(seed + 7.0, seed + 9.0)));
    float radius = u_star_size * sizeVar;
    float T = rand(vec2(seed + 13.0, seed + 17.0));
    vec3 starRGB = tempToRGB(T);
    float twinkle = 0.6 + 0.4 * sin(u_time * 1.7 + seed);

    vec2 aspect = vec2(1.0,0.5625);
    vec2 pos = (uv - p) * aspect;

    float intensity = airyWithArms(pos, radius) * twinkle;

    outColour += starRGB * intensity * u_star_brightness;
    outAlpha += intensity * 0.5;
}

outColour = clamp(outColour, 0.0, 1.0);
outAlpha = clamp(outAlpha, 0.0, 1.0);
gl_FragColor = vec4(outColour, outAlpha);
"""

    directionalMaskedGodRays = """
    vec2 uv = v_tex_coord;
    //This is here so you can use degrees in the transforms and get somewhat sensible outputs.
    float angle_radians = u_angle * 0.017453292519943295; // (Pi/180)
    float ca = cos(angle_radians);
    float sa = sin(angle_radians);

    vec2 centered = uv - u_origin;
    vec2 transformed = vec2(
    centered.x * ca - centered.y * sa,
    centered.x * sa + centered.y * ca);
    
    // Apply spread (depth fake)
    //transformed /= ((uv.y + u_spread) - (uv.y * u_spread)); 
    transformed /= ((centered.y * ca + centered.x * sa) + u_spread) - ((centered.y * ca + centered.x * sa) * u_spread);

    // --- Animated ray noise ---
    float drift = u_time * u_speed;

    float primary = sin(transformed.x * u_density1 + drift + u_seed);
    float secondary = sin(transformed.x * u_density2 + -drift * 2.0 + u_seed);

    float rays = primary * 0.5 + 0.5; // normalize [-1,1] -> [0,1]
    rays += (secondary * 0.5 + 0.5) * u_secondary_strength;

    rays = clamp(rays, 0.0, 1.0);

    float beam_axis_distance = abs(transformed.x);

    float cut = step(u_cutoff, beam_axis_distance);
    rays *= cut;

    rays *= smoothstep(u_cutoff, u_cutoff + u_edge_fade, beam_axis_distance);
    rays *= smoothstep(0.0, u_falloff, 1.0 - uv.y);

    float mask = texture2D(tex1, v_tex_coord).r; 
    rays *= mask;

    // --- Final color blending ---
    vec3 base_color = texture2D(tex0, v_tex_coord).rgb;
    vec3 ray_color = u_color.rgb * rays * u_intensity;

    vec3 final = mix(base_color, ray_color, rays);

    gl_FragColor = vec4(final * texture2D(tex0, v_tex_coord).a, texture2D(tex0, v_tex_coord).a);
    """
    directionalGodRays = """
    vec2 GODuv = v_tex_coord;
    //This is here so you can use degrees in the transforms and get somewhat sensible outputs.
    float angle_radians = u_angle * 0.017453292519943295; // (Pi/180)
    float ca = cos(angle_radians);
    float sa = sin(angle_radians);

    vec2 centered = GODuv - u_origin;
    vec2 transformed = vec2(
    centered.x * ca - centered.y * sa,
    centered.x * sa + centered.y * ca);
    
    // Apply spread (depth fake)
    //transformed /= ((GODuv.y + u_spread) - (GODuv.y * u_spread)); 
    transformed /= ((centered.y * ca + centered.x * sa) + u_spread) - ((centered.y * ca + centered.x * sa) * u_spread);

    // --- Animated ray noise ---
    float drift = u_time * u_speed;

    float primary = sin(transformed.x * u_density1 + drift + u_seed);
    float secondary = sin(transformed.x * u_density2 + -drift * 2.0 + u_seed);

    float rays = primary * 0.5 + 0.5; // normalize [-1,1] -> [0,1]
    rays += (secondary * 0.5 + 0.5) * u_secondary_strength;

    rays = clamp(rays, 0.0, 1.0);

    float beam_axis_distance = abs(transformed.x);

    float cut = step(u_cutoff, beam_axis_distance);
    rays *= cut;

    rays *= smoothstep(u_cutoff, u_cutoff + u_edge_fade, beam_axis_distance);
    rays *= smoothstep(0.0, u_falloff, 1.0 - GODuv.y);


    // --- Final color blending ---
    //Grabbing it from gl_FragColor lets you composite the effects more readily.
    vec3 base_color = gl_FragColor.rgb;
    vec3 ray_color = u_color.rgb * rays * u_intensity;

    vec3 GODfinal = mix(base_color, ray_color, rays);

    gl_FragColor = vec4(GODfinal * texture2D(tex0, v_tex_coord).a, texture2D(tex0, v_tex_coord).a);
    """

    replacerRays = """
    GODfinal = mix(vec3(0.0), ray_color,rays);
    gl_FragColor = vec4(GODfinal, texture2D(tex0, v_tex_coord).a);
    
    """


#1 GodRays

    renpy.register_shader("MakeVisualNovels.MaskRays",
        variables=backgroundShaderCommonVars+directionalMaskedVars,   
        vertex_300="""
        v_tex_coord = a_tex_coord;
        """,
        fragment_300=directionalMaskedGodRays         
)

    renpy.register_shader("MakeVisualNovels.ReplaceRays",
        variables=backgroundShaderCommonVars+directionalVars,   
        vertex_300="""
        v_tex_coord = a_tex_coord;
        """,
        fragment_300=directionalGodRays+replacerRays       
)

    renpy.register_shader("MakeVisualNovels.GodRays",
        variables=backgroundShaderCommonVars+directionalVars,   
        vertex_300="""
        v_tex_coord = a_tex_coord;
        """,
        fragment_300=directionalGodRays         
)

# 2 Bokeh
    renpy.register_shader("MakeVisualNovels.Bokeh",
        variables=bokehVars,   
        vertex_300="""
        v_tex_coord = a_tex_coord;
        """,
        fragment_functions=bokehFunc,
        fragment_300=bokehEffect         
)
    renpy.register_shader("MakeVisualNovels.BokehTransparent",
        variables=bokehVars,   
        vertex_300="""
        v_tex_coord = a_tex_coord;
        """,
        fragment_functions=bokehFunc,
        fragment_300=bokehEffect+bokehTransparentEffect         
)

# 3 Stars/Sparkles
    renpy.register_shader("MakeVisualNovels.StarsPart",
        variables=starsVars,   
        vertex_300="""
        v_tex_coord = a_tex_coord;
        """,
        fragment_functions=starsFunctions,
        fragment_500=starsEffect         
)

    renpy.register_shader("MakeVisualNovels.GlintPart",
        variables=glintVars,   
        vertex_300="""
        v_tex_coord = a_tex_coord;
        """,
        fragment_functions=glintFunctions,
        fragment_500=glintEffect         
)

# 4 Exposure + Transition Fade
    renpy.register_shader("MakeVisualNovels.Bloom",
        variables=bloomVars+backgroundShaderCommonVars,   
        vertex_300="""
        v_tex_coord = a_tex_coord;
        """,
        fragment_500=bloomEffect         
)
    renpy.register_shader("MakeVisualNovels.BlissFade",
        variables=blissFadeVars+backgroundShaderCommonVars,   
        vertex_300="""
        v_tex_coord = a_tex_coord;
        """,
        fragment_500=blissFadeEffect         
)

# 5 Vingette
    renpy.register_shader("MakeVisualNovels.LPVingette",
        variables=vignetteVars+backgroundShaderCommonVars,   
        vertex_300="""
        v_tex_coord = a_tex_coord;
        """,
        fragment_500=vignetteEffect         
)

    