label Literacy:

label LitQuestion1:
    menu:
        "CTC stands for..."
        "Couples Theraputic Counseling":
            pass
        "Constant Time Counting":
            pass
        "Click to Continue":
            $ score += 25
        "Central Thread Calculation":
            pass

label LitQuestion2:
    menu:
        "Where can you get help making your visual novel?"
        "DevTalk @ https://discord.gg/devtalk":
            $ score += 25
        "My grandma.  She's a writer!":
            $ score += 25
        "My dog.  He has a degree in voice acting.":
            $ score += 25
        "My friend.  They like doodling!":
            $ score += 25

label LitQuestion3:
    menu:
        "ADV is..."
        "A defunct anime and manga shop.":
            pass
        "Amazing Dynamic Vision":
            pass
        "Better than NVL":
            $ score += 10 # Partial credit
        "A convention of displaying text that occupies a third of the top or bottom of a screen.":
            $ score += 25


label LitQuestion4:
    menu:
        "The best way to make a visual novel is..."
        "Whatever way it takes to finish it.":
            $ score += 25
        "As fast as possible in a small amount of time.":
            pass
        "Slow & steady, the world can wait for my magnum opus.":
            pass
        "Not like other visual novels":
            pass
    
    result "You got [score] points!" (interact=False)
    $ renpy.pause(hard=True)