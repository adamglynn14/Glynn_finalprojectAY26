# Example file showing a basic pygame "game loop"
import pygame
from util_bg import make_background
from util_param import *
from player import Player

# pygame setup
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))   
clock = pygame.time.Clock()
running = True

background = make_background()

################# TESTING ZONE ###################################




#make a player 
player = Player()

################################################################

#blit the background to our screen
screen.blit(background,(0,0))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    #update the things
    player.update()

    #blit the background to our screen
    screen.blit(background,(0,0))

    # draw player
    player.draw(screen)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()