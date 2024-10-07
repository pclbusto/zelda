import arcade
from PIL import Image

DIRECCION_ARRIBA = 0
DIRECCION_ABAJO = 1
DIRECCION_IZQUIERDA = 2
DIRECCION_DERECHA = 3
UPDATES_PER_FRAME = 5
CHARACTER_SCALING = 0.5
MOVEMENT_SPEED = 10 * CHARACTER_SCALING
DEAD_ZONE = 0.17
SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1440
SCREEN_TITLE = "Move with a Sprite Animation Example"


def load_texture_pair(filename, flipped=False):
    """
    Load a texture
    """
    textura = arcade.load_texture(filename, flipped_horizontally=flipped)
    im = textura.image
    textura.image = im.resize((int(im.size[0]*CHARACTER_SCALING), int(im.size[1]*CHARACTER_SCALING)))
    return textura

