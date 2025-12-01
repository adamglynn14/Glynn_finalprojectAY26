import pygame
from util_param import *
from random import randint
from random import choice

class Loot(pygame.sprite.Sprite):
    def __init__(self, x=WIDTH//2, y=HEIGHT//2):
        pygame.sprite.Sprite.__init__(self)
        self.assets = [
            "Assets_and_images/PNG/Retina/crateWood.png",
            "Assets_and_images/PNG/Retina/sandbagBrown_open.png",
            "Assets_and_images/PNG/Retina/Ship parts/nest.png",
            "Assets_and_images/PNG/Retina/sandbagBrown.png"
        ]
        self.fp = choice(self.assets)
        self.x = x
        self.y = y
        self.base1image = pygame.image.load(self.fp)
        self.image = pygame.transform.rotozoom(self.base1image, 0, 0.4) #makes the base image the smaller version
        self.rect = self.image.get_rect()
        # place the center of the rect
        self.rect.center = (x,y)
    

    def update(self):
        # update the rect
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        # blit our loot to the screen
        screen.blit(self.image, self.rect)
