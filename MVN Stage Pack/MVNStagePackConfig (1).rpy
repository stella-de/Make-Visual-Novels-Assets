#Camera Preset Configurations

#Change to modify the pedestal shot (Pan camera up)
define pedestal_zoffset = 0.0
define pedestal_start_yoffset = 0.0
define pedestal_end_yoffset = 0.0
define pedestal_duration = 10.0

#Change to modify the establishing shot (Pan left to right)
define establish_zoffset = 0
define establish_start_xoffset = 0.0
define establish_end_xoffset = 0.0
define establish_duration = 10.0

# Camera Zoom Configs

#Time for all premade zoom effects.
define default_zoom_time = 1.3

#ZOffsets for Zooms.   Adjust if you change the distance of any of the sections in the config, or just want closer/further zooms.

define zoom_front_zoffset = 0
define zoom_mid_zoffset = 0 
define zoom_back_zoffset = 0

#YOffsets for Zooms.  Adjust this if your camera needs to adjust for taller/shorter sprites.  This is a universal setting, so consider individualized offsets if your sprites have significant height variations.

define zoom_front_yoffset = 0.0
define zoom_mid_yoffset = 0.0
define zoom_back_yoffset = 0.0

#XOffsets for Zooms.  Adjust this if your camera needs to adjust for wider sprites, or sprites where the character's average face location is off center, or if you prefer your zooms compositions to be left/right heavy.

define zoom_front_xoffset = 0.0
define zoom_mid_xoffset = 0.0
define zoom_back_xoffset = 0.0

#Default anchorings for this pack.  If you change this, it will make most of the presets stage themselves in odd ways.  This places the anchor point of a displayable at the center of the bottom of the displayable.  Changing the y anchor to 0.9-0.95 will hide the bottom 5-10% of your sprites past the screen brder, which actually might be desireable, but I'd recommend doing that with the Y offsets below instead.

define scene_xanchor = 0.5
define scene_yanchor = 1.0

#Distance Definitions.  If you change these, the pack should recalculate the new screen edges for you automattically.  You can change this if you want your sprites to be more or less distant in these three positions. The camera and background themselves are members of the scene, so it's possible to move a sprite out of view of the camera by putting it behind it, or behind the background, so test different numbers as you're adjusting.

define mid_distance = 0
define back_distance = -300
define front_distance = 300

#Y OffSets
#The higher the number, the further down screen the sprites will be adjusted.
#At distance(set above) 0, 1.0 is the bottom edge of the screen, 0.0 is the top.
#This is useful if you have particularly tall or short sprites on average and you need 
#to adjust the position to keep them in frame.
# Default mid=1.0, back=1.0, front=1.2
# These defaults are here because I prefer to hide the feet of sprites and use full body/thigh up sprites.
define mid_yoffset = 1.05
define back_yoffset = 1.0
define front_yoffset = 1.1


#X Offsets
#The higher the number, the further from the center the sprites are pushed.
#At distance 0, 0.0 is the left edge of the screen, 1.0 is the right side of the screen.
#This is useful if you have left or right heavy sprites on average and need to adjustments
#to keep their faces in display. Default is 0.0
define mid_xoffset = 0.0 
define back_xoffset = 0.0
define front_xoffset = 0.0 