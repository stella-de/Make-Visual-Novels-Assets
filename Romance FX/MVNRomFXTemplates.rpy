transform NegaGlint:
    mesh True
    shader "MakeVisualNovels.GlintPart"
    blend "multiply"
    u_glint_count (500.0)
    u_glint_brightness (1.2)
    u_glint_size (0.005)
    u_glint_speed (0.00)

transform NyoomMotes:
    mesh True
    shader "MakeVisualNovels.GlintPart"
    blend "add"
    u_glint_count (50.0)
    u_glint_brightness (1.0)
    u_glint_size (0.015)
    u_glint_speed (2.5)
    u_glint_color (0.4,0.7,0.8)
    pause 0
    repeat

transform MoonMotes:
    mesh True
    shader "MakeVisualNovels.GlintPart"
    blend "add"
    u_glint_count (30.0)
    u_glint_brightness (0.8)
    u_glint_size (0.005)
    u_glint_speed (0.005)
    u_glint_color (0.4,0.7,0.8)
    pause 0
    repeat

transform Glint:
    mesh True
    shader "MakeVisualNovels.GlintPart"
    blend "normal"
    u_glint_count (30.0)
    u_glint_brightness (1.0)
    u_glint_size (0.005)
    u_glint_speed (0.005)
    u_glint_color (0.8,0.6,0.4)
    pause 0
    repeat

    
transform BlissEffect:
    mesh True
    shader "MakeVisualNovels.BlissFade"
    u_bfe_tint (1.0, 1.0, 1.0)
    u_bfe_progress (0.0)
    linear 3.5 u_bfe_progress (1.0)
    

transform OtomeBrains:
    mesh True
    shader "MakeVisualNovels.LPVingette"
    u_vin_radius (0.7)       # start vignette halfway from center to edge
    u_vin_softness (0.3)     # wider = smoother transition
    u_vin_strength (0.5)     # 0.0 = no effect, 1.0 = full tint
    u_vin_center (0.5, 0.5)  # center of screen
    u_vin_tint (0.5, 0.05, 0.05)  # black for classic vignette
    pause 0
    repeat

transform MVNVignette:
    mesh True
    shader "MakeVisualNovels.LPVingette"
    u_vin_radius (0.5)       # start vignette halfway from center to edge
    u_vin_softness (0.3)     # wider = smoother transition
    u_vin_strength (0.5)     # 0.0 = no effect, 1.0 = full tint
    u_vin_center (0.5, 0.5)  # center of screen
    u_vin_tint (0.0, 0.0, 0.0)  # black for classic vignette

""" I cheated and turned it into a string to comment this out.   
transform NightLighting:
    mesh True
    shader "MakeVisualNovels.SimulatedLighting"
    u_rim_light_color (0.1, 0.7, 0.9)  
    u_key_light_color (0.4, 0.7, 0.9 )
    u_fill_light_color (0.9, 0.9, 0.7)  
    u_rim_light_radius (0.4)
    u_key_light_position (0.1,0.182)
    u_rim_light_position (0.1,0.182)
    u_key_light_radius (0.0)    
    u_fill_light_direction (-1.0, 0.0)  
    u_rim_light_intensity (2.0)      
    u_key_light_intensity (0.8)          
    u_fill_light_intensity (-0.5)  
    pause 0
    repeat   
"""

transform MVNBubbles: 
    shader "MakeVisualNovels.BokehTransparent"
    blend "add"
    u_circles (20.0)
    u_density (50.0)
    u_speed (0.5,-0.05)
    u_brightness (1.5)
    u_scale_min (0.001)
    u_scale_max (0.03)
    u_color1 (0.3,0.6,2.0,0.5)
    u_color2 (0.15,0.3,2.0,1.0)
    u_seed (10.0)
    pause 0
    repeat
    
transform MVNBubbleBlast:
    shader "MakeVisualNovels.BokehTransparent"
    blend "normal"
    u_circles (20.0)
    u_density (50.0)
    u_speed (-1.0,-0.65)
    u_brightness (1.5)
    u_scale_min (0.001)
    u_scale_max (0.03)
    u_color1 (0.3,0.6,2.0,0.5)
    u_color2 (0.15,0.3,2.0,1.0)
    u_seed (10.0)
    pause 0
    repeat

