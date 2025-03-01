# Hey!  Thanks for opening this file.  Doing so, 
# you took your first step with me in taking over 
# the world with visual novels.

# If you, like me, want to see a world dominated by visual novels
# as the one true storytelling medium, then join us over in Discord
# over at https://discord.gg/devtalk or catch me live on Twitch
# https://twitch.tv/MakeVisualNovels

# If you need support for these shaders and transforms or have requests
# idk, go to the Discord I'm probably around doing something.

# Nai @ Make Visual Novels

# Oh, if you use these shaders on layered sprites, make sure you've got Mesh set to true.

transform AnimatedAberate:
    shader "MakeVisualNovels.AnimatedAberration"
    u_aberrationAmount(10.0)

transform StillAberate:
    shader "MakeVisualNovels.StillAberration"
    u_aberrationAmount(10.0)

transform IntenseAberate:
    shader "MakeVisualNovels.StillAberration"
    u_aberrationAmount(50.0)

transform bits16:
    shader "MakeVisualNovels.256colors"

transform bits8:
    shader "MakeVisualNovels.16colors"
   
transform VHS:
    shader "MakeVisualNovels.VHS"
    #Color applies a shift in color.
    #Remember R G B A.  Values are expressed between 0.0 and 1.0
    #See the bottom  of this document for a cheat sheet.
    #Use White vec4(1.0, 1.0, 1.0, 1.0) to disable this effect.
    #Pure black turns the entire image black.
    u_color (1.0, 1.0, 1.0, 1.0)

transform WhiteNoise:
    shader "MakeVisualNovels.Static"
    #See #Color section at the bottom for details.
    u_color (1.0, 1.0, 1.0, 1.0)
    u_intensity (3)
    # 0 for additive(brightening) static, 1 for multiplicative(darkening) static
    # When 0, intensity is inversed and higher numbers are less pronounced.
    # When 1, intensity is normal, and higher numbers are more pronounced.
    # Why? Because math.
    u_mode (0)

transform Static:
    shader "MakeVisualNovels.Static"
    #See #Color section at the bottom for details.
    u_color (1.0, 1.0, 1.0, 1.0)
    u_intensity (1)
    # 0 for additive(brightening) static, 1 for multiplicative(darkening) static
    # When 0, intensity is inversed and higher numbers are less pronounced.
    # When 1, intensity is normal, and higher numbers are more pronounced.
    # Why? Because math.
    u_mode (1)


# A Preset for the Simulated Lighting Shader
# Caution should be exercised when applied to characters
# It may make them too awesome.

transform TransRights:
    shader "MakeVisualNovels.SimulatedLighting"
    u_back_light_color (1.0, 1.0, 1.0) # White  
    u_key_light_color (0, 0, 1.0)  # Blue  
    u_fill_light_color (0, 0.25, 0.2)  # Pink (subtracted from 1)
    u_back_light_direction (1.5, -0.5)
    u_back_light_position (0.0, -0.5)
    u_key_light_position (0.45, 0.2)
    u_key_light_radius (0.5)  
    u_fill_light_direction (-1.0, 0.0)  
    u_back_light_intensity (2)          
    u_key_light_intensity (1)          
    u_fill_light_intensity (-0.7)

transform TheFuzz:
    shader "MakeVisualNovels.SimulatedLighting"
    u_back_light_color (1.0, 0.0, 1.0)  
    u_key_light_color (0.7, 0.7, 1.0)    
    u_fill_light_color (1.0, 1.0, 1.0)    
    u_back_light_direction (1.5, -0.5)
    u_back_light_position (0.0, -0.5)
    u_key_light_position (0.2, 0.2)
    u_key_light_radius (1.0)  
    u_fill_light_direction (-1.0, 0.0)  
    u_back_light_intensity (1)          
    u_key_light_intensity (0.7)          
    u_fill_light_intensity (-0.5) 

# New Animated Templates:
# TheFuzz simulates police lights
# A Preset for the Simulated Lighting Shader
# Doesn't look good, but it does demonstrate the various areas you can illuminate.    

