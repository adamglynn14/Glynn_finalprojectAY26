import pygame
import pygame
from util_param import *
import math
import random

class Enemyship(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.vx = random.uniform(-4,-1)
        self.vy = random.uniform(-2,2)
        self.x = WIDTH+100
        self.y = random.uniform(0,HEIGHT)
        self.base1_image = pygame.image.load('Assets_and_images/PNG/Retina/Ships/crossbones.png')
        self.image = pygame.transform.rotozoom(self.base1_image, 90, 0.4) #makes the base image the smaller version
        self.rect = self.image.get_rect()
        self.theta = 0 # angle to player in radians
        self.speed = random.uniform(1, 2)  # speed to follow player
        self.player = player
    
    def get_theta(self):
        # calculate the theta in radians to the player
        delta_x = self.player.x - self.x
        delta_y = (self.player.y - self.y)

        # take atan2
        self.theta = math.atan2(delta_y , delta_x)



    def update(self):

        # update the position of the ship
        self.x += self.vx
        self.y += self.vy

        # update the speed of the ship
        self.vx = self.speed * math.cos(self.theta)
        self.vy = self.speed * math.sin(self.theta)

        # update the rect
        self.rect.center = (self.x, self.y)
    
        # update the theta
        self.get_theta()

    def draw(self, screen):
        #if self.theta>math.pi or self.theta <-math.pi:
            #self.image1 = pygame.transform.flip(self.image,0,1)
        #else:
           #self.image1 = self.image

        # blit our ship to the screen
        self.image2 = pygame.transform.rotozoom(self.image, math.degrees(-self.theta),1)
        self.rect = self.image2.get_rect(center=self.rect.center)
        screen.blit(self.image2, self.rect)