import pygame
from util_param import *
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, x = WIDTH, y= HEIGHT):
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


    def check_mouse(self):
        #gets the mouse positon and makes player follow
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.vx = int(self.mouse_x)
        self.vy = int(self.mouse_y)



    def draw(self, screen):
        # blit our ship to the screen
        screen.blit(self.image, self.rect)