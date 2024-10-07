import arcade
import random
from Zelda_character import Zelda_character
from helper import  *


class Zelda(arcade.Window):
    """Main application class.   """
    def __init__(self):
        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player = Zelda_character()

        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player.scale = 0.8

        self.player_list.append(self.player)

        # for i in range(COIN_COUNT):
        #     coin = arcade.Sprite(":resources:images/items/gold_1.png",
        #                          scale=0.5)
        #     coin.center_x = random.randrange(SCREEN_WIDTH)
        #     coin.center_y = random.randrange(SCREEN_HEIGHT)
        #
        #     self.coin_list.append(coin)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.player_list.draw()
        # Code to draw the screen goes here

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player
        self.player_list.update()

        # Update the players animation
        self.player_list.update_animation()

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

def main():
    """ Main method """
    window = Zelda()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
    # nro = 1
    # nro_txt = "{:02d}".format(nro)
    # print(nro_txt)