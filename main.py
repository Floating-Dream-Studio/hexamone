import pygame
from pygame.locals import*
from variables import*

#test
print(player.hexamone.spells['a'])
# player.attack('e', pnj)
# print(pnj.hexamone.hp)
# -->

pygame.init()


screen = pygame.display.set_mode((800, 600))

game = True

while game:
    
    for e in pygame.event.get():
        
        if e.type == KEYDOWN:

            if e.key == K_q:
                player.attack('a', pnj)

            if e.key == K_w:
                player.attack('z', pnj)

            if e.key == K_e:
                player.attack('e', pnj)
                
            if e.key == K_r:
                player.attack('r', pnj)

        #exit game
        if e.type == QUIT:
            pygame.quit()
            quit()

    ehp = myfont.render(str(pnj.hexamone.hp), 1, (255, 0, 0))
    php = myfont.render(str(player.hexamone.hp), 1, (255, 0, 0))

    screen.blit(bg, (0, 0))
    screen.blit(ui, (0, 0))
    screen.blit(ehp, (400, 0))
    screen.blit(php, (365, 480))
    pygame.display.flip();
