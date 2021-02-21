import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        print("MAIN WINDOW MADE")

        arcade.set_background_color(arcade.color.AMAZON)
    def on_key_press(self, key, key_modifiers):
        print("MAIN WINDOW KEY PRESS")
        #GO TO GAME OVER SCREEN
        
        self.close()
        gameover = GameOverWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    def on_draw(self):
        arcade.start_render()

class GameOverWindow(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.RED)
        print("GAME OVER WINDOW MADE")

    def on_key_press(self, key, key_modifiers):
        print("GAME OVER KEY PRESS")

    def on_draw(self):
        arcade.start_render()

def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()