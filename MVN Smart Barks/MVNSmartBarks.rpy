init -10 python:   
    #Configuration stuff.  
    ####
    # Getting Started with Smart Barks!
    # There's a couple things you need to do to get started.  
    # 1. Go find your options.rpy and make sure you have config.has_voice set to true.  By default it's set to False.  Without it, this won't work!
    # 2. Next, all your characters need to be defined as characters with voice tags.  These are tools that'll help us later!
    # For instance: 
    # define E = Character(_("Emily"), color="#0000ff", voice_tag="EmilyVoice") #E for emily
    # define N = Character(_("Narrator Guy"), color="#ff0000", voice_tag="NarratorTag") #N for Narrator
    # 3. Populate the tables below with your character names.  That's the first bit above like "Emily" and "Narrator Guy".  This is a Character Key!
    # 4. Assign keywords you want to trigger certain voice files below for each Character Key.  These are your Phrase Keys! ("hello", "goodbye", etc are the Phrase Keys) 
    #   --The first one to match is the one selected, so avoid putting "hello world" below "hello" if you ever want 'hello world' to trigger.  
    # 5. Assign any number of voice files to each Phrase Key, inside of [], each seperated by a comma and surrounded by quotes.  These are your Voice Values!
    #   -- I like to put mine in "voice/whatever.ogg".   Make sure you're using ogg files, I'm pretty sure that's all RenPy works with but don't quote me on that.
    # 6. If for some reason you need to disable the selection of random voice files from the collection of phrases, turn UseRandomBarks to False.
    #   -- Even if you only have one file associated with the phrase, this doesn't hurt to leave it on.  If it's turned to False, it will only play the first in the collection.
    
    UseRandomBarks = True 
         
    # Oh, quick things: All of the Phrase Keys need to be lowercase.
    # The file names don't need to be, but for your sanity it's easier if they are.
    # The Character Keys need to be cased the same exact way your characters are in their definitions, otherwise they won't work.
    # If you add any more phrases to the tables below, make sure you're adding a comma between each Phrase Key-Voice Value pair.  
    #   -- e.g:         "thank you": ["voice/voice_emily_thank_you1.ogg", "voice/voice_emily_thank_you2.ogg"], #<- Added that comma on the end to extend the collection.
    # Same deal if you want to add more characters, except with the brace.  This thing before the very last one -> } 
    #   -- eg        "you have our gratitude": ["voice/voice_sarah_thank_you_formal.ogg"]
    #           }, #<-Comma there.  Now I can extend the collection of characters.

    character_voice_lines = {
    "Emily": {
        "hello": ["voice/voice_emily_hello1.ogg", "voice/voice_emily_hello2.ogg"],
        "goodbye": ["voice/voice_emily_goodbye1.ogg", "voice/voice_emily_goodbye2.ogg"],
        "how are you": ["voice/voice_emily_how_are_you1.ogg", "voice/voice_emily_how_are_you2.ogg"],
        "thank you": ["voice/voice_emily_thank_you1.ogg", "voice/voice_emily_thank_you2.ogg"]
    },
    "John": { # John can say 'sayonara' whenever he says 'Goodbye', but he'll only say sayonara if his line actually says 'sayonara'
        "hello": ["voice/voice_john_hello1.ogg", "voice/voice_john_hello2.ogg"],
        "goodbye": ["voice/voice_john_goodbye1.ogg", "voice/voice_john_sayonara.ogg"],
        "sayonara": ["voice/voice_john_sayonara.ogg"], 
        "how are you": ["voice/voice_john_how_are_you1.ogg", "voice/voice_john_how_are_you2.ogg"],
        "thank you": ["voice/voice_john_thank_you1.ogg", "voice/voice_john_thank_you2.ogg"]
    },
    "Sarah": { #Sarah is a minor character, so she only has one variation of her normal lines and that's fine.
        "welcome": ["voice/voice/voice_sarah_welcome.ogg"],
        "goodbye": ["voice/voice_sarah_until_next_time.ogg"],
        "how can i help": ["voice/voice_sarah_how_can_i_help.ogg"],
        "thanks": ["voice/voice_sarah_thank_you_informal.ogg"],
        "you have our gratitude": ["voice/voice_sarah_thank_you_formal.ogg"]
    }
    }

 
   
