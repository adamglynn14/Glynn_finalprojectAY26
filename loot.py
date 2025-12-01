import pygame
from util_param import *
from random import randint

class Loot(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.inventory = [] #this is an empty list to start the inventory
        self.x = x
        self.y = y
        self.base1image = pygame.image.load("Assets_and_images/PNG/Retina/Ship parts/nest.png")
        self.image = pygame.transform.rotozoom(self.base1image, 0, 0.8) #makes the base image the smaller version
        self.rect = self.image.get_rect()

    def draw(self, screen):
        # blit our loot to the screen
        self.rect = self.image.get_rect(center=self.rect.center)
        screen.blit(self.image, self.rect)
