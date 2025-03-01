

label VNShillQuiz:
    scene quizbg

label SQuestion1:
    menu:
        "How often do you talk about visual novels?"
        "Rarely, if ever.":
                $ score += 1
        "When there’s big news.":
                $ score += 2
        "At least once a week.":
                $ score += 3
        "Daily, just try to stop me!":
                $ score += 4
    

label SQuestion2:
    menu:
        "Have you had fan art made of any visual novel?"
        "No, that’s weird.":
                $ score += 1
        "Once, as a joke.":
                $ score += 2
        "Yes, and I shared it online.":
                $ score += 3
        "I became an artist so I could MAKE VISUAL NOVELs art.":
                $ score += 4
    

label SQuestion3:
    menu:
        "Have you ever contributed to a fan site for a visual novel?"
        "No.":
                $ score += 1
        "Once or twice, sure!":
                $ score += 2
        "Yes, I contribute regularly to them!":
                $ score += 3
        "I own TEN.":
                $ score += 4
    

label SQuestion4:
    menu:
        "How many times have you posted about your favorite visual novel?"
        "Never.":
                $ score += 1
        "idk like 4 or 5 times???":
                $ score += 2
        "Over a hundred.":
                $ score += 3
        "I lost track of how many times I did it today.":
                $ score += 4
    

label SQuestion5:
    menu:
        "Have you ever given someone a visual novel as a gift?"
        "No, and I am a deplorable wretch of a person with no joy in their heart":
                $ score += 1
        "Yes.":
                $ score += 2
        "Yes, several times.":
                $ score += 3
        "I Make Visual Novels as my gift to the world.":
                $ score += 4
    

label SQuestion6:
    menu:
        "How many platforms are you promoting visual novels on?"
        "None.":
            $ score += 1
        "Just one or two":
                $ score += 2
        "Most major social platforms.":
                $ score += 3
        "I am wanted for felony level littering in 7 cities for scattering visual novel flyers from sky scrapers.":
                $ score += 4
    

label SQuestion7:
    menu:
        "Have you converted any of your family members into visual novel fans?"
        "No. Also I'm a huge disappointment to everyone who ever had hope in me.":
                $ score += 1
        "I've tried, but no.":
                $ score += 2
        "Yes!":
                $ score += 3
        "Yes, and those showing resistance will break soon.":
                $ score += 4
    

label SQuestion8:
    menu:
        "Do you wear any visual novel merchandise?"
        "No??":
                $ score += 1
        "I've thought about it.":
                $ score += 2
        "Yes":
                $ score += 3
        "Did someone say visual novel merch?! Are you holding out on me?!":
                $ score += 4
    

label SQuestion9:
    menu:
        "How do you react to negative feedback about your favorite visual novel?"
        "I ignore it.":
                $ score += 1
        "I politely disagree with them.":
                $ score += 2
        "I unpolitely disagree with them.":
                $ score += 3
        "I add them to The List of People With Very Bad Opinions.":
                $ score += 4
    

label SQuestion10:
    menu:
        "What is the best way to experience visual novels?"
        "See visual novels":
                $ score += 1
        "Read visual novels":
                $ score += 2
        "Love visual novels":
                $ score += 3
        "Make Visual Novels":
                $ score += 4
    $ renpy.jump(GetSimpleLabel())


label Pathetic:
    result "How???  Do you even LIKE visual novels??" (interact=False)
    $ renpy.pause(hard=True)
    
label NeedsWork:
    result "You're not trying hard enough.  SHILL HARDER." (interact=False)
    $ renpy.pause(hard=True)

label Amazing:
    result "You are truly a visual novel shill!!!" (interact=False)
    $ renpy.pause(hard=True)
