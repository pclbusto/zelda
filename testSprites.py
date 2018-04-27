""" 
 Mostramos como usar un sprite respaldado por un gráfico.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Vídeo explicativo: http://youtu.be/vRB_983kUMc
"""

import pygame
from pip._vendor.distlib.util import parse_name_and_version


def addImage(lista,imagen,x1, y1,x2,y2,invert):
    img1 = pygame.Surface((x2-x1+1, y2-y1+1))
    img1.blit(imagen, (0, 0), (x1, y1, x2-x1+1, y2-y1+1))
    img1.set_colorkey((0, 255, 0))
    img1 = img1.convert_alpha()
    if invert:
        img1 = pygame.transform.flip(img1, True, False)

    img1 = pygame.transform.scale(img1,(img1.get_width()*2, img1.get_height()*2))
    lista.append(img1)


# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
FPS = 60
pygame.init()

# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Mi Primer juego en Informática")

# El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.

hecho = False

# Se usa para esta blecer cuan rápido se actualiza la pantalla

megaman = pygame.image.load("Megaman\sprites megaman.png").convert_alpha()
fondo = pygame.image.load("fondo.png")
list_right_run = []
list_left_run = []


# addImage(list_right_run,megaman,2,19,25,41, True)
addImage(list_right_run,megaman,81,19,104,41, True)
addImage(list_right_run,megaman,111,18,126,41, True)
addImage(list_right_run,megaman,135,20,155,41, True)
# addImage(list_right_run,megaman,48,1067,185,1201, False)
# addImage(list_right_run,megaman,48,1326,185,1456, False)
# addImage(list_right_run,megaman,48,1580,185,1710, False)
# addImage(list_right_run,megaman,48,1830,185,1964, False)
# addImage(list_right_run,megaman,48,2080,185,2218, False)
# addImage(list_right_run,megaman,48,2337,185,2478, False)

# addImage(list_left_run,megaman,2,19,25,41, False)
addImage(list_left_run,megaman,82,19,104,41, False)
addImage(list_left_run,megaman,111,18,126,41, False)
addImage(list_left_run,megaman,135,20,155,41, False)

# addImage(list_left_run, megaman, 48, 2337,185,2478, True)
# addImage(list_left_run, megaman, 48, 2080,185,2218, True)
# addImage(list_left_run, megaman, 48, 1830,185,1964, True)
# addImage(list_left_run, megaman, 48, 1580,185,1710, True)
# addImage(list_left_run, megaman, 48, 1326,185,1456, True)
# addImage(list_left_run, megaman, 48, 1067,185,1201, True)
# addImage(list_left_run, megaman, 48, 809,185,948, True)
# addImage(list_left_run, megaman, 48, 560,185,694, True)
# addImage(list_left_run, megaman, 48, 310,185,440, True)
# addImage(list_left_run, megaman, 48, 55,185,185, True)






speed = 10
reloj = pygame.time.Clock()

i=0
delta = 0.2 #len(list_run)/FPS
print(delta)
direccion = 1
index = 0
pygame.key.set_repeat(1,1)
# -------- Bucle principal del Programa -----------
while not hecho:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        elif evento.type == pygame.KEYDOWN:
            lista = pygame.key.get_pressed()
            if lista[pygame.K_LEFT]==1:
                index = int(i) % len(list_left_run)
                i -= delta
                direccion = -1
            if lista[pygame.K_RIGHT] == 1:
                index = int(i) % len(list_left_run)
                i += delta
                direccion = 1

    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ

    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ

    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima 
    # de esto, de otra forma serán borrados por este comando:

    pantalla.fill(BLANCO)
    pantalla.blit(fondo,(0,0))
    # index = int(i)%len(list_left_run)
    if direccion == 1:
        pantalla.blit(list_right_run[index], (i*speed, 150))
    else:
        pantalla.blit(list_left_run[index], (i *speed , 150))
    # pantalla.blit(list_run[6], (0, 0))

    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(FPS)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()
