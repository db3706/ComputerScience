import arcade

# Set constants for the screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Boxer Practicing"

# Open the window. Set the window title and dimensions
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.WHITE)
# Clear screen and start render process
arcade.start_render()

# Draw head
arcade.draw_circle_filled(700, 500, 55, arcade.color.BATTLESHIP_GREY)
# Draw the upper torso
arcade.draw_rectangle_filled(700, 400, 130, 130, arcade.color.BATTLESHIP_GREY)

# Draw the lower torso
arcade.draw_rectangle_filled(700, 300, 120, 70, arcade.color.BATTLESHIP_GREY)

# Draw right shoulder 
arcade.draw_rectangle_filled(625, 439, 54, 54, arcade.color.CADET_GREY)

# Draw right bicep 
arcade.draw_rectangle_filled(570, 439, 130, 49, arcade.color.CADET_GREY)

# Draw right forearm 
arcade.draw_rectangle_filled(465, 439, 130, 45, arcade.color.CADET_GREY)

# Draw right boxing glove
arcade.draw_rectangle_filled(380, 439, 60, 60, arcade.color.CADMIUM_RED)

# Draw left shoulder
arcade.draw_rectangle_filled(770, 435, 54, 54, arcade.color.CADET_GREY)

# Draw left bicep
arcade.draw_rectangle_filled(781, 380, 49, 100, arcade.color.CADET_GREY, -15)

# Draw left forearm
arcade.draw_rectangle_filled(735, 375, 45, 110, arcade.color.CADET_GREY, -30)

# Draw left boxing glove
arcade.draw_rectangle_filled(703, 430, 60, 60, arcade.color.CADMIUM_RED, -30)

# Draw right upper leg
arcade.draw_rectangle_filled(645, 180, 43, 130, arcade.color.BATTLESHIP_GREY, 35)

# Draw right lower leg
arcade.draw_rectangle_filled(615, 80, 43, 100, arcade.color.BATTLESHIP_GREY)

# Draw right foot
arcade.draw_rectangle_filled(605, 20, 65, 20, arcade.color.BATTLESHIP_GREY)

# Draw left upper leg
arcade.draw_rectangle_filled(745, 180, 43, 130, arcade.color.BATTLESHIP_GREY, -20)

# Draw left upper leg
arcade.draw_rectangle_filled(785, 90, 43, 100, arcade.color.BATTLESHIP_GREY, -30)

# Draw left foot
arcade.draw_rectangle_filled(800, 35, 65, 20, arcade.color.BATTLESHIP_GREY, -30)
# Draw boxing shorts
point_list = ((640, 265),
              (760, 265),
              (760, 210),
              (710, 210),
              (700, 220),
              (690, 210),
              (640, 210)

)
arcade.draw_polygon_filled(point_list, arcade.color.SPANISH_VIOLET)



# Finish drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()

