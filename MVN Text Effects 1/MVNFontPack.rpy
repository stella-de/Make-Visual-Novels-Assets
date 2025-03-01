init python:
     config.underlay.append(renpy.Keymap(fontgallery = Show("font_showcase")))
     config.keymap["fontgallery"] = ['alt_K_f']

init python:
    import os

    def toggle_font_gallery():
        if renpy.get_screen("font_showcase",  None):
            renpy.hide_screen("font_showcase")
        else:
            renpy.show_screen("font_showcase")
    
    def get_registered_shaders():
        if hasattr(renpy.config, "textshaders"):
            shaders = list(renpy.config.textshaders.keys())
        else:
            shaders = []
        return shaders if shaders else ["none"]  

    text_shader_list = get_registered_shaders()  # Get all available shaders 

    def get_fonts():
        font_directory = os.path.join(config.gamedir, "fonts")
        font_list = []      
        if not os.path.exists(font_directory):
            return font_list
        for font_family in sorted(os.listdir(font_directory)):
            font_family_path = os.path.join(font_directory, font_family)
            if os.path.isdir(font_family_path):
                styles = []
                for filename in sorted(os.listdir(font_family_path)):
                    if filename.endswith((".ttf", ".otf")):
                        styles.append({"name": filename, "path": f"fonts/{font_family}/{filename}"})
                if styles:
                    font_list.append({"family": font_family, "styles": styles})

        return font_list

    # Dynamically generate font list at startup
    font_list = get_fonts()


default persistent.shader_index = 0
default persistent.font_family_index = 0
default persistent.font_style_index = 0

screen font_showcase():
    default current_family = font_list[persistent.font_family_index]
    default current_style = current_family["styles"][persistent.font_style_index]
    default current_shader = text_shader_list[persistent.shader_index]  # Get current shader

    frame:
        xalign 0.5
        yalign 0.1  # Keep the text at the upper part
        background "#222"
        padding (30, 30)
        xsize 800
        ysize 400  # Reduce height slightly to fit everything

        vbox:
            spacing 20
            xalign 0.5
            yalign 0.0

            text f"{current_family['family']} - {current_style['name']}":
                font current_style["path"]
                size 30
                color "#FFFFFF"
                bold True
                xalign 0.5

            text ("The quick brown fox jumps over the lazy dog." if current_shader == "none" 
                  else f"{{shader={current_shader}}}You should\nMake Visual Novels!{{/shader}}"):
                font current_style["path"]
                size 50
                color "#F8F8F8"
                xalign 0.5

            text f"Shader: {{shader={current_shader}}}{current_shader}{{/shader}}({current_shader})":
                size 20
                color "#BBBBBB"
                xalign 0.5

    # Fixed-position button container at the bottom
    frame:
        xalign 0.5
        yalign 1.0  # Ensures the frame stays at the bottom
        xsize 800
        background "#333"
        padding (10, 10)

        vbox:
            spacing 10
            xalign 0.5

            hbox:
                spacing 20
                xalign 0.5

                textbutton "Previous Style":
                    action [
                        SetVariable("persistent.font_style_index", (persistent.font_style_index - 1) % len(current_family["styles"])),
                        ShowMenu("font_showcase")  # Refresh screen
                    ] style "font_gallery_button"
                    xsize 200

                textbutton "Next Style":
                    action [
                        SetVariable("persistent.font_style_index", (persistent.font_style_index + 1) % len(current_family["styles"])),
                        ShowMenu("font_showcase")
                    ] style "font_gallery_button"
                    xsize 200

            hbox:
                spacing 20
                xalign 0.5

                textbutton "Previous Font":
                    action [
                        SetVariable("persistent.font_family_index", (persistent.font_family_index - 1) % len(font_list)),
                        SetVariable("persistent.font_style_index", 0),
                        ShowMenu("font_showcase")
                    ] style "font_gallery_button"
                    xsize 200

                textbutton "Next Font":
                    action [
                        SetVariable("persistent.font_family_index", (persistent.font_family_index + 1) % len(font_list)),
                        SetVariable("persistent.font_style_index", 0),
                        ShowMenu("font_showcase")
                    ] style "font_gallery_button"
                    xsize 200

            hbox:
                spacing 20
                xalign 0.5

                textbutton "Previous Shader":
                    action [
                        SetVariable("persistent.shader_index", (persistent.shader_index - 1) % len(text_shader_list)),
                        ShowMenu("font_showcase")  # Refresh screen
                    ] style "font_gallery_button"
                    xsize 200

                textbutton "Next Shader":
                    action [
                        SetVariable("persistent.shader_index", (persistent.shader_index + 1) % len(text_shader_list)),
                        ShowMenu("font_showcase")
                    ] style "font_gallery_button"
                    xsize 200

            textbutton "Close": 
                action[
                    Return()
                ]
                xsize 200
                xalign 0.5
                style "font_gallery_button"

style font_gallery_button:
    hover_background "#666"
    padding (10, 5)
    xalign 0.5
