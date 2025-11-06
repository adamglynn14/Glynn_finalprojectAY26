import pygame
from util_param import *

class Pot_Text():
    def __int__(self):
        #loads the font
        self.title_font = pygame.font.Font('Assets_and_images/fonts/28-days-later/28 Days Later.ttf', 150)
        self.black = (255,255,255)

        #make the text surface
        self.title_surface = self.title_font.render('Potential/n Happiness', 1, self.black)
        self.title_rect = self.title_surface.get_rect()
        self.title_rect.center = (WIDTH//2, HEIGHT//2)
        self.birth_time = pygame.time.get_ticks()
        self.death_time = 2000

    def update(self):
        # adjust the alpha based on the age of our text
        current_age = pygame.time.get_ticks() - self.birth_time
        current_age_percent = current_age/self.death_time
        # set the correct alpha
        self.title_surface.set_alpha(255 - current_age_percent * 255)


    def draw(self, screen):
        screen.blit(self.title_surface, self.title_rect)
