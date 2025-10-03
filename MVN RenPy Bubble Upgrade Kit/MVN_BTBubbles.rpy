init python:
    #The continues set the who color to transparent to suppress them.  It's a neat trick, right?
    bubble.properties.update({
        "continue_left": {
            "window_background": Frame('gui/bubble_c_left.png', 55, 55, 55, 95),
            "window_bottom_padding": 27,
            "who_color": "#0000"
        },
        "continue_right": {
            "window_background": Frame("gui/bubble_c_right.png", 55, 55, 55, 95),
            "window_bottom_padding": 27,
            "who_color": "#0000"
        },
        "continue_up": {
            "window_background": Frame("gui/bubble_c_up.png", 55, 55, 55, 95),
            "window_bottom_padding": 27,
            "who_color": "#0000"
        },
        "continue_down": {
            "window_background": Frame("gui/bubble_c_down.png", 55, 55, 55, 95),
            "window_bottom_padding": 27,
            "who_color": "#0000"
        },
        "ping": {
            "window_background": Frame("gui/bubble_ping.png",0,0,0,0),
            "window_bottom_padding": 27,
        },
        "page":{
            "window_background" : bubble.thoughtframe,
            "who_color": "#0000",
            "what_text_align": 0.0,
            "what_align": (0.0, 0.0),
            "window_top_padding": 18,
            "window_bottom_padding": 27,
        }
    })
