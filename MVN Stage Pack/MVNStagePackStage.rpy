# Math settings, don't recommend setting them so I stuffed them in this document instead of othe others.
# Testing at FOV 75, this worked pretty well.
# About every 150 Z units the edge of the screen drifts 0.1
# Someone who is better at math might be able to sus out how to
# incorporate different FOVs into this calculation, but this is
# Good Enough(tm)

# define distance_coefficent = 150/0.1

# Caluclations.  Do NOT change these if you want it to keep working as intended.

define distance_coefficent = 0.000666666
define front_left_edge = front_distance * distance_coefficent
define front_right_edge = 1.0 - front_left_edge

define back_left_edge = back_distance * distance_coefficent
define back_right_edge = 1.0 - back_left_edge

# Just in case you change the mid range distance.
# I'm sure you have a good reason.
# You have a good reason, right??
define mid_left_edge = mid_distance * distance_coefficent
define mid_right_edge = 1.0 - mid_left_edge

# All Lefts subtract from 0.5.  All rights add to 0.5.
# The calculation is pretty simple.  Get the distance from the center
# and divide it by some number.  1.5, 2, 3, and 4 should work fine for us.
# Then subtract(go left) or add(go right) that number to 0.5

# Mid
#9 Presets
transform scene_left_edge: 
    zpos (mid_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (mid_left_edge+mid_xoffset, 0.0+mid_yoffset)

transform scene_left_far: 
    zpos (mid_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 - ((0.5 - mid_left_edge)/1.5) + mid_xoffset, 0.0+mid_yoffset)

transform scene_left: 
    zpos(mid_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos(0.5- ((0.5 - mid_left_edge)/2.0) + mid_xoffset, 0.0+mid_yoffset)

transform scene_center_offleft: 
    zpos (mid_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 - ((0.5 - mid_left_edge)/3.0) + mid_xoffset, 0.0+mid_yoffset)    

transform scene_center:
    zpos (mid_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos(0.5+mid_xoffset, 0.0+mid_yoffset)

transform scene_center_offright:
    zpos (mid_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 + ((mid_right_edge - 0.5)/3.0) - mid_xoffset, 0.0+mid_yoffset)

transform scene_right:
    zpos(mid_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos(0.5 + ((mid_right_edge - 0.5)/2.0) - mid_xoffset, 0.0+mid_yoffset) 

transform scene_right_far: 
    zpos (mid_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 + ((mid_right_edge - 0.5)/1.5) - mid_xoffset, 0.0+mid_yoffset)    

transform scene_right_edge:
    zpos (mid_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (mid_right_edge + mid_xoffset, 0.0+mid_yoffset)    


# Near/Front
# 9 Presets
transform scene_front_left_edge:
    zpos (front_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (front_left_edge+front_xoffset, 0.0+front_yoffset)

transform scene_front_left_far: 
    zpos (front_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 - ((0.5 - front_left_edge)/1.5) + front_xoffset, 0.0+front_yoffset)

transform scene_front_left:
    zpos (front_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 - ((0.5 - front_left_edge)/2.0) + front_xoffset, 0.0+front_yoffset)

transform scene_front_center_offleft:
    zpos (front_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 - ((0.5 - front_left_edge)/3.0)+front_xoffset, 0.0+front_yoffset)

transform scene_front_center:
    zpos (front_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5+front_xoffset, 0.0+front_yoffset)

transform scene_front_center_offright:
    zpos (front_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 + ((front_right_edge - 0.5)/3.0)-front_xoffset, 0.0+front_yoffset)

transform scene_front_right:
    zpos (front_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 + ((front_right_edge - 0.5)/2.0)-front_xoffset, 0.0+front_yoffset)

transform scene_front_right_far: 
    zpos (front_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 + ((front_right_edge - 0.5)/1.5) - front_xoffset, 0.0+front_yoffset)    

transform scene_front_right_edge:
    zpos (front_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (front_right_edge-front_xoffset, 0.0+front_yoffset)



# Distant/Back
# 13 Presets
transform scene_back_left_edge:
    zpos (back_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (back_left_edge+back_xoffset, 0.0+back_yoffset)

transform scene_back_left_far:
    zpos (back_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 - ((0.5 - back_left_edge)/1.5), 0.0+back_yoffset)

transform scene_back_left:
    zpos (back_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5- ((0.5 - back_left_edge)/2.0) + back_xoffset, 0.0+back_yoffset)

transform scene_back_left_nearedge:
    zpos (back_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 - ((0.5 - back_left_edge)/1.25), 0.0+back_yoffset)

transform scene_back_center_offleft:
    zpos (back_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 - ((0.5 - back_left_edge)/3.0), 0.0+back_yoffset)

transform scene_back_center_nearleft:
    zpos (back_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 - ((0.5 - back_left_edge)/5.0), 0.0+back_yoffset)

transform scene_back_center:
    zpos (back_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5+back_xoffset, 0.0+back_yoffset)

transform scene_back_center_nearright:
    zpos (back_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 + ((back_right_edge - 0.5)/5.0), 0.0+back_yoffset)


transform scene_back_center_offright:
    zpos (back_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 + ((back_right_edge - 0.5)/3.0), 0.0+back_yoffset)

transform scene_back_right_nearedge:
    zpos (back_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 + ((back_right_edge - 0.5)/1.25), 0.0+back_yoffset)

transform scene_back_right:
    zpos (back_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 + ((back_right_edge - 0.5)/2.0)+back_xoffset, 0.0+back_yoffset)

transform scene_back_right_far:
    zpos (back_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (0.5 + ((back_right_edge - 0.5)/1.5) + mid_xoffset, 0.0+back_yoffset)

transform scene_back_right_edge:
    zpos (back_distance)
    anchor(scene_xanchor, scene_yanchor)
    pos (back_right_edge+back_xoffset, 0.0+back_yoffset)

default test_timing = 0.5
transform test_stage:
    easeout test_timing scene_back_center
    pause 0.5
    easeout test_timing scene_back_center_offright
    pause 0.5
    easeout test_timing scene_back_center_nearright
    pause 0.5
    easeout test_timing scene_back_center_offleft
    pause 0.5
    easeout test_timing scene_back_center_nearleft
    pause 0.5
    easeout test_timing scene_back_left
    pause 0.5
    easeout test_timing scene_back_left_far
    pause 0.5
    easeout test_timing scene_back_right
    pause 0.5
    easeout test_timing scene_back_right_far
    pause 0.5
    easeout test_timing scene_back_left_edge
    pause 0.5
    easeout test_timing scene_back_right_edge
    pause 0.5
    easeout test_timing scene_front_center
    pause 0.5
    easeout test_timing scene_front_center_offleft
    pause 0.5
    easeout test_timing scene_front_center_offright
    pause 0.5
    easeout test_timing scene_front_right
    pause 0.5
    easeout test_timing scene_front_left
    pause 0.5
    easeout test_timing scene_front_right_edge
    pause 0.5
    easeout test_timing scene_front_left_edge
    pause 0.5
    easeout test_timing scene_center
    pause 0.5
    easeout test_timing scene_center_offleft
    pause 0.5
    easeout test_timing scene_center_offright
    pause 0.5
    easeout test_timing scene_right
    pause 0.5
    easeout test_timing scene_left
    pause 0.5
    easeout test_timing scene_left_far
    pause 0.5
    easeout test_timing scene_right_far
    pause 0.5
    easeout test_timing scene_left_edge
    pause 0.5
    easeout test_timing scene_right_edge
    pause 0.5
    easeout test_timing scene_back_center
    pause 0.5
    easeout test_timing scene_back_right
    pause 0.5
    easeout test_timing scene_back_left
    pause 0.5
    easeout test_timing scene_front_center
    pause 0.5
    easeout test_timing scene_front_right
    pause 0.5
    easeout test_timing scene_front_left
    pause 0.5
    repeat