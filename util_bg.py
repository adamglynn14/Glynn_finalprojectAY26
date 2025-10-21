import pygame
from util_param import *


#make a tiled backgroud
water_tile_location = "Assets_and_images/PNG/Retina/Tiles/water_tile.png"
water_tile = pygame.image.load(water_tile_location)
#tile height and width
water_tile_width = water_tile.get_width()
water_tile_height = water_tile.get_height()

sand_square_tile_location = "Assets_and_images/PNG/Retina/Tiles/sand_square_tile.png"
sand_square_tile_location = pygame.image.load(sand_square_tile_location)
#get the tile width, height

sand_square_tile_width = water_tile.get_width()
sand_square_tile_height = water_tile.get_height()

#make a new surface, background, with the same w,h as screen
background = pygame.Surface((WIDTH, HEIGHT))

#loop over the background and place tiles on it
for x in range(0,WIDTH,water_tile_width):
    for y in range(0,HEIGHT, water_tile_height):
        background.blit(water_tile, (x,y))

