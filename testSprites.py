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



# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

FACTOR_SCALADO = 2
STATE_PARADO = 0
STATE_CORRIENDO = 1
STATE_SALTANDO_UP = 2
STATE_SALTANDO_DOWN = 3
DIRECCION_IZQUIERDA = -1
DIRECCION_DERECHA = 1
FRAMES_PARPADEO = 15
FRAMES_OJOS_ABIERTO = 45
VEL_CORRER_X = 1.375 * FACTOR_SCALADO
VEL_SALTO_X = 1.312 * FACTOR_SCALADO
VEL_SALTO_Y = 4.87 * FACTOR_SCALADO
DESACEL_Y = 0.25 * FACTOR_SCALADO
LIM_MENOR_ACEL_Y = -12
LIM_MEN_SALTO = 1.183 * FACTOR_SCALADO
LIM_ACEL_SIN_SALTO_PRECIONADO = 2.12



def addImage(lista,imagen,x1, y1,x2,y2,invert):
    img1 = pygame.Surface((x2-x1+1, y2-y1+1))
    img1.blit(imagen, (0, 0), (x1, y1, x2-x1+1, y2-y1+1))
    img1.set_colorkey((0, 255, 0))
    img1 = img1.convert_alpha()
    if invert:
        img1 = pygame.transform.flip(img1, True, False)

    img1 = pygame.transform.scale(img1,(img1.get_width()*FACTOR_SCALADO, img1.get_height()*FACTOR_SCALADO))
    lista.append(img1)




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
timer_parpadeo = 0
vel_salto = VEL_SALTO_Y
# for x in range(0,90,4):
#     porcentaje_salto.append(math.sin(math.radians(x)))
#     print(math.sin(math.radians(x)))
# for x in range(0,60,1):
#     porcentaje_salto.append(4.75*x)
#     print(math.sin(math.radians(x)))


addImage(list_right_stand, megaman,4,19,23,41,True)
addImage(list_right_stand, megaman,29,19,48,41,True)
addImage(list_right_stand, megaman,54,19,73,41,True)

addImage(list_left_stand, megaman,4,19,23,41,False)
addImage(list_left_stand, megaman,29,19,48,41,False)
addImage(list_left_stand, megaman,54,19,73,41,False)

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






reloj = pygame.time.Clock()

x = 0
y = 150

delta = 0.15 #len(list_run)/FPS
delta_acumulado = 0
direccion = 1
estado = 0 #0=corriendo o parado 1=saltando
index_porcentaje_salto = 0
index_parado = 0
index_frame_corriendo = 0
index = 0
pygame.key.set_repeat(1,1)
# -------- Bucle principal del Programa -----------
while not hecho:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

    lista = pygame.key.get_pressed()
    if lista[pygame.K_LEFT] == 1:
        index_frame_corriendo = int(delta_acumulado) % len(list_left_run)
        delta_acumulado -= delta
        x -= VEL_CORRER_X
        direccion = DIRECCION_IZQUIERDA
        if estado == STATE_PARADO:
            estado = STATE_CORRIENDO


    if lista[pygame.K_RIGHT] ==1:
        index_frame_corriendo = int(delta_acumulado) % len(list_left_run)
        delta_acumulado += delta
        x += VEL_CORRER_X
        direccion = DIRECCION_DERECHA
        if estado == STATE_PARADO:
            estado = STATE_CORRIENDO

    if lista[pygame.K_RIGHT] == 0 and lista[pygame.K_LEFT] == 0 and estado == STATE_CORRIENDO:
        estado =STATE_PARADO
        timer_parpadeo = 0

    if estado == STATE_PARADO and index_parado == 0 and timer_parpadeo <= FRAMES_OJOS_ABIERTO:
        timer_parpadeo += 1
    if estado == STATE_PARADO and index_parado == 1 and timer_parpadeo <= FRAMES_PARPADEO:
        timer_parpadeo += 1
    if estado == STATE_PARADO and index_parado == 0 and timer_parpadeo == FRAMES_OJOS_ABIERTO:
        index_parado = 1
        timer_parpadeo = 0
    if estado == STATE_PARADO and index_parado == 1 and timer_parpadeo == FRAMES_PARPADEO:
        index_parado = 0
        timer_parpadeo = 0

    if lista[pygame.K_a] == 1:
        if estado == STATE_CORRIENDO or estado == STATE_PARADO:
            estado = STATE_SALTANDO_UP
            y -= vel_salto
            vel_salto -= DESACEL_Y
        elif estado == STATE_SALTANDO_UP:
            y -= vel_salto
            vel_salto -= DESACEL_Y

    elif lista[pygame.K_a]==0 and estado in [STATE_SALTANDO_DOWN, STATE_SALTANDO_UP]:
        # print("index salto: {} stado {}".format(index_porcentaje_salto, estado))
        if vel_salto >=LIM_ACEL_SIN_SALTO_PRECIONADO:
            vel_salto = 1

    # print("tecla A {} estado {} porcentaje {}".format(lista[pygame.K_a], estado,index_porcentaje_salto))
    # print("index: {} estado {} direccion {} pos salto {}".format(index_porcentaje_salto, estado, direccion,
    #                                                 150 - (110 * porcentaje_salto[index_porcentaje_salto])))

    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ

    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ

    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima 
    # de esto, de otra forma serán borrados por este comando:
    pantalla.fill(NEGRO)
    # pantalla.blit(fondo,(0,0))
    # index = int(i)%len(list_left_run)
    if direccion == DIRECCION_DERECHA and estado == STATE_CORRIENDO:
        pantalla.blit(list_right_run[index_frame_corriendo], (x, y))
    elif direccion == DIRECCION_IZQUIERDA and estado == STATE_CORRIENDO:
        pantalla.blit(list_left_run[index_frame_corriendo], (x , y))
    elif direccion == DIRECCION_DERECHA and estado in[STATE_SALTANDO_UP,STATE_SALTANDO_DOWN]:
        pantalla.blit(list_jump_right[0], (x, y))
    elif direccion == DIRECCION_IZQUIERDA and estado in[STATE_SALTANDO_UP,STATE_SALTANDO_DOWN]:
        pantalla.blit(list_jump_left[0], (x, y))
    elif direccion == DIRECCION_DERECHA and estado ==STATE_PARADO:
        pantalla.blit(list_right_stand[index_parado], (x, y))
    elif direccion == DIRECCION_IZQUIERDA and estado ==STATE_PARADO:
        pantalla.blit(list_left_stand[index_parado], (x, y))
    # pantalla.blit(list_run[6], (0, 0))

    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(FPS)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()
