# code.Pylet - Scrolling Background Image
# watch the video here - https://youtu.be/US3HSusUBeI
# Any questions? Just ask!

import pygame
from pygame.locals import *
import sys
import os


def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


# define display surface
W, H = 576*2, 1024
HW, HH = W , H
AREA = W * H

os.environ['SDL_VIDEO_WINDOW_POS'] = "1150,50"

# setup pygame
pygame.init()
CLOCK = pygame.time.Clock()
# flags = pygame.OPENGL
# DS = pygame.display.set_mode((W, H), flags, vsync=1)
DS = pygame.display.set_mode((W, H))

pygame.display.set_caption("code.Pylet - Scrolling Background Image")
FPS = 144


#bkgd = pygame.transform.scale(pygame.image.load("mountains.png").convert(), (910, 1024//2))
bkgd = pygame.image.load("mountains.png").convert()

x = 0

mod = bkgd.get_rect().width

# main loop
while True:
    events()

    rel_x = x % mod
    DS.fill((255,255,255))
    DS.blit(bkgd, (rel_x - mod, 0))
    if rel_x < W:
        DS.blit(bkgd, (rel_x, 0))
    x -= 1.4
    # pygame.draw.line(DS, (255, 0, 0), (rel_x, 0), (rel_x, H), 3)

    pygame.display.update()
    CLOCK.tick(FPS)