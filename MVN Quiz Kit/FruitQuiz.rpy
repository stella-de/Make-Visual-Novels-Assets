
label FruitGirlQuiz:
    scene quizbg
    # I'm lazy.
    show title at top:
        xanchor 0.5
        yanchor 0.15
    # You don't need to do these next 3 things, but I did.
    "" (interact=False)
    pause 0.1
    jump Question1

    # Stylistic choice: I added a super small pause to them to help with the feel of the quiz, but they are not strictly required.
    # I also opted to label all of the questions, though I don't use the labels to navigate, it's useful for organization.

label Question1:
    menu:
        "Finish this sentence: Eat "
        "the rich!":
            $ quizValues["Plum"] += 1
            pause 0.1
        "up, yum yum!":
            $ quizValues["Cherry"] += 1
            pause 0.1
        "me!":
            $ quizValues["Lime"] += 1
            pause 0.1
        "that horse!":
            $ quizValues["Starfruit"] += 1
            pause 0.1
        "it and weep!":
            $ quizValues["Lemon"] += 1
            pause 0.1

label Question2:        
    menu:
        "What is your ideal day?"
        "A day that starts at 3:00 PM.":
            $ quizValues["Lime"] += 1
            pause 0.1
        "A day hanging out with my friends!":
            $ quizValues["Cherry"] += 1
            pause 0.1
        "A day hanging out with my friends, but I'll pretend not to like it.":
            $ quizValues["Lemon"] += 1
            pause 0.1
        "A day that ends with everything checked off.":
            $ quizValues["Starfruit"] += 1
            pause 0.1
        "A day where nothing goes wrong.":
            $ quizValues["Plum"] += 1
            pause 0.1
    
label Question3:    
    menu:
        "In the story of the world, what is your role?"
        "The Only Sane Person":
            $ quizValues["Lime"] += 1
            pause 0.1
        "The Villain":
            $ quizValues["Lemon"] += 1
            pause 0.1
        "The Hero":
            $ quizValues["Plum"] += 1
            pause 0.1
        "The Comic Relief":
            $ quizValues["Cherry"] += 1
            pause 0.1
        "The Sidekick": 
            $ quizValues["Starfruit"] += 1
            pause 0.1
    
label Question4:
    menu:
        "Which mythical creature would you rather be?"
        "A Phoenix, Burning Bright":
            $ quizValues["Starfruit"] += 1
            pause 0.1
        "A Dragon, Fierce and Mighty":
            $ quizValues["Lime"] += 1
            pause 0.1
        "A Pixie, Clever and Swift":
            $ quizValues["Lemon"] += 1
            pause 0.1
        "A Unicorn, Mysterious and Majestic":
            $ quizValues["Cherry"] += 1
            pause 0.1
        "A Merperson, In the Calm Blue": 
            $ quizValues["Plum"] += 1
            pause 0.1
    
    # Quiz Tip:
    # There's no reason you can't adjust multiple values on an answer, and there's nothing saying that all of your results need to have equal distributions.
    # Obviously it will make reaching some results more challenging, but that could be part of it for quiz takers.
    # There are 20 Plum points, 19 Cherry points, 18 Lime and Lemon points.
    # My gag/self insert result 'Starfruit', only has 14 points out of 15 questions

label Question5:
    menu:
        "Movie time!  What are you watching?"
        "Something with a lot of action!":
            $ quizValues["Lime"] += 1
            $ quizValues["Cherry"] += 1
            pause 0.1
        "Something sad and thoughtful.":
            $ quizValues["Lime"] += 1
            $ quizValues["Plum"] += 1
            pause 0.1
        "Something scary!":
            $ quizValues["Lemon"] += 1
            $ quizValues["Plum"] += 1
            pause 0.1
        "Something funny!":
            $ quizValues["Starfruit"] += 1
            $ quizValues["Cherry"] += 1
            $ quizValues["Plum"] += 1
            pause 0.1
        "Something weird!":
            $ quizValues["Lemon"] += 1
            $ quizValues["Cherry"] += 1
            pause 0.1
       
