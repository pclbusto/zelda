import arcade

SCREEN_WIDTH = 9
SCREEN_HEIGHT = 9

class Ball:
    """ This class manages a ball bouncing on the screen. """

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        """ Constructor. """

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
        self.background = arcade.load_texture("artic_cavern.png")

        #self.background = arcade.Sprite("mountains.png", 1)
        self.background_x = 0
        self.background_y = 0

    def draw(self):
        """ Draw the balls with the instance variables we have. """


        arcade.draw_lrwh_rectangle_textured(self.background_x, 0,
                                            self.background.width, self.background.height,
                                            self.background)
        if (self.background_x%self.background.width)< self.background.width-SCREEN_WIDTH:
            arcade.draw_lrwh_rectangle_textured(self.background_x+self.background.width, 0,
                                                self.background.width, self.background.height,
                                                self.background)
            arcade.draw_lines(
                [(self.background_x + self.background.width, 0), (self.background_x + self.background.width,
                                                                  SCREEN_HEIGHT)], arcade.color.RED, 2)

        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        """ Code to control the ball's movement. """
        # rel_x = x % bkgd.get_rect().width
        # DS.blit(bkgd, (rel_x - bkgd.get_rect().width, 0))
        # if rel_x < W:
        #     DS.blit(bkgd, (rel_x, 0))
        # x -= 2
        # pygame.draw.line(DS, (255, 0, 0), (rel_x, 0), (rel_x, H), 3)

        self.background_x -= 4
        self.background_x %= self.background.width
        self.background_x -= self.background.width
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ My window class. """

    def __init__(self, width, height, title):
        """ Constructor. """
        # Call the parent class's init function
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.set_vsync(True)
        # Create our ball
        self.ball = Ball(50, 50, 3, 3, 15, arcade.color.AUBURN)
        self.set_update_rate(1/60)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.update()


def main():
    global SCREEN_WIDTH, SCREEN_HEIGHT
    bg = arcade.Sprite("artic_cavern.png", 1)
    SCREEN_WIDTH = 576 #bg._width//2
    SCREEN_HEIGHT = 1000
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

    arcade.run()


main()