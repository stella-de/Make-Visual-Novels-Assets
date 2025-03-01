Transform List

Middle(Default depth) positions-----
From furthest left to furthest right
scene_left_edge 
scene_left_far
scene_left
scene_center_offleft
scene_center
scene_center_offright
scene_right
scene_right_far
scene_right_edge

Front(Closer to Camera) positions-----
From furthest left to furthest right
scene_front_left_edge
scene_front_left_far
scene_front_left
scene_front_center_offleft
scene_front_center
scene_front_center_offright
scene_front_right
scene_front_right_far
scene_front_right_edge

Back(Furthest from Camera) positions-----
From furthest left to furthest right
scene_back_left_edge
scene_back_left_nearedge
scene_back_left_far
scene_back_left
scene_back_center_offleft
scene_back_center_nearleft
scene_back_center
scene_back_center_nearright
scene_back_center_offright
scene_back_right
scene_back_right_far
scene_back_right_nearedge
scene_back_right_edge

Camera Transforms

These are two specific shots.  You need to specify the X position on the camera when you use shot_pedestal and the y position when you use shot_establish, otherwise it will use the camera's current X or Y.

shot_pedestal
shot_establish

These are origin transforms.  zoom_origin will animate the transistion back to the camera's origin position.  Just origin will make the camera cut back instantly.  Use origin when you're changing scenes!

zoom_origin
origin

These are animated, positional zooms, based off of the premade staging transforms.  They're not as flexible as the staging positions, but they'll cover the majority of use cases.  I might update these later if there's a big demand for more flexible zooms

zoom_front_right
zoom_front_left
zoom_front_center
zoom_back_right
zoom_back_left
zoom_back_center
zoom_right
zoom_left
zoom_center


Test Transforms-----
Apply this to a character to have them cycle through all of the positions.  Good way to check to see if you're going to have any problems with a specific character sprite.

test_stage