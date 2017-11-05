import pygame
from classes import*

pygame.font.init()
myfont = pygame.font.SysFont('Arial', 50)

bg = pygame.image.load("images/bg.png")
ui = pygame.image.load("images/ui.png")

player = Player()
pnj    = Pnj()