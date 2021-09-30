import pygame
pygame.init()#initializes Pygame
pygame.display.set_caption("random circles")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen

while True:#GAME LOOP
    
        pygame.draw.ellipse(screen, (255,255,0), (400,400,50,50))

        pygame.display.flip()

pygame.quit()