transform ColorBokeh(amount, density, mode, speed, color1, color2):
    shader "MakeVisualNovels.BokehTransparent"
    blend mode
    u_circles (amount)
    u_density (density)
    u_speed (speed)
    u_brightness (1.5)
    u_scale_min (0.001)
    u_scale_max (0.03)
    u_color1 (color1)
    u_color2 (color2)
    u_seed (10.0)
    pause 0
    repeat

transform CreateBokeh(amount, density, mode, speed):
    shader "MakeVisualNovels.BokehTransparent"
    blend mode
    u_circles (amount)
    u_density (density)
    u_speed (speed)
    u_brightness (0.6)
    u_scale_min (0.01)
    u_scale_max (0.1)
    u_color1 (2.0, 0.8, 0.9,0.25)
    u_color2 (2.0, 0.5, 0.5,0.25)
    u_seed (10.0)
    pause 0
    repeat

transform AddBokeh:
    shader "MakeVisualNovels.BokehTransparent"
    blend "add"
    u_circles (100.0)
    u_density (50.0)
    u_speed (0.003)
    u_brightness (0.8)
    u_scale_min (0.02)
    u_scale_max (0.06)
    u_color1 (2.0, 0.8, 0.9,0.5)
    u_color2 (2.0, 0.5, 0.5,0.5)
    u_seed (5.0)
    pause 0
    repeat

transform Bokeh:
    shader "MakeVisualNovels.Bokeh"
    u_circles (15.0)
    u_density (1.0)
    u_speed (0.003)
    u_brightness (2.0)
    u_scale_min (0.02)
    u_scale_max (0.06)
    u_color1 (1.0, 0.8, 0.9)
    u_color2 (1.0, 0.9, 0.7)
    u_seed (5.0)
    pause 0
    repeat

transform MoonBloom:
    shader "MakeVisualNovels.Bloom"
    u_bloom_threshold (0.70)
    u_bloom_intensity (0.02)
    u_bloom_blur_size (6.0 / 720.0)

transform FuzzyBloom:
    shader "MakeVisualNovels.Bloom"
    u_bloom_threshold (0.95)
    u_bloom_intensity (0.10)
    u_bloom_blur_size (3.0 / 720.0)

transform Bloom:
    shader "MakeVisualNovels.Bloom"
    u_bloom_threshold (0.95)
    u_bloom_intensity (0.07)
    u_bloom_blur_size (3.0 / 720.0)

transform Moonrays:
    shader "MakeVisualNovels.ReplaceRays"
    blend "add"
    u_angle (90.0)          #The angle of the godrays emission from their origin.
    u_origin (-1.0, 0.5)   #Anchor-Origin relative to the thing you put it on.  Can start outside.
    u_intensity (0.15)       #Brightness boost, basically.  Bigger numbers = brighter effect.
    u_density1 (30.0)       #The density/thickness of 1 set of rays
    u_density2 (100.0)      #The density/thickness for the other set of rays.
    u_secondary_strength (0.5) #The power of the second set of rays relative to the first. 0.0 = off.
    u_spread (1.1)          #The size of the spread of the rays. 0. is basically a sunburst
    u_cutoff (-0.1)          #The location of edges of the spread of god rays
    u_edge_fade (0.4)       #The intensity & reach of the fade towards the edge.
    u_falloff (0.5)         #How rapidly the beams decay vertically. Higher = weaker beams
    u_speed (0.1)           #How fast the ray drifting happens. 0.0 = no movement, negatives reverse.
    u_seed (5.0)            #Seed for psuedorandomized placement of rays
    u_color (0.5, 0.8, 0.8, 1.0) # Color of your godrays.
    pause 0                 #Needed for any animated effect tbh
    repeat                  #Needed for any animated effect tbh


