import pygame
from util_param import *
import math
from wind import wind_dir

class Player(pygame.sprite.Sprite):
    def __init__(self, x = 100, y= HEIGHT//2):
        pygame.sprite.Sprite.__init__(self) # init the sprite class
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.image = pygame.image.load('Assets_and_images/PNG/Retina/Ships/bluehorseship.png')
        # do any resize here
        self.image = pygame.transform.rotozoom(self.image, 0, 0.4) 
        self.rect = self.image.get_rect()
        
    def update(self):
        #initial position vector
        self.x += self.vx
        self.y += self.vy
        # update the rect
        self.rect.center = (self.x, self.y)

        #make a wind vector
        if wind_dir() <= 90:
            self.vx = 1
            self.vy =1
        else:
            self.vx = -1
            self.vy = -1


    def draw(self, screen):
        # blit our ship to the screen
        screen.blit(self.image, self.rect)