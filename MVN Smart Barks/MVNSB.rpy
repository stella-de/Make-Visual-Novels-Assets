

init -9 python:
    import re
    import random
    

    def Nothing(who, what, *args, **kwargs):
        return #does nothing, wow!

    pe = False
    def SB_say(who, what, *args, **kwargs):
        global pe
        global UseRandomBarks
        name = None
        if who is None:
            return renpy.store.say(who, what, *args, **kwargs)
        if isinstance(who, str):
            return renpy.store.say(who, what, *args, **kwargs)
        if isinstance(who, _Extend):
            pe = True
            name = renpy.last_say().who.name
            tag =  renpy.last_say().who.voice_tag
            what_lower = what.replace(renpy.last_say().what, '').lower()
            #renpy.store.say("Test", what.replace(last_say_info.what, ''))
        else:
            name = who.name
            tag = who.voice_tag
            if pe:
                what_lower = what.replace(renpy.last_say().what, '').lower()
                pe = False
            else:
                what_lower = what.lower()
        if name in character_voice_lines:
            voice_lines = character_voice_lines[name]
            pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, voice_lines.keys())) + r')\b')
            match = pattern.search(what_lower)
            if match:
                matched_phrase = match.group(0)
                voice_line_choices = voice_lines.get(matched_phrase)              
                if voice_line_choices:
                    chosen_voice_line = random.choice(voice_line_choices) if UseRandomBarks else voice_line_choices[0]
                    voice(chosen_voice_line, tag=tag)
                    return who(what, *args, **kwargs)  
        return who(what, *args, **kwargs)
        
    renpy.say = SB_say