import pygame
import time
import random
from classesnfunctions import *

WIN_WIDTH = 1920
WIN_HEIGHT = 1080
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = 'red'


pygame.init()
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption('TSNM')
bg = pygame.Surface(DISPLAY)
bg.fill(BACKGROUND_COLOR)
running = True

all_sprites = pygame.sprite.Group()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, (0, 0))
    pygame.display.update()