transform LightDemo:
    shader "MakeVisualNovels.SimulatedLighting"  
    u_key_light_color (1.0, 0.0, 1.0)
    u_back_light_color (1.0,1.0,0.0)  
    u_back_light_direction (0.75,0.0)
    u_back_light_position (0.0,1.0)
    u_fill_light_color (1.0, 1.0, 1.0)
    u_key_light_position (0.2, 0.2)
    u_key_light_radius (0.25)  
    u_fill_light_direction (-1.0, 0.0)  
    u_back_light_intensity (1.0)          
    u_key_light_intensity (2.0)          
    u_fill_light_intensity (-1)  
    block:  
        u_key_light_radius(0.25)
        ease 1 u_key_light_position (0.0, 0.0)
        ease 1 u_back_light_direction (0.0,0.0)
        ease 1 u_back_light_position (0.0,0.0)
        pause 2
        ease 1 u_key_light_position (1.0, 1.0)
        ease 1 u_back_light_direction (1.0,1.0)
        ease 1 u_back_light_position (1.0,1.0)
        pause 2
        ease 1 u_key_light_position (0.5, 0.5)
        ease 1 u_back_light_direction (0.0,0.0)
        ease 1 u_back_light_position (1.0,1.0)
        pause 2
        ease 1 u_key_light_radius (0.5)
        ease 1 u_back_light_direction (-1.0,-1.0)
        ease 1 u_back_light_position (1.0,1.0)
        pause 2
        ease 1 u_key_light_position (0.0,0.0)
        ease 1 u_back_light_direction (-1.0,-1.0)
        ease 1 u_back_light_position (0,0)
        pause 2
        ease 1 u_key_light_position (0.0, 1.0)
        ease 1 u_back_light_direction (2.0,2.0)
        ease 1 u_back_light_position (0,0)
        pause 2
        ease 1 u_key_light_position (1.0, 0.0)
        ease 1 u_back_light_direction (-2.0,-2.0)
        ease 1 u_back_light_position (2.0,2.0)
        pause 2
        pause 2
        repeat

# An animated preset for the Simulated Lighting shader
# This was specifically designed to work on a background but it'd work on anything really.

transform DramaticRevealBG:
    shader "MakeVisualNovels.SimulatedLighting"  
    u_key_light_color (1.0, 1.0, 1.0)
    u_back_light_color (0.0,0.0,0.0)  
    u_back_light_direction (10.75,0.0)
    u_back_light_position (0.0,1.0)
    u_fill_light_color (1.0, 1.0, 1.0)
    u_key_light_position (0.5, 0.0)
    u_key_light_radius (0.05)  
    u_fill_light_direction (-1.0, 0.0)  
    u_back_light_intensity (1.0)          
    u_key_light_intensity (1.0)          
    u_fill_light_intensity (-1)  
    block:  
        parallel: 
            linear 2 u_key_light_intensity (2)
        parallel:
            easein 0.5 u_key_light_position (0.2,0.2)
            easein 0.85 u_key_light_position (0.7,0.3)
            easein 0.95 u_key_light_position (0.2,0.4)
            ease 0.5 u_key_light_position (0.5,0.5)
    parallel:
        linear 2 u_key_light_intensity (5)
    parallel:
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        ease 0.1 u_key_light_position (0.5,0.5)
    linear 0.25 u_key_light_radius (1.0)
    u_fill_light_intensity (-0.5)
    pause 0.7
    u_key_light_position(0.5,0.3)
    linear 4 u_key_light_radius(0.5)
    linear 0.2 u_key_light_intensity (0.5)
    u_fill_light_intensity (0)

#A Preset for the Simulated Lighting shader
#This was designed specifically to work with characters, but there's no reason it wouldn't work elsewhere.
#This, when used with tandem with the BG shader, will produce a staggered visual effect that will (usually) reveal the character first.

