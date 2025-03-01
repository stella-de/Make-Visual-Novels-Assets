init -9 python:
    
    ####
    #   Getting Started - Easy Version
    #       Step 1:  Make some labels seperating different parts of your visual novel.  Cool names mandatory.
    #       Step 2:  Place your backgrounds in a folder somewhere in your project.  Ideally /gui/
    #       Step 3:  Pair the labels you wrote in step 1 to the paths in step 2 in the table below.
    #       Step 4:  In your main menu definition (usually in screens.rpy) you need to add this line and remove other backgrounds you might have there.
    #                   add smart_background() 
    #       Step 5:  Use the jump command in your scripts to switch to different sections of your visual novel.  If you jump to one of the labels you define below
    #               the menu will change itself without you needing to do anything else.
    #       Step 6: Follow, like, subscribe, go to https://patreon.com/vndevtalk and donate (jk you're done that's it)
    #        
    ######

    #   Leave 'Title' in this list of definitions and leave gui/main_menu.png in your project.  
    #   If you need to reset back to it, use reset_title() in your script or in the console.

    title_backgrounds = {
        "Title": "gui/main_menu.png",
        "ExampleLabel": "gui/ExampleFile.png",
        "Chapter1": "gui/bg_chapter1.png",
        "Chapter2": "gui/bg_chapter2.png",
        "Chapter3": "gui/bg_chapter3.png",
    }
    

    ####
    #   Menu Dictionary - Intermediate/Advanced
    #   You can use an entirely different menu screen, not just a background, with the following dictionary.
    #   There's two major differences in setting this one up.
    #   1)In step 2, you make screens including whatever you want to put there.
    #   2)In step 4, use this instead of add smart_background (though you can use that in the new screens you make if you want.)
    #       $ renpy.use_screen(smart_title())
    #   3)In step 6 you actually do it (no more clowning around fork it over)
    #   
    #   Use this in combination with your awesome graphic design skills to give your players something fun to see when they come back.
    ######
    
    #   These example screens are defined in MVNSTSExampleScreens.rpy just in case you are using these labels already. 
    #   If you add a label here, you need to also add that label to title_backgrounds, even if you wind up not using the smart background feature.
    
    title_menus = {
        "Title": "start_title",
        "ExampleLabel": "example_screen",
        "Chapter 1": "chapter_1_title",
        "Chapter 2": "chapter_2_title",
        "Chapter 3": "chapter_3_title",
    }


    #####
    #   Functions - For nerds
    #   smart_background() - Defined in MVNSTSOR.rpy
    #       Gets the background definition as defined above based on the last lowest label in the above list.
    #       Defaults to gui/main_menu.png if the player hasn't sceen any of the defined labels.
    #       Use this whenever you want to get the graphic used on the title screen:
    #           add smart_background() 
    #       
    #       You can also type smart_background() in the console to display path of the active background.

    #   smart_title() - Defined in MVNSTSOR.rpy
    #       Gets the menu screen name as defined below based on the last lowest label in the below list.
    #       Use this with show screen in your main menu definition to load entire pre-defined screens when your main menu loads:
    #           $ renpy.use_screen(smart_title())
    #       
    #       You can also type smart_title() in the console to display the name of the active screen.
    
    #   reset_title() - Defined in MVNSTSOR.rpy
    #       Resets the game's title menu state back to the 'Title' definition.
    #       You can put this in scripts, as actions in response to a button being pressed, or just use it in the console to test your setup.
    

    ####
    #   Obligatory Visual Novel Propaganda 
    #       You should make visual novels.  They're cool.
    #       Come check out https://discord.gg/devtalk, the community we visual novel developers run.
    #       Oh also I'm planning on making a dynamic GUI pack as well so stay tuned.
    ######
   

   