label Question6:
    menu:
        "Pack your bags, you're going on a vacation!  Where are you going?"
        "A cozy cabin in the mountains.":
            $ quizValues["Plum"] += 1
            $ quizValues["Cherry"] += 1
            pause 0.1
        "A sunny beach!":
            $ quizValues["Lime"] += 1
            $ quizValues["Cherry"] += 1
            pause 0.1
        "A big city!":
            $ quizValues["Lime"] += 1
            $ quizValues["Lemon"] += 1
            pause 0.1
        "Somewhere I can work!":
            $ quizValues["Starfruit"] += 1
            $ quizValues["Lemon"] += 1
            $ quizValues["Plum"] += 1
            pause 0.1
        "Somewhere with a lot to do!":
            $ quizValues["Lime"] += 1
            $ quizValues["Plum"] += 1
            pause 0.1

    # And there's nothing saying you can't give one result multiple things in one question.  Entirely up to you how to do it.
label Question7:
    menu:
        "What do your friends say is your best quality?"
        "My patience and understanding.":
            $ quizValues["Lime"] += 1
            pause 0.1
        "My dedication and drive.":
            $ quizValues["Plum"] += 1
            pause 0.1
        "My creativity and imagination!":
            $ quizValues["Cherry"] += 1
            pause 0.1
        "My kindness and compassion!":
            $ quizValues["Cherry"] += 1
            pause 0.1
        "...":
            $ quizValues["Starfruit"] += 1
            $ quizValues["Lemon"] += 1
            pause 0.1
     
label Question8:
    menu:
        "What do your friends say is your worst quality?"
        "My cowardice.":
            $ quizValues["Plum"] += 1
            pause 0.1
        "My laziness.":
            $ quizValues["Lime"] += 1
            pause 0.1
        "My intelligence.":
            $ quizValues["Cherry"] += 1
            pause 0.1
        "My pettiness.":
            $ quizValues["Lemon"] += 1
            pause 0.1
        "My competitiveness.":
            $ quizValues["Starfruit"] += 1
            $ quizValues["Lemon"] += 1
            pause 0.1

label Question9:
    menu:
        "What's your biggest pet peeve?"
        "Public displays of affection.":
            $ quizValues["Lemon"] += 1
            pause 0.1
        "Loud chewing noises.":
            $ quizValues["Plum"] += 1
            pause 0.1
        "Unnecessary drama.":
            $ quizValues["Lime"] += 1
            pause 0.1
        "Bad puns.":
            $ quizValues["Starfruit"] += 1
            pause 0.1
        "Overly serious attitudes.":
            $ quizValues["Cherry"] += 1
            pause 0.1

label Question10:
    menu:
        "What's your guilty pleasure?"
        "Staying up way too late.":
            $ quizValues["Lime"] += 1
            pause 0.1
        "Binging reality TV shows.":
            $ quizValues["Cherry"] += 1
            pause 0.1
        "Eating snacks in bed.":
            $ quizValues["Plum"] += 1
            pause 0.1
        "Online shopping sprees.":
            $ quizValues["Lemon"] += 1
            pause 0.1
        "Excessively REDACTED literature.":
            $ quizValues["Starfruit"] += 1
            pause 0.1

label Question11:
    menu:
        "What's your special power?"
        "Shapeshifting!":
            $ quizValues["Starfruit"] += 1
            pause 0.1
        "Super speed!":
            $ quizValues["Lime"] += 1
            pause 0.1
        "Invisibility!":
            $ quizValues["Plum"] += 1
            pause 0.1
        "Mind control!":
            $ quizValues["Lemon"] += 1
            pause 0.1
        "Summoning cute creatures!":
            $ quizValues["Cherry"] += 1
            pause 0.1

label Question12:
    menu:
        "Which food speaks to your soul?"
        "Something sweet and indulgent, like cake!":
            $ quizValues["Cherry"] += 1
            $ quizValues["Starfruit"] += 1
            pause 0.1
        "Something fresh and zesty, like a salad!":
            $ quizValues["Lime"] += 1
            pause 0.1
        "Something hearty and comforting, like soup!":
            $ quizValues["Plum"] += 1
            pause 0.1
        "Something unique and surprising, like sushi!":
            $ quizValues["Lemon"] += 1
            pause 0.1
        "Something bold and spicy, like tacos!":
            $ quizValues["Plum"] += 1
            pause 0.1
            

