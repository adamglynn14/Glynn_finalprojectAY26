import pygame
from util_param import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x=WIDTH*0.1, y=HEIGHT/2):
        pygame.sprite.Sprite.__init__(self) # init the sprite class
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.image = pygame.image.load('Assets_and_images/PNG/Retina/Ships/bluehorseship.png')
        # do any resize here
        self.image = pygame.transform.rotozoom(self.image, 0, 1.2)
        self.rect = self.image.get_rect()
        self.score = 0

    def update(self):
        self.x += self.vx
        self.y += self.vy
        # update the rect
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        # blit our ship to the screen
        screen.blit(self.image, self.rect)