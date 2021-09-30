import random
import pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("matrix rainbow barf")
clock = pygame.time.Clock()

# Create a 2 dimensional array. A two dimensional array is simply a list of lists.
grid = []
for i in range(10):
    # Add an empty array that will hold each cell in this row
    grid.append([])
    for j in range(10):
        grid[i].append(0)  # Append a cell
 

GameLoop = True #variable to run game loop

# GAME LOOP-----------------------------------------------------------
while GameLoop:
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            GameLoop = False 
    clock.tick(60)
    
    # Draw the grid
    for i in range(10):
        for j in range(10):
            pygame.draw.rect(screen,(random.randrange(0,255), 255, 255),[10 * j, 10* i, 10, 10])
 
    pygame.display.flip()
    
#END GAME LOOP---------------------------------------------------------
pygame.quit()
