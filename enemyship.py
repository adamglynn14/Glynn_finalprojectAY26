import pygame
import pygame
from util_param import *
import math
from random import randint

class Enemyship(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.vx = randint(-4,-1)
        self.vy = randint(-2,2)
        self.x = WIDTH+100
        self.y = randint(0,HEIGHT)
        self.image = pygame.image.load('Assets_and_images/PNG/Retina/Ships/crossbones.png')
        self.image =  pygame.transform.flip(self.image, 1, 0)
        self.image = pygame.transform.rotozoom(self.image, 0, 0.4)
        self.rect = self.image.get_rect()
        self.theta = 0 # angle to player in radians
        self.speed = randint(1, 2)  # speed to follow player
        self.player = player
    
    def get_theta(self):
        # calculate the theta in radians to the player
        delta_x = self.player.x - self.x
        delta_y = (self.player.y - self.y)

        # take atan2
        self.theta = math.atan2(delta_y , delta_x)


    def update(self):
        # update the theta
        self.get_theta()

        # update the position of the ship
        self.x += self.vx
        self.y += self.vy

        # update the speed of the ship
        self.vx = self.speed * math.cos(self.theta)
        self.vy = self.speed * math.sin(self.theta)

        # update the rect
        self.rect.center = (self.x, self.y)
    

    def draw(self, screen):
        screen.blit(self.image, self.rect)