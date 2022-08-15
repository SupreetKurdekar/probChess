import pygame
 
from pygame.locals import (
    MOUSEBUTTONUP,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
 
pygame.init()
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))