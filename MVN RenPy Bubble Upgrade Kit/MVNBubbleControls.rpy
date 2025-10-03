init python:
    import json

    bubble_presets = {}
    size_presets = {}
    location_presets= {}

    # May be removed in a future version, mostly to make sure the toolbar updates properly. 
    def rollback_callback():
        if renpy.in_rollback():
            bubble.GetCurrentDialogue()

    config.interact_callbacks.append(rollback_callback)
    
    # Grabs the presets and loads them in. 
    # These presets do not need to be left in your files once you go to ship your game.
    def load_bubble_presets():
        global bubble_presets, size_presets
        path = os.path.join(renpy.config.basedir, "game", "bubble_presets.json")
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                bubble_presets = data.get("bubble_presets", {})
                size_presets = data.get("size_presets", {})
                location_presets = data.get("location_presets", {})
        except Exception as e:
            renpy.log(f"Failed to load bubble presets: {e}")
            bubble_presets = {}
            size_presets = {}
            location_presets = {} 

    load_bubble_presets()

    def save_bubble_preset(tlid, preset_name, category):
        json_path = os.path.join(renpy.config.basedir, "game", "bubble_presets.json")

        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except:
            data = { "bubble_presets": {}, "size_presets": {} }

        if tlid not in bubble.db or "area" not in bubble.db[tlid]:
            renpy.notify(f"Cannot save preset — no area defined for {tlid}")
            return

        entry = {
            "area": bubble.db[tlid]["area"],
        }

        if "properties" in bubble.db[tlid]:
            entry["properties"] = bubble.db[tlid]["properties"]

        if category == "bubble":
            data.setdefault("bubble_presets", {})[preset_name] = entry
        elif category == "size":
            data.setdefault("size_presets", {})[preset_name] = entry
        else:
            renpy.notify("Invalid category.")
            return

        try:
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            renpy.notify(f"Preset '{preset_name}' saved to {category}_presets.")
            renpy.reload_script() # Probably overkill but sometimes reloading the presets doesn't work.
            load_bubble_presets()  # reload into memory
            
        except Exception as e:
            renpy.notify(f"Failed to save preset: {e}")
    

    def apply_bubble_size(image_tag, tlid, size_name):
        preset = size_presets.get(size_name)
        if not preset:
            renpy.notify(f"Size preset '{size_name}' not found.")
            return
        
        if tlid not in bubble.db:
            bubble.db[tlid] = {}

        current = bubble.db[tlid].get("area", [0, 0, 400, 200])
        x, y = current[0], current[1]
        w, h = preset["area"][2], preset["area"][3]
        bubble.db[tlid]["area"] = [x, y, w, h]

        if "properties" in preset:
            bubble.db[tlid]["properties"] = preset["properties"]

        renpy.rollback(checkpoints=0, force=True, greedy=True)
        renpy.notify(f"Size '{size_name}' applied to {tlid}.")

    #Originally intended to make a size preset and a location preset, but wound up only implementing full presets and size presets.
    #If there's demand for it, I can put the functionality in but it didn't feel that important at the time.
    def apply_bubble_location(image_tag, tlid, location_name):
        preset = location_presets.get(location_name)
        if not preset:
            renpy.notify(f"Size preset '{location_name}' not found.")
            return
        
        if tlid not in bubble.db:
            bubble.db[tlid] = {}

        current = bubble.db[tlid].get("area", [0, 0, 400, 200])
        x, y = current[0], current[1]
        w, h = preset["area"][2], preset["area"][3]
        bubble.db[tlid]["area"] = [x, y, w, h]

        if "properties" in preset:
            bubble.db[tlid]["properties"] = preset["properties"]

        renpy.rollback(checkpoints=0, force=True, greedy=True)
        renpy.notify(f"Size '{size_name}' applied to {tlid}.")

    def GetProperties(image_tag, tlid):
        if tlid not in bubble.db:
            return ""
        if "properties" in bubble.db[tlid]:
            return bubble.db[tlid]["properties"]
        return ""

    # Recent preset tracking
    recent_bubble_presets = []
    def track_recent_preset(preset_name):
        if preset_name in recent_bubble_presets:
            recent_bubble_presets.remove(preset_name)
        recent_bubble_presets.insert(0, preset_name)
        if len(recent_bubble_presets) > 4:
            recent_bubble_presets.pop()
    
    def get_retain_state(image_tag, tlid):
      
        if "clear_retain" not in bubble.db[tlid]:
            return False
        return bubble.db[tlid]['clear_retain']

    # The built-in toggle retain is cleaner, actually
    def apply_retain(image_tag, tlid, clear):
  
        if tlid not in bubble.db:
            bubble.db[tlid] = {}
        
        bubble.db[tlid]["clear_retain"] = clear

        renpy.rollback(checkpoints=0, force=True, greedy=True)
        

    def apply_bubble_preset(image_tag, tlid, preset_name):
        preset = bubble_presets.get(preset_name)
        if not preset:
            renpy.notify(f"Preset '{preset_name}' not found.")
            return

        if tlid not in bubble.db:
            bubble.db[tlid] = {}

        if "area" in preset:
            bubble.db[tlid]["area"] = preset["area"]

        if "properties" in preset:
            bubble.db[tlid]["properties"] = preset["properties"]

        track_recent_preset(preset_name)

        renpy.rollback(checkpoints=0, force=True, greedy=True)
        renpy.notify(f"Preset '{preset_name}' applied to {tlid}.")

    def apply_named_property(image_tag, tlid, property_name):
        if property_name not in bubble.properties:
            renpy.notify(f"Property '{property_name}' not found in bubble.properties.")
            return

        if tlid not in bubble.db:
            bubble.db[tlid] = {}

        bubble.db[tlid]["properties"] = property_name  # just store the key name

        renpy.rollback(checkpoints=0, force=True, greedy=True)