transform DramaticReveal:
    shader "MakeVisualNovels.SimulatedLighting"  
    u_key_light_color (1.0, 0.3, 0.3)
    u_back_light_color (0.0,0.0,0.0)  
    u_back_light_direction (0.75,0.0)
    u_back_light_position (0.0,1.0)
    u_fill_light_color (1.0, 1.0, 1.0)
    u_key_light_position (0.5, 0.0)
    u_key_light_radius (0.05)  
    u_fill_light_direction (-1.0, 0.0)  
    u_back_light_intensity (3.0)          
    u_key_light_intensity (1.0)          
    u_fill_light_intensity (-1)  
    block:  
        parallel: 
            linear 2 u_key_light_intensity (2)
        parallel:
            easein 0.5 u_key_light_position (0.2,0.2)
            easein 0.85 u_key_light_position (0.7,0.3)
            easein 0.95 u_key_light_position (0.2,0.4)
            ease 0.5 u_key_light_position (0.5,0.5)
    parallel:
        linear 2 u_key_light_intensity (5)

    parallel:
        easeout 0.2 u_key_light_color (1.0,1.0,1.0)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        ease 0.1 u_key_light_position (0.5,0.5)
    linear .5 u_key_light_radius (1.0)
    u_fill_light_intensity (-0.5)
    pause 0.7
    u_back_light_color (1.0,1.0,1.0)
    u_key_light_position(0.5,0.3)
    u_key_light_radius(0.5)
    linear 0.2 u_key_light_intensity (0.1)
    linear 4 u_back_light_intensity (0)
    
    block:
        ease 0.25 u_fill_light_intensity (-0.20)
        ease 0.5 u_fill_light_intensity (-0.15)
        repeat

#A Preset for the Simulated Lighting shader
#Apply this to a layer and it'll effect eveything on the layer as a single unit.  
#mesh True is doing most of the heavy lifting here.
#You can use this to make spotlights, light sweeps, and a number of other things.

transform DramaticLayerReveal:
    mesh True
    shader "MakeVisualNovels.SimulatedLighting"  
    u_key_light_color (1.0, 1.0, 1.0)
    u_back_light_color (0.0,0.0,0.0)  
    u_back_light_direction (0.75,0.0)
    u_back_light_position (0.0,1.0)
    u_fill_light_color (1.0, 1.0, 1.0)
    u_key_light_position (0.5, 0.0)
    u_key_light_radius (0.25)  
    u_fill_light_direction (-1.0, 0.0)  
    u_back_light_intensity (3.0)          
    u_key_light_intensity (0.0)          
    u_fill_light_intensity (-1)  
    block:  
        parallel: 
            linear 2 u_key_light_intensity (1)
        parallel:
            easein 0.5 u_key_light_position (0.2,0.2)
            easein 0.85 u_key_light_position (0.7,0.3)
            easein 0.95 u_key_light_position (0.2,0.4)
            ease 0.5 u_key_light_position (0.5,0.5)
    parallel:
        linear 2 u_key_light_intensity (5)

    parallel:
        easeout 0.2 u_key_light_color (1.0,1.0,1.0)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        easeout 0.1 u_key_light_position (0.55,0.5)
        easeout 0.1 u_key_light_position (0.45,0.5)
        ease 0.1 u_key_light_position (0.5,0.5)
    linear .5 u_key_light_radius (1.0)
    u_fill_light_intensity (-0.5)
    pause 0.7
    u_key_light_position(0.5,0.3)
    u_key_light_radius(0.5)
    linear 0.2 u_key_light_intensity (0.1)
    linear 4 u_back_light_intensity (0)
    block:
        ease 0.25 u_fill_light_intensity (-0.20)
        ease 0.5 u_fill_light_intensity (-0.15)
        repeat


default raveRightRimColor = (0.0,1.0,1.0)
default raveLeftRimColor = (1.0,1.0,1.0)
default raveRightColor = (0.2,0.7,0.7)
default raveLeftColor = (0.7,0.7,0.2)

