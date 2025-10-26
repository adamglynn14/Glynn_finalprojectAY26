import pygame
from util_param import *

def make_background():
    #make a tiled backgroud
    water_tile_location = "Assets_and_images/PNG/Retina/Tiles/water_tile.png"
    water_tile = pygame.image.load(water_tile_location)
    #tile height and width
    water_tile_width = water_tile.get_width()
    water_tile_height = water_tile.get_height()

    sand_square_tile_location = "Assets_and_images/PNG/Retina/Tiles/sand_square_tile.png"
    sand_square_tile = pygame.image.load(sand_square_tile_location)
    scaled_sand_square_tile = pygame.transform.rotozoom(sand_square_tile, 0, 0.2)

    #get the tile width, height
    sand_square_tile_width = scaled_sand_square_tile.get_width()
    sand_square_tile_height = scaled_sand_square_tile.get_height()

    #make a new surface, background, with the same w,h as screen
    background = pygame.Surface((WIDTH, HEIGHT))

    #loop over the background and place tiles on it
    for x in range(0,WIDTH,water_tile_width):
        for y in range(0,HEIGHT, water_tile_height):
            background.blit(water_tile, (x,y))


    y = (0, HEIGHT, sand_square_tile_height)
    for x in range(0,WIDTH,sand_square_tile_width):
        background.blit(scaled_sand_square_tile, (x,y))

    #return background
    return background


