import arcade
from helper import *

class Zelda_character(arcade.Sprite):
    def __init__(self):

        # Set up parent class
        super().__init__(scale = 0.1)

        # Default to face-right
        self.character_face_direction = DIRECCION_DERECHA

        # Used for flipping between image sequences
        self.cur_texture = 0

        # self.scale = 0.25

        # Adjust the collision box. Default includes too much empty space
        # side-to-side. Box is centered at sprite center, (0, 0)
        self.points = [[-22, -64], [22, -64], [22, 28], [-22, 28]]

        # Get list of game controllers that are available
        joysticks = arcade.get_joysticks()
        print(joysticks)
        # If we have any...
        if joysticks:
            # Grab the first one in  the list
            self.joystick = joysticks[0]

            # Open it for input
            self.joystick.open()

            # Push this object as a handler for joystick events.
            # Required for the on_joy* events to be called.
            self.joystick.push_handlers(self)
        else:
            # Handle if there are no joysticks.
            print("There are no joysticks, plug in a joystick and run again.")
            self.joystick = None

        # --- Load Textures ---

        # Images from Kenney.nl's Asset Pack 3
        main_path = "imagenes/characters/Link/"

        # Load textures for idle standing front
        self.idle_texture_pair = load_texture_pair(f"{main_path}idle front-01.png")
        # Load textures for walking
        self.walk_textures = []
        # creamos listas vacias para lista de animaciones arriba abajo derecha e izqierda



        self.walk_textures.append([])
        for i in range(1,11):
            nro = "{:02d}".format(i)
            texture = load_texture_pair(f"{main_path}walk back-{nro}.png")
            self.walk_textures[DIRECCION_ARRIBA].append(texture)
        self.walk_textures.append([])
        for i in range(1,11):
            nro = "{:02d}".format(i)
            texture = load_texture_pair(f"{main_path}walk front-{nro}.png")
            self.walk_textures[DIRECCION_ABAJO].append(texture)
        self.walk_textures.append([])
        for i in range(1,11):
            nro = "{:02d}".format(i)
            texture = load_texture_pair(f"{main_path}walk side-{nro}.png")
            self.walk_textures[DIRECCION_IZQUIERDA].append(texture)
        self.walk_textures.append([])
        for i in range(1,11):
            nro = "{:02d}".format(i)
            texture = load_texture_pair(f"{main_path}walk side-{nro}.png", flipped=True)
            self.walk_textures[DIRECCION_DERECHA].append(texture)
        self.update_animation()
        self.hit_box = self.texture.hit_box_points
    def update(self):
        """ Move the player """

        # If there is a joystick, grab the speed.
        if self.joystick:

            # x-axis
            # print("X:{} y:{}".format(self.joystick.x, self.joystick.y))
            self.change_x = self.joystick.x * MOVEMENT_SPEED
            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.x ) < DEAD_ZONE:
                self.change_x = 0

            # y-axis
            # if self.change_x!=0:

            self.change_y = -self.joystick.y * MOVEMENT_SPEED
            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.y) < DEAD_ZONE:
                self.change_y = 0

        # Move the player
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Keep from moving off-screen
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1
        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


    def update_animation(self, delta_time: float = 1/60):


        # Figure out if we need to flip face left or right



        if abs(self.change_x)>abs(self.change_y):
            if self.change_x < 0:
                self.character_face_direction = DIRECCION_IZQUIERDA
            elif self.change_x > 0:
                self.character_face_direction = DIRECCION_DERECHA
        else:
            if self.change_y > 0:
                self.character_face_direction = DIRECCION_ARRIBA
            elif self.change_y < 0:
                self.character_face_direction = DIRECCION_ABAJO

        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_pair
            self.cur_texture = 0
            return

        # Walking animation
        self.cur_texture += 1
        if self.cur_texture > 9 * UPDATES_PER_FRAME:
            self.cur_texture = 0
        frame = self.cur_texture // UPDATES_PER_FRAME
        self.texture = self.walk_textures[self.character_face_direction][frame]
        self.hit_box = self.texture.hit_box_points

        #self.texture = self.walk_textures[DIRECCION_IZQUIERDA][frame]