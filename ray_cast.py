import pygame, sys
from pygame.locals import *

pygame.init()

width, height = 640, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("")

colours = {
    'background': (0, 0, 0),
}

# VARIABLES

def setup():
    global finished
    finished = False

setup()

while True:
    if not finished:
        screen.fill(colours['background'])

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    pygame.display.update()
