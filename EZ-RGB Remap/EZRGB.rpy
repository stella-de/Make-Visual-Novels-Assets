init python:
    rgbCommonVars="""
    attribute vec2 a_tex_coord;
    varying vec2 v_tex_coord;
    uniform sampler2D tex0;
    """

    rgbRemapVars = """
uniform sampler2D tex1;
uniform float u_remap_strength;
"""

   
    rgbRemapEffect = """
precision highp float;
vec4 base = texture2D(tex0, v_tex_coord);
vec2 remapUV = vec2(base.r, base.g);
vec3 remapped = texture2D(tex1, remapUV).rgb;
vec3 finalColor = mix(base.rgb, remapped, u_remap_strength);
gl_FragColor = vec4(finalColor*base.a, base.a);
"""



    renpy.register_shader("MakeVisualNovels.RGBMap",
        variables=rgbRemapVars+rgbCommonVars,   
        vertex_300="""
        v_tex_coord = a_tex_coord;
        """,
        fragment_500=rgbRemapEffect         
)