label Question13:
    menu:
        "If you were a season, which one would want to be?"
        "Spring, full of hope and rebirth.":
            $ quizValues["Cherry"] += 1
            pause 0.1
        "Summer, full of passion and heat.":
            $ quizValues["Starfruit"] += 1
            pause 0.1
        "Autumn, calm and introspective.":
            $ quizValues["Plum"] += 1
            $ quizValues["Lime"] += 1
            pause 0.1
        "Winter, cool and mysterious.":
            $ quizValues["Lemon"] += 1
            pause 0.1
        
label Question14:
    menu:
        "What’s your approach to solving a problem?"
        "Charge headfirst and figure it out as I go.":
            $ quizValues["Starfruit"] += 1
            pause 0.1
        "Think it through carefully before acting.":
            $ quizValues["Plum"] += 1
            pause 0.1
        "Ask for advice or brainstorm with others.":
            $ quizValues["Cherry"] += 1
            pause 0.1
        "Analyze every possible outcome.":
            $ quizValues["Lemon"] += 1   
            pause 0.1
        "Wait for inspiration to strike!":
            $ quizValues["Lime"] += 1
            pause 0.1

label Question15:
    menu:
        "What's your favorite way to relax?"
        "Getting lost in a good book.":
            $ quizValues["Plum"] += 1
        "Playing video games with friends.":
            $ quizValues["Cherry"] += 1
        "Taking a long nap.":
            $ quizValues["Lime"] += 1
        "Daydreaming about my future.":
            $ quizValues["Lemon"] += 1
    
    # This line is required at the end of your quiz to determine the result.
    # This will go through quizValues and find which one has the most points, 
    # or the 1st one in the list should there be a tie for the highest and
    # then jumps to the name of the result as a label.
    hide title
    $ renpy.jump(GetResultLabel())
    
label Lemon:
    scene lemonresult
    result "You're Lemon!\n\n{size=28}Passionate, proud, and ambitious.  Some people may write you as the villain in their story, but you believe in something better and you dream big.\n\n{b}Never stop believing.{/b}" (interact=False)
    $ renpy.pause(hard=True)

label Cherry:
    scene cherryresult
    result "You're Cherry!\n\n{size=28}Cheerful, bright and carefree.  You love to make others as happy as you are.  Your nature may make others see you as dim, but your sense of humor betrays your true wit.\n\n{b}Laugh on.{/b}" (interact=False)
    $ renpy.pause(hard=True)

label Lime:
    scene limeresult
    result "You're Lime!\n\n{size=28}Mature, refined, and often the only sane person in the room. Your patience is a virtue, but also a double edged sword.  Underneath your laziness, a great power waits to be awakened from its slumber and change everything.\n\n{b}It's time to wake up.{/b}" (interact=False)
    $ renpy.pause(hard=True)

label Plum:
    scene plumresult 
    result "You're Plum!\n\n{size=28}Thoughtful, active, and determined. You're always thinking about what's next. You're doing it now, aren't you? Some call you a workaholic, but you find serenity in your your effort.\n{b}Keep up the grind.{/b}" (interact=False)
    $ renpy.pause(hard=True)
    
label Starfruit:
    scene starresult
    result "You're Starfruit!\n{size=28}Oh, wow, this is embarassing.  Apparently you picked enough of my own answers that you got me.  Anyway, you're probably smoking hot, awesome, and just the best kind of person.  Like me!\n{b}Weird, right?{/b}" (interact=False)
    $ renpy.pause(hard=True)


    # We use escape characters to add spaces and just stylize the text using the inline style options
    # \n gives you a line break, useful for spacing out the result text into headers/bodies.
    # In the original gui/screens for the demonstration, the text size was set to 40.
    # I opted not to include my gui and screens files because I severely butchered it 
    # and it'd be better if you started fresh.

    # Tom says not to use RenPy.pause, but who does Tom think he is? The creator of REN'PY? Hah!
    # Anyway, we pause and leave them on a screen to either start over(jump to start) or go back (rollback), or they can
    # screen shot and show all their friends which fruit girl they are.


return
