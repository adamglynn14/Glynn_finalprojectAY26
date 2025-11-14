import pygame
from util_param import *
import math
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, x = 50, y= HEIGHT//5):
        pygame.sprite.Sprite.__init__(self) # init the sprite class
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.base1_image = pygame.image.load('Assets_and_images/PNG/Retina/Ships/bluehorseship.png')
        # do any resize here
        self.base_image = pygame.transform.rotozoom(self.base1_image, 0, 0.4) 
        self.rect = self.base_image.get_rect()
        self.theta=0 # rad

    def get_theta(self):
        # get our theta based on our vx and vy
        self.theta = math.atan2(self.vx,self.vy)

    def update(self):
        #initial position vector
        self.x += self.vx
        self.y += self.vy
        # update the rect
        self.rect.center = (self.x, self.y)

        #update the theta value
        self.get_theta()
    


    def check_event(self, event):
        # pass an event and check for key moves
        if event.type == pygame.KEYDOWN:
            # we got a keydown event
            # check and see if it was W key
            if event.key == pygame.K_w:
                self.vy += -0.7
                # player goes up
            # check and see if it was a S key
            if event.key == pygame.K_s:
                # player goes down
                self.vy  += 0.7
            # move left and right
            if event.key == pygame.K_a:
                # player goes back
                self.vx += -0.7
            if event.key == pygame.K_d:
                # player goes forward
                self.vx += 0.7
            if event.key == pygame.K_t:
                # player goes forward
                self.vx *= 0.3
            if event.key == pygame.K_t:
                # player goes forward
                self.vy *= 0.3


    def draw(self, screen):
        if self.theta>math.pi or self.theta <-math.pi:
            self.image = pygame.transform.flip(self.base_image,0,1)
        else:
            self.image = self.base_image

        # blit our ship to the screen
        self.image = pygame.transform.rotozoom(self.image, math.degrees(self.theta),1)
        self.rect = self.image.get_rect(center=self.rect.center)
        screen.blit(self.image, self.rect)