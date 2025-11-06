import pygame
from util_param import *
import math
import random

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


    def check_event(self, event):
        # pass an event and check for key moves
        if event.type == pygame.KEYDOWN:
            # we got a keydown event
            # check and see if it was W key
            if event.key == pygame.K_w:
                self.vy += -1
                # player goes up
            # check and see if it was a S key
            if event.key == pygame.K_s:
                # player goes down
                self.vy  += 1
            # move left and right
            if event.key == pygame.K_a:
                # player goes back
                self.vx += -1
            if event.key == pygame.K_d:
                # player goes forward
                self.vx += 1
            if event.key == pygame.K_t:
                # player goes forward
                self.vx *= 0.3
            if event.key == pygame.K_t:
                # player goes forward
                self.vy *= 0.3


    def draw(self, screen):
        # blit our ship to the screen
        screen.blit(self.image, self.rect)