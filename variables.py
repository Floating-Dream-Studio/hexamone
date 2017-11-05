import pygame
from classes import*

pygame.font.init()

bg = pygame.image.load("images/bg.png")
ui = pygame.image.load("images/ui.png")
myfont = pygame.font.SysFont('Arial', 50)

player = Player()
pnj    = Pnj()