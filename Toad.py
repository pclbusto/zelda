import  arcade

SPRITE_SCALING = 1
CHARACTER_SCALING = 1
TEXTURE_RIGHT = True
# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1
UPDATES_PER_FRAME = 7

class Toad(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.character_face_direction = RIGHT_FACING
        # Track out state
        self.jumping = False
        self.walking = False
        self.running = False
        self.swimming = False
        self.standup = True
        self.hanging = False
        self.climbing = False
        self.is_on_ladder = False
        self.cur_texture = 0
        self.scale = CHARACTER_SCALING
        image_source_parado = "Megaman/toad_parado_0{}.png"
        image_source_corriendo = "Megaman/toad_corriendo_0{}.png"

        self.texturas_parado = []
        for i in range(1, 80):
            idle_texture_pair = arcade.load_texture_pair(image_source_parado.format(1))
            self.texturas_parado.append(idle_texture_pair)
        for i in range(1, 32):
            idle_texture_pair = arcade.load_texture_pair(image_source_parado.format(2))
            self.texturas_parado.append(idle_texture_pair)
        print(len(self.texturas_parado))
        self.texturas_corriendo = []
        for i in range(1, 6):
            running_texture_pair = arcade.load_texture_pair(image_source_corriendo.format(i))
            self.texturas_corriendo.append(running_texture_pair)

    def update(self):
        self.cur_texture += 1
        self.cur_texture %= 54*2
        print(self.cur_texture)
        self.texture = self.texturas_parado[self.cur_texture][self.character_face_direction]

