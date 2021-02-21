import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
snow_person1_x = 550

def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

def draw_snow_person(x, y):
    """ Draw a snow person """ 
    
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(0 + x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(0 + x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(0 + x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(-15 + x, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(15 + x, 210 + y, 5, arcade.color.BLACK)

def on_draw(delta_time):
    """ Draw everything """

    global snow_person1_x
    arcade.start_render()
    draw_grass()
    draw_snow_person(snow_person1_x, 140)
    draw_snow_person(450, 180)
    
    snow_person1_x += 1

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    arcade.schedule(on_draw, 1/60)
    # Draw a snow person

    #  Finish and run
    arcade.finish_render()
    arcade.run()

# Call the main function to get the program started
main()