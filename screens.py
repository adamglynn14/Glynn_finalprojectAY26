import pygame
from button import *
from util_param import *

class Screen():
    def __init__(self):
        self.title_font = pygame.font.Font('Assets_and_images/fonts/28-days-later/28 Days Later.ttf', 100)
        self.go_bg = pygame.image.load('Assets_and_images/gove_overbg.jpg')
        self.introbg = pygame.image.load('Assets_and_images\introbg.jpg')
        self.black = (0, 0, 0)
        self.red = (255,0,0)

    def new(self):
        self.playing = 1

    def game_over(self):
            text = self.title_font.render("Game Over", 1, self.red)
            text_rect = text.get_rect(center = (WIDTH/2, HEIGHT/2))

            restart_button = Button(10, -60, 120,- 50, self.red, self.black, "Restart", 32)

            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = 0
                    
                mouse_pos = pygame.mouse.get_pos()
                mouse_pressed = pygame.mouse.get_pressed()

                if restart_button.is_pressed(mouse_pos, mouse_pressed):
                    self.new()
                
                
                self.screen.blit(self.go_bg, (0,0))
                self.screen.blit(text, text_rect)
                self.screen.blit(restart_button.image, restart_button.rect)
                pygame.display.update()

    def intro(self, title_button_rect):
        intro = 1
        title_button = self.title_font.render('Potential Happiness', 1, self.black)
        title_button_rect = title_button.get_rect(x=10, y=10)

        play_button = Button(10, 50, 100, 50, (255,255,255),(0,0,0), "Play", 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = 0
            self.screen.blit(self.introbg, (0,0))
            self.screen.blit(title_button, title_button_rect)
            self.screen.blit(play_button.image, play_button.rect)
            pygame.display.update()