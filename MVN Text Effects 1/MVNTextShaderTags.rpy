    # Use tags in  {TAG}{/TAG} to produce the effects.
    # {blackout} <- A customized version of RedactedSimple to make it black instead of red.
    # {purple} <- A customized version of one of the fire shaders to make it purple and smaller.
   
    # Premade tags for all included shaders using default settings:
    # {ghostwrite}
    # {burningforbigtext}
    # {burningforsmalltext}
    # {blueburnbig}
    # {blueburnsmall}
    # {demo}
    # {hollowglow}
    # {gradientglow}
    # {glow}
    # {redalert}
    # {prey}
    # {goldsweep}
    # {colorsweep}
    # {textshadow}
    # {gradient}
    # {reversed}
    # {flipped}
    # {cthonic}
    # {cthonicjitter}
    # {redactedglitch}
    # {cthonicglitch}
    # {cthonicglitchcolor}
    # {static}


init python:
    
    # You can pass parameters to easily customize shaders and then include them into a tag to allow you to shorthand 
    # complex shader reconfigurations without editing the shader code or bloating your script. 
    # I've included all of the variables of each of the bundled shaders for you, and provided a few sample tag definitions.

    
    #Example 1:
    #RedactedSimple defaults to obscuring the text with a solid red color.  This does the same thing, but makes the color black.
    #This works by making a custom tag pass the shader we want with the alternative settings attached to it after a colon.
    
    def blackout_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=RedactedSimple:u__color=#000000FF"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

    #This makes it into a tag you can use in text, via {blackout}TEXTHERE{/blackout}
    config.custom_text_tags["blackout"] = blackout_tag

    
    #Example 2:
    # BurningForBigText: The shaders come with pre-built blue and red fire shaders. Let smake it a purple and reduce the radius
    # instead for a sligihtly more complex preset.
    
    # u__end_color="#00BBBB66"
    # u__glow_color="#0000BBFF"    
    # u__glow_radius=1.0"

    def purplefire_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=BurningForBigText:u__end_color=#660066FF:u__glow_color=#440044FF:u__glow_radius=1.0"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

    #The name of the tag can be anything.  Instead of a {purplefire} tag, I just made it {purple}
    config.custom_text_tags["purple"] = purplefire_tag



    def ghostwrite_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=GhostWrite"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

        # u__fps= 15.0
        # u__minSmooth= 0.0 
        # u__maxSmooth= 0.5 
        # u__warpIntensity= 300.0
        # u__speed= -1.55
        # u__scale= 1.55
        # u__flipIntensity= 1.0
        # u__flipSpeed= 1.0
        # u__flipScale= 1.0
        # u__end_color="#00880066"
        # u__glow_color="#00000000"    
        # u__glow_intensity=5.0      
        # u__glow_radius=4.0         


    def burningforbigtext_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=BurningForBigText"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

        # u__fps= 60.0,
        # u__minSmooth= 0.0, 
        # u__maxSmooth= 0.5, 
        # u__warpIntensity= 50.0,
        # u__speed= 0.15,
        # u__scale= 25.0,
        # u__flipIntensity= 0.0,
        # u__flipSpeed= 1.0,
        # u__flipScale= 1.0,
        # u__end_color="#BBBB0066",
        # u__glow_color="#BB0000FF",    
        # u__glow_intensity=5.0,      
        # u__glow_radius=4.0         

    def burningforsmalltext_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=BurningForSmallText"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

        # u__fps= 60.0,
        # u__minSmooth= 0.0, 
        # u__maxSmooth= 0.0, 
        # u__warpIntensity= 50.0,
        # u__speed= 0.15,
        # u__scale= 5.0,
        # u__flipIntensity= 0.0,
        # u__flipSpeed= 1.0,
        # u__flipScale= 1.0,
        # u__end_color="#BBBB0066",
        # u__glow_color="#BB0000FF",    
        # u__glow_intensity=5.0,      
        # u__glow_radius=4.0     

    def blueburnbig_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=BlueBurnBig"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

    # u__fps= 60.0,
        # u__minSmooth= 0.0, 
        # u__maxSmooth= 0.5, 
        # u__warpIntensity= 50.0,
        # u__speed= 0.15,
        # u__scale= 25.0,
        # u__flipIntensity= 0.0,
        # u__flipSpeed= 1.0,
        # u__flipScale= 1.0,
        # u__end_color="#00BBBB66",
        # u__glow_color="#0000BBFF",    
        # u__glow_intensity=5.0,      
        # u__glow_radius=4.0     

    def blueburnsmall_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=BlueBurnSmall"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

     # u__fps= 60.0,
        # u__minSmooth= 0.0, 
        # u__maxSmooth= 0.0, 
        # u__warpIntensity= 50.0,
        # u__speed= 0.15,
        # u__scale= 5.0,
        # u__flipIntensity= 0.0,
        # u__flipSpeed= 1.0,
        # u__flipScale= 1.0,
        # u__end_color="#00BBBB66",
        # u__glow_color="#0000BBFF",    
        # u__glow_intensity=5.0,      
        # u__glow_radius=4.0      

    def adjustableburndemo_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=AdjustableBurnDemo"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

     # u__fps= 60.0,
        # u__minSmooth= 0.0, 
        # u__maxSmooth= 0.5, 
        # u__warpIntensity= 50.0,
        # u__speed= 0.55,
        # u__scale= 25.0,
        # u__flipIntensity= 0.0,
        # u__flipSpeed= 1.0,
        # u__flipScale= 1.0,
        # u__end_color="#BBBB0066", #lmao I'm lazy, these don't do anything on the demo.
        # u__glow_color="#BB0000FF",    
        # u__glow_intensity=4.0,      
        # u__glow_radius=7.0         

    def hollowglow_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=HollowGlow"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]
    
    # u__end_color="#FF00FF",
    # u__glow_color="#FFFF00",    
    # u__glow_intensity=5.0,      
    # u__glow_radius=3.0, 

    def gradientglow_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=gradientglow"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]
    
    # u__end_color="#FF00FF",
    # u__glow_color="#FFFF00",    # Default glow color (White)
    # u__glow_intensity=3.0,      # Default glow intensity
    # u__glow_radius=6.0,         # Default glow radius

    def glow_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=Glow"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

    # u__glow_color="#FFFFFF",    # Default glow color (White)
    # u__glow_intensity=2.0,      # Default glow intensity
    # u__glow_radius=5.0,         # Default glow radius

    def redalert_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=RedAlert"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

        # u__color="#FF0000",      
        # u__intensity=1.0,        
        # u__duration=1.0,         
        # u__delay=1.0,            
        

    def prey_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=Prey"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

        # u__color="#770000",      # Default sweep color (Red)
        # u__softness=0.1,        # Default softness
        # u__width=0.50,            # Default width
        # u__start_pos=(-1.0, 0.5), # Default starting position (bottom-left)
        # u__end_pos=(2.0, 0.5),   # Default ending position (top-right)
        # u__intensity=1.0,        # Default intensity
        # u__duration=2.0,         # Duration of the sweep effect
        # u__delay=1.0,            # Default delay between loops

    def goldsweep_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=GoldSweep"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

        # u__base_color= "#C4B454",
        # u__color="#FFD700",      # Default sweep color (Red)
        # u__softness=1.0,        # Default softness
        # u__width=0.10,            # Default width
        # u__start_pos=(-2.0, 0.5), # Default starting position (bottom-left)
        # u__end_pos=(3.0, 0.5),   # Default ending position (top-right)
        # u__intensity=50.0,        # Default intensity
        # u__duration=5.0,         # Duration of the sweep effect
        # u__delay=0.0,            # Default delay between loops

    def colorsweep_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=ColorSweep"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

        # u__color="#CC00FF",      # Default sweep color (Red)
        # u__softness=0.15,         # Default softness
        # u__width=0.0,            # Default width
        # u__angle=0.0,            # Default angle (horizontal sweep)
        # u__direction=1.0,        # Default direction (left-to-right)
        # u__intensity=1.0,        # Default intensity
        # u__duration=2.0,         # Default duration (2 seconds)
        # u__delay=0.0,            # Default delay (no delay)

    def textshadow_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=TextShadow"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]
    
        # u__shadow_color="#000000"
        # u__offset=(5.0, -2.0), 

    def gradient_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=Gradient"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

    # u__start_color="#add8e6",  # Default Start Color (Light Blue)
    # u__end_color="#FFFFFF",    # Default End Color (Black)

    def redactedsimple_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=RedactedSimple"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]
      # u__color="#FF0000FF"

    def reversed_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=Reversed"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

    # No variables

    def flipped_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=Flipped"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]
    
    # No Variables

    def cthonic_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=Cthonic"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]
    
    # No Variables
    

    def cthonicjitter_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=CthonicJitter"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

    # No variables

    def redactedglitch_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=RedactedGlitch"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

    # u__glitchFrequency=0.5, #Time between glitch effects.
    # u__pulseDelay=1.15, #Multiplier against the glitch frequency for the second layer of glitching.
    # u__cuts= 50.0, #Number of horizontal slices made to the text.
    # u__minChaos= 6.0, # The minimum number of slices
    # u__maxChaos= 10.0, # The maximum number of slices.
    # u__jitterFrequency= 0.3,  #Time between jitters.  
    # u__jitterIntensity = 0.02, #Intensity of the jitter

    def cthonicglitch_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=CthonicGlitch"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]
    
    # u__glitchFrequency=0.5, #Time between glitch effects.
    # u__pulseDelay=1.15, #Multiplier against the glitch frequency for the second layer of glitching.
    # u__cuts= 50.0, #Number of horizontal slices made to the text.
    # u__minChaos= 6.0, # The minimum number of slices
    # u__maxChaos= 10.0, # The maximum number of slices.
    # u__jitterFrequency= 0.3,  #Time between jitters.  
    # u__jitterIntensity = 0.02, #Intensity of the jitter


    def cthonicglitchcolor_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=CthonicGlitchColor"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

    # u__glitchFrequency=0.5, #Time between glitch effects.
    # u__pulseDelay=1.15, #Multiplier against the glitch frequency for the second layer of glitching.
    # u__cuts= 50.0, #Number of horizontal slices made to the text.
    # u__minChaos= 6.0, # The minimum number of slices
    # u__maxChaos= 10.0, # The maximum number of slices.
    # u__jitterFrequency= 0.3,  #Time between jitters.  
    # u__jitterIntensity = 0.02, #Intensity of the jitter
    # u__firstColor="#880000FF",
    # u__secondColor="#000088FF",


    def static_tag(tag, argument, contents):
        return [
        (renpy.TEXT_TAG, u"shader=Static"),
    ] + contents + [
        (renpy.TEXT_TAG, u"/shader"),
    ]

    # u__intensity=0.6,
    # u__seed=0.3  

    # Tag definitions
    config.custom_text_tags["ghostwrite"] = ghostwrite_tag
    config.custom_text_tags["burningforbigtext"] = burningforbigtext_tag
    config.custom_text_tags["burningforsmalltext"] = burningforsmalltext_tag
    config.custom_text_tags["blueburnbig"] = blueburnbig_tag
    config.custom_text_tags["blueburnsmall"] = blueburnsmall_tag
    config.custom_text_tags["demo"] = adjustableburndemo_tag
    config.custom_text_tags["hollowglow"] = hollowglow_tag
    config.custom_text_tags["gradientglow"] = gradientglow_tag
    config.custom_text_tags["glow"] = glow_tag
    config.custom_text_tags["redalert"] = redalert_tag
    config.custom_text_tags["prey"] = prey_tag
    config.custom_text_tags["goldsweep"] = goldsweep_tag
    config.custom_text_tags["colorsweep"] = colorsweep_tag
    config.custom_text_tags["textshadow"] = textshadow_tag
    config.custom_text_tags["gradient"] = gradient_tag
    config.custom_text_tags["reversed"] = reversed_tag
    config.custom_text_tags["flipped"] = flipped_tag
    config.custom_text_tags["cthonic"] = cthonic_tag
    config.custom_text_tags["cthonicjitter"] = cthonicjitter_tag
    config.custom_text_tags["redactedglitch"] = redactedglitch_tag
    config.custom_text_tags["cthonicglitch"] = cthonicglitch_tag
    config.custom_text_tags["cthonicglitchcolor"] = cthonicglitchcolor_tag
    config.custom_text_tags["static"] = static_tag


