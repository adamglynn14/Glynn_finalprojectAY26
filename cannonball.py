import pygame
from util_param import *
import math

class Cannonball(pygame.sprite.Sprite):
        def __init__(self, player):
            super().__init__()
            self.cballimage = pygame.image.load("Assets_and_images/PNG/Retina/Ship parts/cannonBall.png")
            self.cballimage = pygame.transform.rotozoom(self.cballimage, 0, 0.4)
            self.rect = self.image.get_rect(center=(x, y))
            self.speed = 2
            self.direction_vector = 
            self.velocity = direction_vector.normalize() * self.speed # Normalize for consistent speed
        
        def update(self):
            self.rect.x += self.velocity.x
            self.rect.y += self.velocity.y