#Screen code, huzzah!            

screen MVN_bubble_editor_toolbar():
    layer config.interface_layer
    zorder 1050

    default property_dropdown_open = False
    default bubble_dropdown_open = False
    default size_dropdown_open = False

    if bubble.current_dialogue and not _menu:
        frame:
            style "empty"
            background "#000c"
            padding (6, 6)
            xfill True
            yminimum 50

            hbox:
                spacing 20
                align (0.5, 0.0)

                for image_tag, properties in bubble.GetCurrentDialogue():
                    hbox:
                        spacing 10

                        text "Character: [image_tag]" size 16 color "#fff"
                        text "ID: [bubble.current_dialogue[0][1]]" size 16 color "#aaa"
                        textbutton "Move":
                            text_size 14
                            action [bubble.SetWindowArea(image_tag, bubble.current_dialogue[0][1])]
                        textbutton "Style: [GetProperties(image_tag, bubble.current_dialogue[0][1])]":
                            text_size 14
                            action CaptureFocus("toolbar_propertyselect")

                        textbutton "Bubble Presets":
                            text_size 14
                            action CaptureFocus("bubblepresets")

                        textbutton "Size Presets":
                            text_size 14
                            action CaptureFocus("sizepresets")

                        textbutton _("Clear Bubbles: [get_retain_state(image_tag,bubble.current_dialogue[0][1])]"):
                            text_size 14
                            action bubble.ToggleClearRetain(bubble.current_dialogue[0][1])

                        textbutton "Save":
                            text_size 14
                            action ShowMenu("MVN_bubble_save_preset", tlid=bubble.current_dialogue[0][1])

        # Style dropdown
        if GetFocusRect("toolbar_propertyselect"):
            dismiss action ClearFocus("toolbar_propertyselect")
            nearrect:
                focus "toolbar_propertyselect"
                preferred_side "bottom"
                frame:
                    background "#111d"
                    padding (6, 6)
                    modal True

                    vbox:
                        spacing 4
                        for prop_name in bubble.properties:
                            textbutton prop_name:
                                action [
                                    ClearFocus("toolbar_propertyselect"),
                                    Function(apply_named_property, image_tag, bubble.current_dialogue[0][1], prop_name)
                                ]
                                text_size 14

        # Bubble preset dropdown
        if GetFocusRect("bubblepresets"):
            dismiss action ClearFocus("bubblepresets")
            nearrect:
                focus "bubblepresets"
                preferred_side "bottom"
                frame:
                    background "#111d"
                    padding (6, 6)
                    modal True

                    vbox:
                        spacing 4
                        for preset_name in bubble_presets:
                            textbutton preset_name:
                                action [
                                    ClearFocus("bubblepresets"),
                                    Function(apply_bubble_preset, image_tag, bubble.current_dialogue[0][1], preset_name)
                                ]
                                text_size 14

        # Size preset dropdown
        if GetFocusRect("sizepresets"):
            dismiss action ClearFocus("sizepresets")
            nearrect:
                focus "sizepresets"
                preferred_side "bottom"
                frame:
                    background "#111d"
                    padding (6, 6)
                    modal True

                    vbox:
                        spacing 4
                        for size_name in size_presets:
                            textbutton size_name:
                                action [
                                    ClearFocus("sizepresets"),
                                    Function(apply_bubble_size, image_tag, bubble.current_dialogue[0][1], size_name)
                                ]
                                text_size 14

