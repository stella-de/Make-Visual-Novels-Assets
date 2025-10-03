    
    #Flow (For electricity/water)
    #Perlin (For Fire)
    #Emist/Radial (For Light/Warps)
    #Impact Frame Effect
    #Smoke

transform RadialSpeedLines(color=(1.0,1.0,1.0,0.5), alt=(0.0,0.0,0.0,0.5), density=5.0, thickness=0.5, cutoff=0.2):
    mesh True
    shader "MakeVisualNovels.RadialSpeedLines"
    blend "normal"
    u_line_color color
    u_alt_color alt
    u_density density
    u_thickness thickness
    u_center_fade cutoff
    u_flicker_rate (10.0)
    pause 0
    repeat


transform CreateSmoke(color=(0.2, 0.0, 0.2, 0.8), mode="normal",speed=0.05, scale=4.0):
    mesh True
    blend mode
    shader "MakeVisualNovels.ProcSmoke"
    u_smoke_color color
    u_scroll_speed speed
    u_noise_scale scale
    pause 0
    repeat


transform Deluxe(intensity=0.8,light=(1.0,1.0,1.0,1.0), dark=(0.01,0.01, 0.01, 1.0)):
    shader "MakeVisualNovels.MangaDeluxe"
    mesh True
    u_manga_intensity (intensity)
    u_manga_light_color (light)
    u_manga_dark_color (dark)
    u_state (1.0)
    
transform Impact(intensity=0.8,light=(1.0,1.0,1.0,1.0), dark=(0.01,0.01, 0.01, 1.0), duration=0.092, fade=0.023):
    shader "MakeVisualNovels.MangaDeluxe"
    mesh True
    u_manga_intensity (intensity)
    u_manga_light_color (light)
    u_manga_dark_color (dark)
    u_state (1.0)
    linear duration
    ease fade u_state (0.0)


transform Blazing(child,left=0, up=0, right=0, down=0, glowcolor=(0.73,0.0,0.0,1.0), endcolor=(0.99,0.89,0.0,1.0)):
    # Left, Up, Right, Down add extra padding to the displayable this is attached to.
    # Be aware that expanding a displayable can result in your displayable being shifted
    # around, but allows the effect to be drawn in places where your image would otherwise cut off.
    shader "MakeVisualNovels.Blazing"
    mesh True
    mesh_pad (left,up, right, down)
    gl_pixel_perfect True
    u_fps (60.0)
    u_minSmooth (0.0) 
    u_maxSmooth (0.25) 
    u_warpIntensity (550.0)
    u_flipIntensity (0.0)
    u_speed (0.25)
    u_scale (20.0)
    u_flipSpeed (1.0)
    u_flipScale (1.0)
    u_end_color (endcolor)
    u_glow_color (glowcolor)  
    u_glow_intensity (3.0)      
    u_glow_radius (4.0)
    pause 0
    repeat

transform Gloom(child,left=0, up=0, right=0, down=0, glowcolor=(0.73,0.0,0.0,1.0),endcolor=(0.0,0.0,0.0,1.0)):
    # Left, Up, Right, Down add extra padding to the displayable this is attached to.
    # Be aware that expanding a displayable can result in your displayable being shifted
    # around, but allows the effect to be drawn in places where your image would otherwise cut off.
    shader "MakeVisualNovels.Blazing"
    mesh True
    mesh_pad (left,up, right, down)
    gl_pixel_perfect True
    u_fps (60.0)
    u_minSmooth (0.0) 
    u_maxSmooth (0.5) 
    u_warpIntensity (750.0)
    u_flipIntensity (0.0)
    u_speed (0.50)
    u_scale (15.0)
    u_flipSpeed (1.0)
    u_flipScale (1.0)
    u_end_color (endcolor)
    u_glow_color (glowcolor)   
    u_glow_intensity (1.0)      
    u_glow_radius (4.0)
    pause 0
    repeat    

transform Radial(child):
    mesh (True)
    Model().texture(child, texture_wrap=mirror).shader("MakeVisualNovels.Radial")
    u_speed (0.05)
    pause 0
    repeat

transform EMist:
    mesh (True)
    shader "MakeVisualNovels.EMist"
    blend ("add")
    pause 0
    repeat

transform Flow(waves=3.0, complexity=3.33, x=1.5,y=2.5, color=(0.0,0.05,0.1,1.0), mode="normal"):
    mesh (True)
    shader "MakeVisualNovels.Flow"
    blend mode
    u_waves waves
    u_complexity complexity
    u_blend (0.0) # 1.0 to blend with the original texture of the displayable, 0.0 to overwrite.
    u_speed (2.0)
    u_xFreq x
    u_yFreq y
    u_flowColor color
    pause 0
    repeat

transform FlowDemo:
    mesh (True)
    shader "MakeVisualNovels.Flow"
    u_waves (3.0)
    u_complexity(3.33)
    u_blend (0.0) # 1.0 to blend with the original texture of the displayable, 0.0 to overwrite.
    u_speed (2.0)
    u_xFreq (1.5)
    u_yFreq (2.5)
    u_flowColor (0.0,0.05,0.1,1.0)
    blend "normal"
    linear 2.0 u_waves 5.0
    linear 2.0 u_waves 3.0
    linear 2.0 u_yFreq (10.5)
    linear 2.0 u_yFreq (2.5)
    linear 2.0 u_xFreq (10.0)
    linear 2.0 u_xFreq (2.0)
    linear 2.0 u_xFreq (50.0)
    linear 2.0 u_yFreq (50.0)
    linear 2.0 u_xFreq (1.5)
    linear 2.0 u_yFreq (2.5)
    repeat


transform Overflow(waves=3.0, complexity=3.33, x=1.5,y=2.5, color=(0.0,0.05,0.1,1.0), mode="normal"):
    mesh (True)
    shader "MakeVisualNovels.OverlayFlow"
    u_waves waves
    u_complexity complexity
    u_blend (0.0) # 1.0 to blend with the original texture of the displayable, 0.0 to overwrite.
    u_speed (2.0)
    u_xFreq x
    u_yFreq y
    u_flowColor color
    pause 0
    repeat

transform MappedFlow(child):
    Model().shader('MakeVisualNovels.MappedFlow').texture(child,main=True, fit=True).texture("INSERT MASK IMAGE PATH HERE", fit=True)
    u_waves (3.0)
    u_complexity(10.33)
    u_blend (0.0) # 1.0 to blend with the original texture of the displayable, 0.0 to overwrite.
    u_speed (2.0)
    u_xFreq (1.5)
    u_yFreq (2.5)
    u_flowColor (0.1,0.05,0.0,1.0)
    pause 0
    repeat

transform MaskedFlow(mask, child):
    Model().shader('MakeVisualNovels.MappedFlow').texture(child,main=True, fit=True).texture(mask, fit=True)
    u_waves (3.0)
    u_complexity(10.33)
    u_blend (0.0) # 1.0 to blend with the original texture of the displayable, 0.0 to overwrite.
    u_speed (2.0)
    u_xFreq (1.5)
    u_yFreq (2.5)
    u_flowColor (0.1,0.05,0.0,1.0)
    pause 0
    repeat