import pygame
from util_param import *

class Pot_Text():
    def __init__(self):
        # load up a font
        self.title_font = pygame.font.Font('Assets_and_images/fonts/28-days-later/28 Days Later.ttf', 100)

        self.black = (0, 0, 0)
        # make a CHOMP surface
        self.title_surface = self.title_font.render('Potential Happiness', 1, self.black)
        self.title_rect = self.title_surface.get_rect()
        self.title_rect.center = (WIDTH//2, HEIGHT//5)
        self.birth_time = pygame.time.get_ticks()
        self.death_time = 2000

        # make a score font / surface
        self.score_font = pygame.font.Font('Assets_and_images/fonts/28-days-later/28 Days Later.ttf', 40)
        self.black = (0,0,0)
        self.score_surface = self.score_font.render('0',1,self.black)

    def update_score(self, score):
        self.score_surface = self.score_font.render(f"{score}",1,self.black)

    def update(self):
        # adjust the alpha based on the age of our text
        current_age = pygame.time.get_ticks() - self.birth_time
        current_age_percent = current_age/self.death_time
        # set the correct alpha
        self.title_surface.set_alpha(255 - current_age_percent * 255)


    def draw(self, screen):
        screen.blit(self.title_surface, self.title_rect)
        screen.blit(self.score_surface, (WIDTH - 50, 30))
