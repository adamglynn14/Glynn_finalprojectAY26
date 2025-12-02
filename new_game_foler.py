# Example file showing a basic pygame "game loop"
import pygame
from util_bg import make_background
from util_param import *
from player import Player
from Potential_h import *
from enemyship import *
from loot import Loot
from random import randint
from time import sleep
from button import Button

# pygame setup
pygame.init()

title_font = pygame.font.Font('Assets_and_images/fonts/28-days-later/28 Days Later.ttf', 100)
go_bg = pygame.image.load('Assets_and_images/gove_overbg.jpg')
introbg = pygame.image.load('Assets_and_images\introbg.jpg')
black = (0, 0, 0)
red = (255,0,0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))   
clock = pygame.time.Clock()

background = make_background()

def get_font(size):
    return pygame.font.Font("Assets_and_images/fonts/28-days-later/28 Days Later.ttf", size)

def main_menu(): #makes a main menu screen
    pygame.display.set_caption("Menu")

    while True:
        screen.blit(introbg, (0,0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("MAIN MENU", True, black)
        menu_rect = menu_text.get_rect(center = (640, 100))

        play_button = Button(image=pygame.image.load("Assets_and_images/PNG/Default/button_red.png"), pos=(640,250),
                             text_input="PLAY", font= title_font(75), color=red)

        options_button = Button(image=pygame.image.load("Assets_and_images/PNG/Default/button_grey.png"), pos=(640,400),
                             text_input="OPTIONS", font= title_font(75), color=red)

        quit_button = Button(image=pygame.image.load("Assets_and_images/PNG/Default/button_red.png"), pos=(640,550),
                             text_input="QUIT", font= title_font(75), color=red)

        screen.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_for_input(menu_mouse_pos):
                    play()
                if options_button.check_for_input(menu_mouse_pos):
                    options()
                if quit_button.check_for_input(menu_mouse_pos):
                    pygame.quit()

def options(): #makes an options screen

    pygame.display.set_caption("Options")

    while True: 
        options_mouse_pos = pygame.mouse.get_pos()

        screen.fill("white")

        options_text = get_font(45).render("This is the Options screen", True, "Black")
        options_rect = options_text.get_rect(center=(640, 260))
        screen.blit(options_text, options_rect)

        options_back = Button(image=None, pos=(640,460),
                             text_input="Back", font= get_font(75), color="Black")
        options_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_back.check_for_input(options_mouse_pos):
                    main_menu()

        pygame.display.update

def play(): #makes the play function
    pygame.display.set_caption("Play")

    running = True
    while running: 

        play_mouse_pos = pygame.mouse.get_pos()

        screen.fill("black")

        play_text = title_font.render("This is the play screen", True, "white")
        play_rect = play_text.get_rect(center=(640, 260))
        screen.blit(play_text, play_rect)

        play_back = Button(image=None, pos=(640,460),
                             text_input="Back", font= title_font(75), color="white")
        play_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.check_for_input(play_mouse_pos):
                    main_menu()



        #sets up the timer
        start_time = pygame.time.get_ticks() # Gets the time in milliseconds

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
        #sets up the timer
        current_time = pygame.time.get_ticks()
        elapsed_time_ms = current_time - start_time
        elapsed_seconds = elapsed_time_ms // 1000
        #make a timer font / surface
        timer_font = pygame.font.Font('Assets_and_images/fonts/28-days-later/28 Days Later.ttf', 30)
        #formats the timer 
        minutes = elapsed_seconds // 60
        seconds = elapsed_seconds % 60
        timer_text = f"{minutes:02d}:{seconds:02d}"
        timer_surface = timer_font.render(timer_text, 1, (0,0,0)) #black color


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
        #blit the timer to the screen
        screen.blit(timer_surface, (10, 10))
            


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

        #end the game if player score is less than zero
        #



pygame.quit