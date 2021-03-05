import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3


class Ball:

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
        self.laser_sound = arcade.load_sound("laser.ogg")

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x +10, self.position_y +0, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x +0, self.position_y +10, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x -10, self.position_y -0, self.radius, self.color)
        arcade.draw_circle_filled(self.position_x -0, self.position_y -10, self.radius, self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x
         
        if self.position_x < 25:
            self.position_x = 25
            arcade.play_sound(self.laser_sound)

        if self.position_x > SCREEN_WIDTH - 25:
            self.position_x = SCREEN_WIDTH - 25
            arcade.play_sound(self.laser_sound)

        if self.position_y < 25:
            self.position_y = 25
            arcade.play_sound(self.laser_sound)

        if self.position_y > SCREEN_HEIGHT - 25:
            self.position_y = SCREEN_HEIGHT - 25
            arcade.play_sound(self.laser_sound)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball1 = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)
        self.ball2 = Ball(150, 50, 0, 0, 15, arcade.color.BLUE)

        self.background_sprite = arcade.Sprite("Shrek U R Die.jpg",1.5)
        self.background_sprite.center_x = 320
        self.background_sprite.center_y = 240

        self.laser_sound = arcade.load_sound("laser.ogg")

    def on_draw(self):
        arcade.start_render()

        self.background_sprite.draw()
        self.ball1.draw() 
        self.ball2.draw()

    def update(self, delta_time):
        self.ball1.update()
        self.ball2.update()

    def on_mouse_motion(self, x, y, dx, dy):
        self.ball2.position_x = x
        self.ball2.position_y = y
              
    def on_mouse_press(self, x, y, button, modifiers):
        arcade.play_sound(self.laser_sound)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball1.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball1.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball1.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball1.change_y = -MOVEMENT_SPEED


    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball1.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball1.change_y = 0

        # Load the sound when the application starts
        

def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()
    
main()