# The OG editor setup.  May finish and put it in at a later date.  The tool bar with drop downs seemed slicker.
screen MVN_bubble_editor():
    layer config.interface_layer
    zorder 1050

    if bubble.current_dialogue and not _menu:
        drag:
            draggable True
            focus_mask None
            xpos 0.5
            ypos 0
            
            frame:
                style "empty"
                background "#0008"
                xpadding 10
                ypadding 10
                xmaximum 800

                vbox:
                    spacing 10
                    text "Make Visual Novels! Bubble Control Panel" size 20 color "#fff"

                    frame:
                        background "#111c"
                        xmaximum 800
                        ymaximum 600
                        padding (8, 8)
                        vpgrid:
                            cols 1
                            mousewheel True
                            scrollbars "vertical"
                            draggable True

                            vbox:
                                spacing 10
                                for image_tag, properties in bubble.GetCurrentDialogue():
                                    frame:
                                        background "#111a"
                                        xpadding 5
                                        ypadding 5
                                        xmaximum 1200

                                        vbox:
                                            hbox:
                                                spacing 4
                                                frame:
                                                    xpadding 10
                                                    ypadding 10
                                                    xmaximum 200
                                                    ymaximum 150
                                                    vbox:
                                                        
                                                        text "Character: [image_tag]" size 16 color "#fff"     
                                                        text "ID: [bubble.current_dialogue[0][1]]" size 16 color "#aaa"
                                                        textbutton "Style: [GetProperties(image_tag,bubble.current_dialogue[0][1])]":
                                                            text_size 16
                                                            action CaptureFocus("propertyselect")

                                                          
                                                        
                                                        if bubble.current_dialogue:                          
                                                            textbutton _("Clear Bubbles: [get_retain_state(image_tag,bubble.current_dialogue[0][1])]"):
                                                                action bubble.ToggleClearRetain(bubble.current_dialogue[0][1])
                                                                text_size 16
                                                        textbutton "Save as Preset":
                                                            action ShowMenu("MVN_bubble_save_preset", tlid=bubble.current_dialogue[0][1])
                                                            text_size 16
                                                            tooltip "Save this bubble as a preset (position or size)"
                                                        
                                                frame:
                                                    background "#1118"
                                                    xpadding 8
                                                    ypadding 8
                                                    vbox:
                                                        spacing 2
                                                        text "Recent Presets" size 18 color "#ccc"

                                                        if recent_bubble_presets:
                                                            for preset_name in recent_bubble_presets:
                                                                textbutton preset_name:
                                                                    action Function(apply_bubble_preset, image_tag, bubble.current_dialogue[0][1], preset_name)
                                                                    text_size 16
                                                                    tooltip f"Reapply preset: {preset_name}"
                                                        else:
                                                            text "No recent presets yet." size 16 color "#aaa"
                                                                                               
                                            hbox:
                                                spacing 40

                                                frame:
                                                    background "#2228"
                                                    xpadding 10
                                                    ypadding 10
                                                    xmaximum 200
                                                    ymaximum 150
                                                    vbox:
                                                        spacing 6
                                                        text "Bubble Presets" size 18 color "#ccc"
                                                        viewport:
                                                            mousewheel True
                                                            scrollbars "vertical"
                                                            draggable True

                                                            vbox:
                                                                spacing 4
                                                                for preset_name in bubble_presets:
                                                                    textbutton preset_name:
                                                                        action Function(apply_bubble_preset, image_tag, bubble.current_dialogue[0][1], preset_name)
                                                                        text_size 18
                                                                        tooltip f"Apply bubble preset: {preset_name}"

                                                frame:
                                                    background "#2228"
                                                    xpadding 10
                                                    ypadding 10
                                                    xmaximum 200
                                                    ymaximum 150
                                                    vbox:
                                                        spacing 6
                                                        text "Size Presets" size 18 color "#ccc"
                                                        viewport:
                                                            mousewheel True
                                                            scrollbars "vertical"
                                                            draggable True

                                                            vbox:
                                                                spacing 4
                                                                for size_name in size_presets:
                                                                    textbutton size_name:
                                                                        action Function(apply_bubble_size, image_tag, bubble.current_dialogue[0][1], size_name)
                                                                        text_size 18
                                                                        tooltip f"Apply size preset: {size_name}"
        if GetFocusRect("propertyselect"):
            dismiss action ClearFocus("propertyselect")
            nearrect:
                
                focus "propertyselect"
                preferred_side "left"

                frame:
                    background "#111d"
                    padding (6, 6)
                    

                    vbox:
                        spacing 4
                        for prop_name in bubble.properties:
                            textbutton prop_name:
                                action [
                                    ClearFocus("propertyselect"),
                                    Function(apply_named_property, image_tag, bubble.current_dialogue[0][1], prop_name)
                                ]
                                text_size 16           
                                            