transform Demorays:
    shader "MakeVisualNovels.ReplaceRays"
    blend "add"
    u_angle (20.0)          #The angle of the godrays emission from their origin.
    u_origin (-0.4, -0.1)   #Anchor-Origin relative to the thing you put it on.  Can start outside.
    u_intensity (0.8)       #Brightness boost, basically.  Bigger numbers = brighter effect.
    u_density1 (30.0)       #The density/thickness of 1 set of rays
    u_density2 (100.0)      #The density/thickness for the other set of rays.
    u_secondary_strength (0.8) #The power of the second set of rays relative to the first. 0.0 = off.
    u_spread (1.0)          #The size of the spread of the rays. 0. is basically a sunburst
    u_cutoff (0.1)          #The location of edges of the spread of god rays
    u_edge_fade (0.8)       #The intensity & reach of the fade towards the edge.
    u_falloff (1.5)         #How rapidly the beams decay vertically. Higher = weaker beams
    u_speed (0.1)           #How fast the ray drifting happens. 0.0 = no movement, negatives reverse.
    u_seed (5.0)            #Seed for psuedorandomized placement of rays
    u_color (1.0, 0.8, 0.5, 1.0) # Color of your godrays.
    pause 0                 #Needed for any animated effect tbh
    repeat                  #Needed for any animated effect tbh

#   You need to tune this to your scenes when you use it.
#   These values were tuned to work with a scene already tuned with my SunsetLighting transform
#   from my MVN Renpy Shader Pack, which applies color modifications.

transform Godrays:
    shader "MakeVisualNovels.GodRays"
    u_angle (30.0)          #The angle of the godrays emission from their origin.
    u_origin (-0.4, -0.1)   #Anchor-Origin relative to the thing you put it on.  Can start outside.
    u_intensity (3.0)       #Brightness boost, basically.  Bigger numbers = brighter effect.
    u_density1 (30.0)       #The density/thickness of 1 set of rays
    u_density2 (100.0)      #The density/thickness for the other set of rays.
    u_secondary_strength (0.8) #The power of the second set of rays relative to the first. 0.0 = off.
    u_spread (1.0)          #The size of the spread of the rays. 0. is basically a sunburst
    u_cutoff (0.1)          #The location of edges of the spread of god rays
    u_edge_fade (0.8)       #The intensity & reach of the fade towards the edge.
    u_falloff (1.5)         #How rapidly the beams decay vertically. Higher = weaker beams
    u_speed (0.1)           #How fast the ray drifting happens. 0.0 = no movement, negatives reverse.
    u_seed (5.0)            #Seed for psuedorandomized placement of rays
    u_color (1.0, 0.8, 0.7, 1.0) # Color of your godrays.
    pause 0                 #Needed for any animated effect tbh
    repeat                  #Needed for any animated effect tbh


transform MaskedRays(mask, child):
    Model().shader("MakeVisualNovels.MaskRays").texture(child).texture(mask)
    u_angle (30.0)          #The angle of the godrays emission from their origin.
    u_origin (-0.4, -0.1)   #Anchor-Origin relative to the thing you put it on.  Can start outside.
    u_intensity (3.0)       #Brightness boost, basically.  Bigger numbers = brighter effect.
    u_density1 (30.0)       #The density/thickness of 1 set of rays
    u_density2 (100.0)      #The density/thickness for the other set of rays.
    u_secondary_strength (0.8) #The power of the second set of rays relative to the first. 0.0 = off.
    u_spread (1.0)          #The size of the spread of the rays. 0. is basically a sunburst
    u_cutoff (0.1)          #The location of edges of the spread of god rays
    u_edge_fade (0.8)       #The intensity & reach of the fade towards the edge.
    u_falloff (1.5)         #How rapidly the beams decay vertically. Higher = weaker beams
    u_speed (2.0)           #How fast the ray drifting happens. 0.0 = no movement, negatives reverse.
    u_seed (5.0)            #Seed for psuedorandomized placement of rays
    u_color (1.0, 0.8, 0.7, 1.0) # Color of your godrays.
    pause 0                 #Needed for any animated effect tbh
    repeat                  #Needed for any animated effect tbh
