import pygame
from util_param import *
import math
from random import randint


#make a wind function that will control the direction the ship moves in
def wind_dir():
        y = randint(-360, 360)
        x = randint(-360,360)

        angle_radians = math.atan2(y, x)
        angle_degrees = math.degrees(angle_radians)
        deg = angle_degrees

        return int(deg)

print(wind_dir())

