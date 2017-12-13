""" 
 Mostramos como usar un sprite respaldado por un gráfico.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Vídeo explicativo: http://youtu.be/vRB_983kUMc
"""

import pygame

def addImage(lista,imagen,x1, y1,x2,y2):
    img1 = pygame.Surface((x2-x1+1, y2-y1+1))
    img1.blit(imagen, (0, 0), (x1, y1, x2-x1+1, y2-y1+1))
    img1.set_colorkey((0, 255, 0))
    img1 = img1.convert_alpha()
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

# Se usa para establecer cuan rápido se actualiza la pantalla

megaman = pygame.image.load("sprites runs.png").convert_alpha()
list_run = []

# addImage(list_run,megaman,344,427,424,564)
# addImage(list_run,megaman,427,423,520,564)
# addImage(list_run,megaman,526,432,659,565)
# addImage(list_run,megaman,685,429,774,566)
# addImage(list_run,megaman,780,428,879,569)
# addImage(list_run,megaman,889,433,1024,565)

#
# addImage(list_run,megaman,0,0,61,101)
# addImage(list_run,megaman,0,0,61,101)
# addImage(list_run,megaman,0,0,61,101)
# addImage(list_run,megaman,74,0,144,104)
# addImage(list_run,megaman,74,0,144,104)
# addImage(list_run,megaman,74,0,144,104)
# addImage(list_run,megaman,164,0,261,104)
# addImage(list_run,megaman,164,0,261,104)
# addImage(list_run,megaman,164,0,261,104)
# addImage(list_run,megaman,164,0,261,104)
# addImage(list_run,megaman,284,0,387,104)
# addImage(list_run,megaman,284,0,387,104)
# addImage(list_run,megaman,284,0,387,104)
# addImage(list_run,megaman,419,0,498,104)
# addImage(list_run,megaman,419,0,498,104)
# addImage(list_run,megaman,419,0,498,104)
# addImage(list_run,megaman,515,0,582,104)
# addImage(list_run,megaman,515,0,582,104)
# addImage(list_run,megaman,515,0,582,104)
# addImage(list_run,megaman,593,0,669,104)
# addImage(list_run,megaman,593,0,669,104)
# addImage(list_run,megaman,593,0,669,104)
# addImage(list_run,megaman,689,0,780,104)
# addImage(list_run,megaman,689,0,780,104)
# addImage(list_run,megaman,689,0,780,104)
# addImage(list_run,megaman,803,0,906,104)
# addImage(list_run,megaman,803,0,906,104)
# addImage(list_run,megaman,803,0,906,104)
# addImage(list_run,megaman,926,0,1013,104)
# addImage(list_run,megaman,926,0,1013,104)
# addImage(list_run,megaman,926,0,1013,104)


addImage(list_run,megaman,0,0,61,101)
addImage(list_run,megaman,74,0,144,104)
addImage(list_run,megaman,164,0,261,104)
addImage(list_run,megaman,284,0,387,104)
addImage(list_run,megaman,419,0,498,104)
addImage(list_run,megaman,515,0,582,104)
addImage(list_run,megaman,593,0,669,104)
addImage(list_run,megaman,689,0,780,104)
addImage(list_run,megaman,803,0,906,104)
addImage(list_run,megaman,926,0,1013,104)


reloj = pygame.time.Clock()

i=0
delta =  2*len(list_run)/ FPS
print(delta)
# -------- Bucle principal del Programa -----------
while not hecho:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ

    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ

    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima 
    # de esto, de otra forma serán borrados por este comando:

    pantalla.fill(BLANCO)
    index = int(i)%len(list_run)
    pantalla.blit(list_run[index], (0, 0))
    # pantalla.blit(list_run[6], (0, 0))
    i+=delta
    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(FPS)

# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()