transform RaveLights:
    #Hey, we're not liable if you use this template as is.  It does contain flashing lights
    #Because it's a rave template.
    shader "MakeVisualNovels.SimulatedLighting"  
    u_key_light_color (0.2, 0.2, 0.7)
    u_back_light_color (0.0,0.0,1.0)  
    u_back_light_direction (0.75,0.0)
    u_back_light_position (0.0,1.0)
    u_fill_light_color (1.0, 1.0, 1.0)
    u_key_light_position (0.2, 0.2)
    u_key_light_radius (0.6)  
    u_fill_light_direction (-1.0, 0.0)  
    u_back_light_intensity (0.25)          
    u_key_light_intensity (0.7)          
    u_fill_light_intensity (-0.5)  
    block:  
        u_back_light_direction (0,5.0)
        u_back_light_position (1,0)
        ease 0.10 u_key_light_color (raveRightColor)   
        u_back_light_color (raveRightRimColor)
        pause 0.1
        ease 0.10 u_back_light_color (0.0,0.5,0.5)
        pause 0.1 
        ease 0.1 u_back_light_color (0.0,1.0,1.0)
        pause 0.2
        u_back_light_direction (-2.5,0.0)
        u_back_light_position (1.0,1.0)
        ease 0.10 u_key_light_color (raveLeftColor)  
        u_back_light_color (raveLeftRimColor)
        pause 0.1
        ease 0.10 u_back_light_color (0.5, 0.5, 0.0)
        pause 0.1
        ease 0.10 u_back_light_color (1.0, 1.0, 0.0)
        pause 0.2
        repeat  
 
# A Preset for the Simulated Lighting Shader
# Caution should be exercised when applied to characters
# It may make them too awesome.

transform Bisexuality:
    shader "MakeVisualNovels.SimulatedLighting"
    u_back_light_color (1.0, 0.0, 1.0)  
    u_key_light_color (0.7, 0.7, 1.0)    
    u_fill_light_color (1.0, 1.0, 1.0)    
    u_back_light_direction (1.5, -0.5)
    u_back_light_position (0.0, -0.5)
    u_key_light_position (0.2, 0.2)
    u_key_light_radius (1.0)  
    u_fill_light_direction (-1.0, 0.0)  
    u_back_light_intensity (1)          
    u_key_light_intensity (0.7)          
    u_fill_light_intensity (-0.5)        


# A Preset for the Simulated Lighting Shader
transform SunsetLighting:
    shader "MakeVisualNovels.SimulatedLighting"
    u_back_light_color (0.9, 0.7, 0.4)  
    u_key_light_color (0.0, 0.0, 0.5)
    u_fill_light_color (0.4, 0.9, 0.9)  
    u_back_light_direction (1.5, -0.5)
    u_back_light_position (0.25, -0.5)
    u_key_light_position (0.45, 0.2)  
    u_key_light_radius (0.8)    
    u_fill_light_direction (-1.0, 0.0)  
    u_back_light_intensity (4)      
    u_key_light_intensity (0.4)          
    u_fill_light_intensity (-0.5)      


# Default Settings for characters, because they're pretty decent
transform SimulatedLighting:
    shader "MakeVisualNovels.SimulatedLighting"
    u_back_light_color (1.0, 1.0, 1.0)  
    u_key_light_color (1.0, 1.0, 1.0)    
    u_fill_light_color (1, 1, 1) # This is typically SUBTRACTED from the sprite since sprites are usually 100% lit.
    u_back_light_direction (1.5, -0.5)
    # Direction of the back light (towards the camera)
    u_back_light_position (0.25, -0.5)  
    # This will be, on average, pretty close to most sprites' faces
    # assuming they're nearly centered in their images and are about 20% down from the top
    u_key_light_position (0.45, 0.2)  
    u_key_light_radius (0.8)        # This is relative to the thing you're lighting. 0.5 is half the size of the thing.  
    u_fill_light_direction (-1.0, 0.0)   # Direction of the rim light (from the side and behind)
    u_back_light_intensity (1)             # Intensity of the back light
    u_key_light_intensity (0.5)              # Intensity of the key light
    # This is really a fill shadow, because light works differently on screens.
    u_fill_light_intensity (-0.5)  


