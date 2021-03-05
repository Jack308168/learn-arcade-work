import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.15
SPRITE_SCALING_COIN = 0.15
COIN_COUNT = 25
BAD_COIN_COUNT = 10

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Sprite Collect Coins Example"


class MyGame(arcade.Window):
    

    def __init__(self):
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_list = None
        self.good_coin_list = None
        self.bad_coin_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0
        self.lives = 3

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.game_over_list = arcade.SpriteList()
        self.good_coin_list = arcade.SpriteList()
        self.bad_coin_list = arcade.SpriteList()

        # Score
        self.score = 0
        self.lives = 3

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("Shrek.PNG",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)


        self.game_over_sprite = arcade.Sprite("Shrek U R Die.jpg",1.05)
        self.game_over_sprite.center_x = 250
        self.game_over_sprite.center_y = 250
        self.game_over_list.append(self.game_over_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("Fiona.PNG",
                                 SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.good_coin_list.append(coin)

        # Create the coins
        for i in range(BAD_COIN_COUNT):
 
            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("Donkey.PNG",
                                 SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.bad_coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        if self.lives < 0:
            #draw a picture of game over screen
            self.game_over_list.draw()    
           
            return

        self.good_coin_list.draw()
        self.bad_coin_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        output = f"lives: {self.lives}"
        arcade.draw_text(output, 10, 40, arcade.color.WHITE, 14)


    def on_mouse_motion(self, x, y, dx, dy):
        

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.good_coin_list.update()
        self.bad_coin_list.update()


        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.lives -= 1

        # Game Over
        

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()