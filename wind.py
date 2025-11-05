import pygame
from util_param import *
import math
from random import randint


#make a wind function that will control the direction the ship moves in
def wind_dir(self, x, y):
        self.deg = deg
        self.x = x
        self.y = y
        y = int(randint(0, 3.14))
        x = int(randint(0,3.14))

        angle_radians = math.atan2(y, x)
        angle_degrees = math.degrees(angle_radians)
        deg = angle_degrees

        return deg