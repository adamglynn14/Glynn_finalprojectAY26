import pygame
from util_param import *
import math

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


    def check_mouse(self,):
        #gets the mouse positon and makes player follow
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.rel_x, self.rel_y = self.mouse_x - self.x, self.mouse_y - self.y
        angle_radians = math.atan2(self.rel_y, self.rel_x)
        angle_degrees = math.degrees(angle_radians)
        rotated_image =  pygame.transform.rotate(self.image, -angle_degrees) 
        new_rect = rotated_image.get_rect(center=self.rect.center)
        self.image = rotated_image
        self.rect = new_rect



    def draw(self, screen):
        # blit our ship to the screen
        screen.blit(self.image, self.rect)