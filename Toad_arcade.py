import  arcade

SPRITE_SCALING = 1
CHARACTER_SCALING = 2
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
        self.FRAMES_OJOS_ABIERTO = 100
        self.FRAMES_PARPADEO = 20
        self.index_textura_parado = 0
        self.index_textura_walking = 0
        self.timer_parpadeo = 0

        image_source_parado = "Megaman/toad_parado_0{}.png"
        image_source_corriendo = "Megaman/toad_corriendo_0{}.png"

        self.texturas_parado = []
        for i in range(1, 3):
            idle_texture_pair = arcade.load_texture_pair(image_source_parado.format(i))
            self.texturas_parado.append(idle_texture_pair)
        print(len(self.texturas_parado))
        self.texturas_corriendo = []
        for i in range(1, 6):
            running_texture_pair = arcade.load_texture_pair(image_source_corriendo.format(i))
            self.texturas_corriendo.append(running_texture_pair)


    def update(self):
        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
            self.standup = False
            self.walking = True

        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING
            self.standup = False
            self.walking = True

        elif self.change_x == 0:
            self.standup = True
            self.walking = False

        self.center_x += self.change_x

        if self.standup:
            self.update_standup()
        if self.walking:
            self.update_walking()

    def update_walking(self):
        self.index_textura_walking += 1
        self.index_textura_walking %= 5
        self.texture = self.texturas_corriendo[self.index_textura_walking][self.character_face_direction]


    def update_standup(self):
        # ojos abiertos
        if self.index_textura_parado == 0:
            if self.timer_parpadeo <= self.FRAMES_OJOS_ABIERTO:
                self.timer_parpadeo += 1
            else:
                # se produce un parpadeo
                self.timer_parpadeo = 0
                self.index_textura_parado += 1
        elif self.index_textura_parado == 1:
            if self.timer_parpadeo <= self.FRAMES_PARPADEO:
                self.timer_parpadeo += 1
            else:
                # se termina el parpadeo o de tener los ojos cerrados
                self.index_textura_parado = 0
                self.timer_parpadeo = 0
        self.texture = self.texturas_parado[self.index_textura_parado][self.character_face_direction]

        #self.cur_texture += 1
        #self.cur_texture %= 54*2
        #print(self.cur_texture)