screen bubble_preset_dropdown(image_tag, tlid):
    frame:
        xpadding 10
        ypadding 10
        vbox:
            for preset_name in bubble_presets:
                textbutton preset_name:
                    action [
                        Function(apply_bubble_preset, image_tag, tlid, preset_name),
                        Hide("bubble_preset_dropdown")
                    ]

# This is basically just the built in one, but I was intending to make this only move the bubble vs resizing it too.  Maybe in a future update.
screen MVN_bubble_move_picker(image_tag, tlid):
    layer config.interface_layer
    zorder 1052
    modal True

    default grid_rows = bubble.rows
    default grid_cols = bubble.cols

    frame:
        background "#000a"
        xpadding 10
        ypadding 10
        vbox:
            spacing 10
            text "Click to move the bubble (size will be preserved)" size 18 color "#fff"

            areapicker:
                cols grid_cols
                rows grid_rows
                finished Function(bubble.MoveBubblePosition, image_tag, tlid)
                add "#f004"

    key "game_menu" action Hide()

screen MVN_bubble_area_picker(image_tag, tlid):
    layer config.interface_layer
    zorder 1051
    modal True

    default grid_rows = bubble.rows
    default grid_cols = bubble.cols

    frame:
        background "#000a"
        padding (10, 10, 10, 10)
        vbox:
            text "Click to pick a bubble area" size 18 color "#fff"
            areapicker:
                cols grid_cols
                rows grid_rows
                finished bubble.SetWindowArea(image_tag, tlid).finished
                add "#f004"

    key "game_menu" action Hide()

# This thing keeps coming up as a full screen.  Not really ideal but it's fine for now. 
screen MVN_bubble_save_preset(tlid):
    modal True
    zorder 1054
    layer config.interface_layer

    default preset_name = ""
    default category = "bubble"

    frame:
        background "#000c"
        padding (60, 60, 60, 60)
        
        xalign 0.5
        yalign 0.5

        vbox:
            align (0.5, 0.5)
            spacing 45

            text "Save Current Bubble as Preset":
                xalign 0.5
                size 24
                color "#fff"

            vbox:
                spacing 10
                text "Preset Name:" color "#ccc"
                input value ScreenVariableInputValue("preset_name") length 40

            vbox:
                spacing 10
                text "Category:" color "#ccc"
                hbox:
                    spacing 20
                    textbutton "Bubble":
                        action SetScreenVariable("category", "bubble")
                        background ( "#666" if category == "bubble" else "#222" )
                        xalign 0.5
                    textbutton "Size":
                        action SetScreenVariable("category", "size")
                        background ( "#666" if category == "size" else "#222" )
                        xalign 0.5

            hbox:
                spacing 150
                xalign 0.5

                textbutton "Save":
                    action [Function(save_bubble_preset, tlid, preset_name.strip(), category), Return()]
                    sensitive If(preset_name.strip(), True, False)
                    xalign 0.5

                textbutton "Cancel":
                    action Return()
                    xalign 0.5

    key "game_menu" action Hide()



init python:
    if config.developer:
        # Commented out the OG screen, uncomment it if you want it enabled by default.
        # config.always_shown_screens.append("MVN_bubble_editor")
        config.always_shown_screens.append("MVN_bubble_editor_toolbar")
