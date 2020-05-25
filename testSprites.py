""" 
 Mostramos como usar un sprite respaldado por un gráfico.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Vídeo explicativo: http://youtu.be/vRB_983kUMc
"""

import pygame
import Toads_pygame


# Definimos algunos colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)

#VEL_CORRER_X = 1.675 * FACTOR_SCALADO
CORRIENDO = 1
#VEL_SALTO_X = 1.312 * FACTOR_SCALADO
#VEL_SALTO_Y = 4.87 * FACTOR_SCALADO
#DESACEL_Y = 0.25 * FACTOR_SCALADO
LIM_MENOR_ACEL_Y = -12
#LIM_MEN_SALTO = 1.183 * FACTOR_SCALADO
LIM_ACEL_SIN_SALTO_PRECIONADO = 2.12


FPS = 120
pygame.init()

# Establecemos las dimensiones de la pantalla [largo,altura]
dimensiones = [1700,500]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Mi Primer juego en Informática")
hecho = False

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
pygame.key.set_repeat(1, 1)
cantidad_ticks_desde_posible_doble = 0
derecha_presionada = False
izquierda_presionada = False
posible_doble_izquierdo = False
posible_doble_derecho = False

KEY_DERECHA = pygame.K_l
KEY_IZQUIERDA = pygame.K_j

cantidad_elementos = 0
lista_movimientos = []
pygame.key.set_repeat(0)
pygame.joystick.init()
print("Cantidad de Joysticks: {}".format(pygame.joystick.get_count()))
if pygame.joystick.get_count() > 0:
    joy = pygame.joystick.Joystick(0)
    joy.init()
    print("Nombre: {}".format(joy.get_name()))
toad = Toads_pygame.Toad()


# -------- Bucle principal del Programa -----------
while not hecho:
    # --- Bucle principal de eventos
    #lista = pygame.key.get_pressed()

    #for evento in pygame.event.get():
    evento = pygame.event.poll()
    if evento.type == pygame.QUIT:
        hecho = True
    toad.update(evento)

    pantalla.fill(ROJO)
    # pantalla.blit(fondo,(0,0))
    # index = int(i)%len(list_left_run)

    pantalla.blit(toad.cur_texture, toad.pos)

    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(FPS)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()
