#cannonball file
import pygame
from player import Player
from util_bg import make_background
from util_param import *

class Cball(Player):
    #subclass of player that deals will the firing of the cannonball
    def __init__(self, x, y):
        
        self.cball_x = x
        self.cball_y = y
        self.cball_vx = 0
        self.cball_vy = 0

    
        self.cball_surface = pygame.image.load("Assets_and_images/PNG/Retina/Ship parts/cannonBall.png")
        self.cball_surface = pygame.transform.rotozoom(self.cball_surface, 0, 0.4)
