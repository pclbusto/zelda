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
import math

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

STATE_PARADO = 0
STATE_CORRIENDO = 1
STATE_SALTANDO_UP = 2
STATE_SALTANDO_DOWN = 3
DIRECCION_IZQUIERDA = -1
DIRECCION_DERECHA = 1


FPS = 60
pygame.init()

# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Mi Primer juego en Informática")

# El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.

hecho = False

# Se usa para esta blecer cuan rápido se actualiza la pantalla

megaman = pygame.image.load("Megaman/sprites megaman.png").convert_alpha()
# fondo = pygame.image.load("fondo.png")
list_right_stand = []
list_left_stand = []
list_right_run = []
list_left_run = []
list_jump_right = []
list_jump_left = []
porcentaje_salto = []
for x in range(0,90,4):
    porcentaje_salto.append(math.sin(math.radians(x)))
    print(math.sin(math.radians(x)))
longitud_lista_porcentaje =len(porcentaje_salto)-2
print(len(porcentaje_salto))

addImage(list_left_stand, megaman,4,19,23,41,True)
addImage(list_left_stand, megaman,29,19,48,41,True)
addImage(list_left_stand, megaman,54,19,73,41,True)

addImage(list_right_stand, megaman,4,19,23,41,False)
addImage(list_right_stand, megaman,29,19,48,41,False)
addImage(list_right_stand, megaman,54,19,73,41,False)

# addImage(list_right_run,megaman,2,19,25,41, True)
addImage(list_right_run ,megaman,81,18,104,41, True)
addImage(list_right_run,megaman,107,18,130,41, True)
addImage(list_right_run,megaman,135,18,158,41, True)
addImage(list_right_run,megaman,107,18,130,41, True)

addImage(list_left_run,megaman,81,18,104,41, False)
addImage(list_left_run,megaman,107,18,130,41, False)
addImage(list_left_run,megaman,135,18,158,41, False)
addImage(list_left_run,megaman,107,18,130,41, False)

addImage(list_jump_right,megaman,195,10,221,40, True)
addImage(list_jump_left,megaman,195,10,221,40, False)






speed =12
reloj = pygame.time.Clock()

i=0
delta = 0.15 #len(list_run)/FPS
print(delta)
direccion = 1
estado = 0 #0=corriendo o parado 1=saltando
index_porcentaje_salto = 0
index = 0
pygame.key.set_repeat(1,1)
# -------- Bucle principal del Programa -----------
while not hecho:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        # elif evento.type == pygame.KEYDOWN or evento.type == pygame.KEYUP:
        #     print("presionada o liberada")
    lista = pygame.key.get_pressed()
    if lista[pygame.K_LEFT]==1:
        index = int(i) % len(list_left_run)
        i -= delta
        direccion = DIRECCION_IZQUIERDA
        estado = STATE_CORRIENDO

    if lista[pygame.K_RIGHT] == 1:
        index = int(i) % len(list_left_run)
        i += delta
        direccion = DIRECCION_DERECHA
    if lista[pygame.K_RIGHT] == 0:
        estado =STATE_PARADO
    if lista[pygame.K_a]==1:
        if estado == 0:
            estado=STATE_SALTANDO_UP
            index_porcentaje_salto += 1
        elif estado == STATE_SALTANDO_UP and index_porcentaje_salto<longitud_lista_porcentaje:
            index_porcentaje_salto +=1
        elif estado == STATE_SALTANDO_UP and index_porcentaje_salto>=longitud_lista_porcentaje:
            estado = STATE_SALTANDO_DOWN
            index_porcentaje_salto -= 1
        elif estado == STATE_SALTANDO_DOWN and index_porcentaje_salto > 0:
            index_porcentaje_salto -= 1
        elif estado == STATE_SALTANDO_DOWN and index_porcentaje_salto == 0:
            index = 0
            estado = STATE_PARADO
        # print("index: {} estado {} pos salto {}".format(index_porcentaje_salto,estado,150-(80* porcentaje_salto[index_porcentaje_salto])))

    if lista[pygame.K_a]==0 and estado in[1,2]:
        if index_porcentaje_salto >0:
            index_porcentaje_salto -= 1
            estado = STATE_SALTANDO_DOWN
        elif index_porcentaje_salto == 0:
            estado = STATE_PARADO


    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ

    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ

    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima 
    # de esto, de otra forma serán borrados por este comando:
    pantalla.fill(NEGRO)
    # pantalla.blit(fondo,(0,0))
    # index = int(i)%len(list_left_run)
    if direccion == DIRECCION_DERECHA and estado == STATE_CORRIENDO:
        pantalla.blit(list_right_run[index], (i*speed, 150))
    elif direccion == DIRECCION_IZQUIERDA and estado == STATE_CORRIENDO:
        pantalla.blit(list_left_run[index], (i *speed , 150))
    elif direccion == DIRECCION_DERECHA and estado in[STATE_SALTANDO_UP,STATE_SALTANDO_DOWN]:
        pantalla.blit(list_jump_right[0], (i * speed, 150-(110* porcentaje_salto[index_porcentaje_salto])))
    elif direccion == DIRECCION_IZQUIERDA and estado in[STATE_SALTANDO_UP,STATE_SALTANDO_DOWN]:
        pantalla.blit(list_jump_left[0], (i * speed, 150-(110*porcentaje_salto[index_porcentaje_salto])))
    elif direccion == DIRECCION_IZQUIERDA and estado in[STATE_PARADO]:
        pantalla.blit(list_left_stand[0], (i , 150))
    elif direccion == DIRECCION_DERECHA and estado ==STATE_PARADO:
        pantalla.blit(list_right_stand[0], (i , 150))
    elif direccion == DIRECCION_IZQUIERDA and estado ==STATE_PARADO:
        pantalla.blit(list_left_stand[0], (i , 150))
    # pantalla.blit(list_run[6], (0, 0))

    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(FPS)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()
