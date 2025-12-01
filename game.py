# Example file showing a basic pygame "game loop"
import pygame
from util_bg import make_background
from util_param import *
from player import Player
from Potential_h import Pot_Text
from enemyship import *
from loot import Loot
from random import randint
from time import sleep
#from gameover import Over_Text

# pygame setup
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))   
clock = pygame.time.Clock()
running = True

background = make_background()

#make an enemy group and a loot group
enemy_group = pygame.sprite.Group()
loot_group = pygame.sprite.Group()

#make some loot
for i in range(15):
    #make loot and add to the group
    loot_group.add(Loot(randint(0,WIDTH), randint(20,HEIGHT)))

#make a player 
player = Player(loot_group, enemy_group, background)


#make enemy ships
num_enemies = 3
for i in range(num_enemies):
    enemy_group.add(Enemyship(player))



#make the title
title = Pot_Text()
#agameover = Over_Text()
################# TESTING ZONE ###################################





################################################################
screen_num = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # pass the event to our player
        player.check_event(event)
        
        # check for the p button to take a screenshot
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_p:
                pygame.image.save(screen,f"screenshot_{screen_num}.png")
                screen_num +=1
                print("Took a screenshot!")
   

    #update the things
    player.update()
    enemy_group.update()
    loot_group.update()

    #blit the background to our screen
    screen.blit(background,(0,0))

    #draw the title 
    title.update()
    title.update_score(player.score)
    title.draw(screen)



    # draw player
    player.draw(screen)
    #draw enemy ships
    for e in enemy_group:
        e.draw(screen)
    #draw the loot
    for l in loot_group:
        l.draw(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit