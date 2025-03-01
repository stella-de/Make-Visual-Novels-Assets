#Camera transforms!
#Camera Documentation
# Premade Shots:

# Pedestal Shot
# A slow camera movement that starts below and moves upwards.
# Great for character introductions or dramatic entrances!

#EXAMPLE
# camera at shot_pedestal:
#   xpos 0.35

# Establish Shot 

# shot_establish:




transform shot_pedestal:
    perspective True
    zpos -450 + pedestal_zoffset
    ypos 0.10 + pedestal_start_yoffset
    linear pedestal_duration ypos -0.10 + pedestal_end_yoffset

transform shot_establish:
    perspective True
    zpos -450 + establish_zoffset
    xpos -0.25 + establish_start_xoffset
    linear establish_duration xpos 0.25 + establish_end_xoffset

# transform dutch:
#   rotate 45
# WHY TOM PLEASE HELP

transform zoom_origin:
    perspective True
    parallel:
        ease default_zoom_time zpos 0
    parallel:
        ease default_zoom_time xpos 0
    parallel:
        ease default_zoom_time ypos 0

transform origin:
    perspective True
    zpos 0
    xpos 0
    ypos 0

transform zoom_front_right:
    perspective True
    parallel:
        ease default_zoom_time zpos -300 + zoom_front_zoffset
    parallel:
        ease default_zoom_time xpos 0.15 + zoom_front_xoffset
    parallel:
        ease default_zoom_time ypos 0.05 + zoom_front_yoffset

transform zoom_front_left:
    perspective True
    parallel:
        ease default_zoom_time zpos -300 + zoom_front_zoffset
    parallel:
        ease default_zoom_time xpos -0.15 - zoom_front_xoffset
    parallel:
        ease default_zoom_time ypos 0.05 + zoom_front_yoffset

transform zoom_front_center:
    perspective True
    parallel:
        ease default_zoom_time zpos -300 + zoom_front_zoffset
    parallel:
        ease default_zoom_time xpos 0.0
    parallel:
        ease default_zoom_time ypos 0.05 + zoom_front_yoffset

transform zoom_back_right:
    perspective True
    parallel:
        ease default_zoom_time zpos -500 + zoom_back_zoffset
    parallel:
        ease default_zoom_time xpos 0.25 + zoom_back_xoffset
    parallel:
        ease default_zoom_time ypos -0.10 + zoom_back_yoffset

transform zoom_back_left:
    perspective True
    parallel:
        ease default_zoom_time zpos -500 + zoom_back_zoffset
    parallel:
        ease default_zoom_time xpos -0.25 - zoom_back_xoffset
    parallel:
        ease default_zoom_time ypos -0.10 + zoom_back_yoffset

transform zoom_back_center:
    perspective True
    parallel:
        ease default_zoom_time zpos -500 + zoom_back_zoffset
    parallel:
        ease default_zoom_time xpos 0.0
    parallel:
        ease default_zoom_time ypos -0.10 + zoom_back_yoffset

transform zoom_right:
    perspective True
    parallel:
        ease default_zoom_time zpos -450 + zoom_mid_zoffset
    parallel:
        ease default_zoom_time xpos 0.25 + zoom_mid_xoffset
    parallel:
        ease default_zoom_time ypos -0.10 + zoom_mid_yoffset

transform zoom_left:
    perspective True
    parallel:
        ease default_zoom_time zpos -450 + zoom_mid_zoffset
    parallel:
        ease default_zoom_time xpos -0.25 - zoom_mid_xoffset
    parallel:
        ease default_zoom_time ypos -0.10 + zoom_mid_yoffset
    
transform zoom_center:
    perspective True
    parallel:
        ease default_zoom_time zpos -450 + zoom_mid_zoffset
    parallel:
        ease default_zoom_time xpos 0.0
    parallel:
        ease default_zoom_time ypos -0.10 + zoom_mid_yoffset
