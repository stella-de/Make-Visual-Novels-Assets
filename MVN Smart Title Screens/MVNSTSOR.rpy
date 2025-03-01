
init -10 python:
    
    # This is where we hijack the built-in jump command to make the rest of the stuff work.
    # I would recommend not messing with this unless you know what you're doing.
    def on_label_reached(label, reached_via_jump):
        config.log = "mmb.txt"
        renpy.log(label)
        if label in title_backgrounds:
            current_label = persistent.last_valid_label if hasattr(persistent, 'last_valid_label') else None       
            if current_label is None or list(title_backgrounds).index(label) > list(title_backgrounds).index(current_label):
                persistent.last_valid_label = label
                renpy.save_persistent()
            persistent.smart_background = title_backgrounds[persistent.last_valid_label]  
            persistent.smart_title = title_menus[persistent.last_valid_label]  
    
    config.label_callbacks.append(on_label_reached)

    def reset_title():
            persistent.last_valid_label = "Title"
            return "Title"

    def smart_background():
        if hasattr(persistent, 'last_valid_label') and persistent.last_valid_label in title_backgrounds:
            return title_backgrounds[persistent.last_valid_label]   
        return "gui/main_menu.png"
    
    def smart_title(): 
        if hasattr(persistent, 'last_valid_label') and persistent.last_valid_label in title_backgrounds:
            return title_menus[persistent.last_valid_label]   
        return "start_title"
    

    #For the jump command in the console, mainly for testing
    default_jump = renpy.jump
    def MVNLabel_jump(label, *args, **kwargs):
        config.log = "mmb.txt"
        print("Jump called!")
        print(label)
        renpy.log(label)
        renpy.log(persistent.last_valid_label)
        if label in title_backgrounds:
            print(current_label)
            current_label = persistent.last_valid_label if hasattr(persistent, 'last_valid_label') else None         
            print(current_label)
            if current_label is None or list(title_backgrounds).index(label) > list(title_backgrounds).index(current_label):
                print(current_label)
                persistent.last_valid_label = label
                print(label)
                renpy.save_persistent()
        return default_jump(label, *args, **kwargs)


