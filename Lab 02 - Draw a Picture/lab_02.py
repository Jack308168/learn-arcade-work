'''
In case of "ModuleNotFoundError: No module named ..."
To install a new module in Python:

py -m pip install arcade

(instead of arcade, you can write the name of the module that you want)

'''

"""
This is a sample program

Multi_line comments are surround by three double-quotes
"""

# Import the "arcade" Library

import arcade

arcade.open_window(600, 600,  "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a rectangle 
# left of 0, right of 599
# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

# Tree trunk
# Center of 100, 320
# Width of 20
# Hight of 60
arcade.draw_rectangle_filled(100, 300, 20, 60, arcade.csscolor.SIENNA)

# Tree top
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

# Drawing code goes here

# Another tree, with an ellopse for the top
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)

# Another tree, with a trunk and arc ofr the top
# Arc is centered at (300, 340) with a width of 50 and hight of 100.
# The starting angle is 0, and ending angele is 180 
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

#Another tree, with a trunk and triqngle for the top
# Triangle is made of these points:
# (400, 400), (370, 320), (430, 320)
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)

# Draw a tree using a polygon with a list of points
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)
                            ),
                            arcade.csscolor.DARK_GREEN)

# Draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

# Rays to the left, right, up, and down
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)

# Diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

# House 
arcade.draw_rectangle_filled(400, 150, 180, 180, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(310, 240, 490, 240, 400, 350, arcade.csscolor.MAROON)
arcade.draw_rectangle_filled(400, 110, 50, 100, arcade.csscolor.YELLOW)
arcade.draw_circle_filled(420, 115, 3, arcade.color.BLACK)

# Finish Drawing
arcade.finish_render()

# Keep the window open
arcade.run()