transform Regicide:
    shader "MakeVisualNovels.PerlinWarp"
    # How many changes per second.
    # Higher is more energetic.
    u_fps (6.0)
    # Body Warp Variables.
    # This provides smooth warps of the entire image.
    u_minSmooth (0.0) # Minimum of 0.0
    u_maxSmooth (0.5) # Maximum of 0.5
    u_warpIntensity (2.0)
    u_speed (1.15)
    u_scale (10)
    # Flipping Warp Variables.  
    # This produces more vividly bouncing deformations
    u_flipIntensity (5.0)   
    u_flipSpeed (2.0)
    u_flipScale (100)
    #Consider tacking on 
    #pause 0 
    #and 
    #repeat 
    #to make RenPy actually render it properly.
    
transform VirtualBoy:
    #Why
    shader "MakeVisualNovels.Manga"
    u_color (0.7, 0.1, 0.1, 1.0)
    #Intensity here is 0 to 1 and determines how much of the darker colors are crushed to black.
    u_intensity (0.6)

transform Manga:
    shader "MakeVisualNovels.Manga"
    #Makes the fill color transparent.
    u_color (0.0,0.0,0.0,0.0) 
    #Intensity here is 0 to 1 and determines how much of the darker colors are crushed to black.
    u_intensity (0.6)

transform TakeOnMe:
    shader "MakeVisualNovels.TakeOnMe"
    #Intensity here is 0 to 1 and determines how much of the darker colors are crushed to black.
    u_color (1.0,1.0,1.0,1.0)
    u_intensity (0.6)
    # How many changes per second.
    # Higher is more energetic.
    u_fps (6.0)
    # Body Warp Variables.
    # This provides smooth warps of the entire image.
    u_minSmooth (0.0) # Minimum of 0.0
    u_maxSmooth (0.5) # Maximum of 0.5
    u_warpIntensity (2.0)
    u_speed (1.15)
    u_scale (5)
    # Flipping Warp Variables.  
    # This produces more vividly bouncing deformations
    u_flipIntensity (5.0)  
    u_flipSpeed (0.15)
    u_flipScale (10)
    #Consider tacking on 
    #pause 0 
    #and 
    #repeat 
    #to make RenPy actually render it properly.
    



# Color applies a shift in color.
# Remember R G B A.  Values are expressed between 0.0 and 1.0
# Use White vec4(1.0, 1.0, 1.0, 1.0) to disable these effects.
# Pure black turns the entire image black.


# Color Cheat Sheet!
# Red: vec4(1.0, 0.0, 0.0, 1.0)
# Green: vec4(0.0, 1.0, 0.0, 1.0)
# Blue: vec4(0.0, 0.0, 1.0, 1.0)
# Yellow: vec4(1.0, 1.0, 0.0, 1.0)
# Cyan: vec4(0.0, 1.0, 1.0, 1.0)
# Magenta: vec4(1.0, 0.0, 1.0, 1.0)
# White: vec4(1.0, 1.0, 1.0, 1.0)
# Black: vec4(0.0, 0.0, 0.0, 1.0)
# Gray: vec4(0.5, 0.5, 0.5, 1.0) (a neutral gray)
# Orange: vec4(1.0, 0.5, 0.0, 1.0)
# Purple: vec4(0.5, 0.0, 0.5, 1.0)
# Pink: vec4(1.0, 0.75, 0.8, 1.0)
# Lime: vec4(0.75, 1.0, 0.0, 1.0)
# Teal: vec4(0.0, 0.5, 0.5, 1.0)
# Brown: vec4(0.6, 0.3, 0.1, 1.0)
# Navy: vec4(0.0, 0.0, 0.5, 1.0)
# Maroon: vec4(0.5, 0.0, 0.0, 1.0)
# Olive: vec4(0.5, 0.5, 0.0, 1.0)
# Sky Blue: vec4(0.53, 0.81, 0.92, 1.0)
# Salmon: vec4(0.98, 0.5, 0.45, 1.0)
