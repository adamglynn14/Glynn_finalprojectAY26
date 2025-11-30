import pygame
from util_param import *
from pygame.sprite import Sprite
from settings import *

class Cannonball(Sprite):
        """Class for the cannonball"""
        def __init__(self, game):
            """creates a cannonball at player ships position"""
            super().__init__()
            self.screen = game.screen
            self.settings = game.settings
            self.cballimage = pygame.image.load("Assets_and_images/PNG/Retina/Ship parts/cannonBall.png")
            self.cballimage = pygame.transform.rotozoom(self.cballimage, 0, 0.4)

            #creates a cannomnball rect at (0,0) and then sets position
            self.rect = pygame.Rect(0,0, self.cballimage)           

            #store cannonballs positon as a decimal
            self.y = float(self.rect.y)
            self.x = float(self.rect.x)
        
        def update(self):
            """moves the cannonball"""
            #update the decimal positon of cannonball
            self.y -= 1
            self.x -= 1
            #update rect position
            self.rect.y = self.y
            self.rect.x = self.x

        def draw_cannonball(self):
            """draw cannonball to screen"""
            pygame.draw.rect(self.screen, self.cballimage, self.rect)
            


