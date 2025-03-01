###
# You're in the right place!  This contains the configuration you need to go through.



###############################################
# SECTION 1: VALUES AND RESULTS
# This kit works in two premade ways.  In either case, the Result1-6 can be renamed to whatever you want to use as long as you have labels
# for them set up in your script.rpy. The people taking your quiz can't see these names, so whatever you want to 
# use is fine as long as you understand it.


########### Method A: Multiple buckets, highest one wins. (Good for character quizes)
# You give points towards a specific result and whichever has the most points is the result.
## For this method, you need to set up startingValues and quizValues below  startingValues is the 'default' values when your
## quiz takers start over, so keep it 0'd out for your sanity.  The names you give these values are important and case sensitive.


# TO ADD/SUBTRACT: 
# $ quizValues["Result1"] += 1 to add 1 or $ quizValues["Result1"] -= 1 from the value named 'Result1'

# TO CALCULATE THE RIGHT RESULT AT THE END OF THE QUIZ:
# $ renpy.jump(GetResultLabel()) 

default startingValues = { "Result1":0, "Result2":0, "Result3":0, "Result4":0, "Result5":0, "Result6":0 }
default quizValues = { "Result1":0, "Result2":0, "Result3":0, "Result4":0, "Result5":0, "Result6":0 }

############ Method B: One bucket, highest result the bucket beats wins. (Good for purity/power level quizes)
# You track a single value(score) and the result is determined by checking the below value against this table(simpleValues), also below.
## The text in each of these is the label it will take your quiz takers to at the end and 
## the number in front of it is the score they need to MEET or BEAT to see it.

## TO ADD/SUBTRACT:
# $ score += 1 to add 1 or $ score -= 1 to subtract from the score.

## TO CALCULATE THE RIGHT RESULT AT THE END OF THE QUIZ:
# $ renpy.jump(GetSimpleLabel()) 

default score = 0
default simpleValues = { 0:"Result1", 2:"Result2", 5:"Result3", 7:"Result4", 9:"Result5", 10:"Result6" }


###############################################
# SECTION 2: Disabling shortcuts
# We use an on-screen rollback button which helps keep the feel of online quizes, and disabling accidental rollbacks
# using scroll/pageup will prevent goofy UX issues.  We also want to disable the game menu.

## Note:
# Some of the key definitions changed in Ren'PY 8.3.
# The fastest way to find the right ones for your version is to look at your renpy\common\00keymap.rpy file
# You'll specifically want the ones assigned to 'rollback' and 'game_menu'
# 


#init python:
    #    config.keymap['rollback'].remove('any_K_PAGEUP') # Uncomment this line if you're on 8.2 or earlier.
    #    config.keymap['rollback'].remove('any_KP_PAGEUP') # Uncomment this line if you're on 8.2 or earlier.
    #    config.keymap['rollback'].remove('anyrepeat_K_PAGEUP') #Uncomment this line if you're on 8.3 or later.
    #    config.keymap['rollback'].remove('anyrepeat_KP_PAGEUP') #Uncomment this line if you're on 8.3 or later.
    #    config.keymap['rollback'].remove('K_AC_BACK')
    #    config.keymap['rollback'].remove('mousedown_4')       

    #   config.keymap['game_menu'].remove('K_ESCAPE')
    #   config.keymap['game_menu'].remove('K_MENU')
    #   config.keymap['game_menu'].remove('K_PAUSE')
    #   config.keymap['game_menu'].remove('mouseup_3')

###############################################
# SECTION 3: STYLING
#   This is where you change the appearance of the basic controls.


# The Dialogue Box
# You're going to want to stylize/adjust the appearance of the following styles in screens.rpy
# window, namebox, say_label, say_dialogue
# Do this to your preference.  I've included what I used in the demonstration, but it's wise to make your own.

#style window:
#    xfill True
#    yalign  0.15
#    xpos 0.02
#    background Image("gui/question.png")

#style say_dialogue:
#    properties gui.text_properties("dialogue")
#    xsize 600 
#    xfill True   
#    xalign gui.dialogue_xpos
#    xpos 0.45
#    ypos 0.12

# The Choice Menu
#   This adds the back and start over buttons to your quiz.
#   This will overwrite our screens.rpy definition of your choice menu.  Comment it out or delete this if you want to use screens.rpy instead.

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            frame:
                textbutton i.caption action i.action
    use back_button
    use SO_button


# The Back and Start Over Buttons
#   These are set up to use the same style as your choice buttons, so customize your choice styles in screens.rpy to your liking.

screen back_button():
    frame:
        background "#FFFFFF" 
        xalign 0.05
        yalign 0.975
        frame:
            padding (5,5)
            textbutton "Go Back" action Rollback():
                xysize(150,100)
                style_prefix "choice"
                
screen SO_button():
    # Position the button in the bottom-left corner
    frame:
        background "#FFFFFF" 
        xalign 0.95
        yalign 0.975
        frame:
            padding (5,5)
            textbutton "Start Over" action Function(StartOver):
                xysize(150,100)
                style_prefix "choice"                
                
        

style back_button_text:
    xalign 0.5 yalign 0.4
    size 28
    font "DejaVuSans.ttf"  # Replace with your font file


# The Results screen
#   We define result as a character so we can give it different formatting easily.
#   Feel free to customize to your liking.

define result = Character(None, window_style="results_window")
init python:
    # Define a custom style for the Results box
    style.results_window = Style(style.window)
    style.results_window.xalign = 0.5  # Center horizontally
    style.results_window.yalign = 0.05  # Start at the top of the screen
    style.results_window.xsize = 0.8   # Take up 80% of the screen width
    style.results_window.ysize = 0.2   # Take up 80% of the screen height
    style.results_window.background = "#FFFFFF00" 
    style.results_window.padding = (20, 20, 20, 20)  # Add padding for text