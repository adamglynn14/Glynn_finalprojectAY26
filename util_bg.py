import pygame
from util_param import *

def make_background():
    #make a tiled backgroud
    water_tile_location = "Assets_and_images/PNG/Retina/Tiles/water_tile.png"
    water_tile = pygame.image.load(water_tile_location)
    #tile height and width
    water_tile_width = water_tile.get_width()
    water_tile_height = water_tile.get_height()

    sand_square_tile_location = "Assets_and_images/PNG/Retina/Tiles/clear_sand.png"
    sand_square_tile = pygame.image.load(sand_square_tile_location)
    scaled_sand_square_tile = pygame.transform.rotozoom(sand_square_tile, 0, 0.2)

    #get the tile width, height
    sand_square_tile_width = scaled_sand_square_tile.get_width()
    sand_square_tile_height = scaled_sand_square_tile.get_height()

    #make a new surface, background, with the same w,h as screen
    background = pygame.Surface((WIDTH, HEIGHT))

    #loop over the background and place water tiles on it
    for x in range(0,WIDTH,water_tile_width):
        for y in range(0,HEIGHT, water_tile_height):
            background.blit(water_tile, (x,y))

    #place sand on the bottom row
    y_sands = HEIGHT - sand_square_tile_height
    for x in range(0,WIDTH,sand_square_tile_width):
        #blit the sand tile
        background.blit(scaled_sand_square_tile,(x,y_sands))

    #place sand on the top row
    for x in range(0,WIDTH,sand_square_tile_width):
        #blit the sand tile
        background.blit(scaled_sand_square_tile,(x,0))

    #place sand in the edge row
    x_sand = WIDTH - sand_square_tile_width
    for y in range(0, HEIGHT, sand_square_tile_height):
        #blit the sand background
        background.blit(scaled_sand_square_tile, (x_sand, y))

    #make a circle of in the middle with grass on the side

    #make a tiled backgroud
    SGulc_tile_location = "Assets_and_images/PNG/Retina/Tiles/sand_grassulc.png"
    SGulc_tile = pygame.image.load(SGulc_tile_location)
    #tile height and width
    SGulc_tile_width = SGulc_tile.get_width()
    SGulc_tile_height = SGulc_tile.get_height()

    #place tile on screen
    x_ulc = 500
    y_ulc = 100 

    #make the tile smaller:
    scaled_SGulc_tile = pygame.transform.rotozoom(SGulc_tile, 0, 0.4)
    #blit the sand background
    background.blit(scaled_SGulc_tile, (x_ulc, y_ulc))

    #make a tiled backgroud
    SGurc_tile_location = "Assets_and_images/PNG/Retina/Tiles/sand_grassurc.png"
    SGurc_tile = pygame.image.load(SGurc_tile_location)
    #tile height and width
    SGurc_tile_width = SGurc_tile.get_width()
    SGurc_tile_height = SGurc_tile.get_height()

    #place tile on screen
    x_urc = 500 + SGurc_tile_width * 0.4
    y_urc = 100 

    #make the tile smaller:
    scaled_SGurc_tile = pygame.transform.rotozoom(SGurc_tile, 0, 0.4)
    #blit the sand background
    background.blit(scaled_SGurc_tile, (x_urc, y_urc))


    #make a tiled backgroud
    SGlrc_tile_location = "Assets_and_images/PNG/Retina/Tiles/sand_grasslrc.png"
    SGlrc_tile = pygame.image.load(SGlrc_tile_location)
    #tile height and width
    SGlrc_tile_width = SGlrc_tile.get_width()
    SGlrc_tile_height = SGlrc_tile.get_height()

    #place tile on screen
    x_lrc = 500 + SGlrc_tile_width * 0.4
    y_lrc = 100 + SGlrc_tile_height * 0.4

    #make the tile smaller:
    scaled_SGlrc_tile = pygame.transform.rotozoom(SGlrc_tile, 0, 0.4)

    #blit the sand background
    background.blit(scaled_SGlrc_tile, (x_lrc, y_lrc))
    

    #make a tiled backgroud
    SGllc_tile_location = "Assets_and_images/PNG/Retina/Tiles/sand_grassllc.png"
    SGllc_tile = pygame.image.load(SGllc_tile_location)
    #tile height and width
    SGllc_tile_width = SGllc_tile.get_width()
    SGllc_tile_height = SGllc_tile.get_height()

    #place tile on screen
    x_llc = 500 
    y_llc = 100 + SGllc_tile_height * 0.4

    #make the tile smaller:
    scaled_SGllc_tile = pygame.transform.rotozoom(SGllc_tile, 0, 0.4)

    #blit the sand background
    background.blit(scaled_SGllc_tile, (x_llc, y_llc))

    #make a channel 
    wavysand_location = "Assets_and_images/PNG/Retina/Tiles/wavysand.png"
    wavysand = pygame.image.load(wavysand_location)
    scaled_wavysand = pygame.transform.rotozoom(wavysand, 0, 0.2)

    ywavy = HEIGHT - 100
    for x in range(150,WIDTH - 200,sand_square_tile_width):
        #blit the sand tile
        background.blit(scaled_wavysand,(x,ywavy))
    
    #toppart of channel
    scaled2_wavysand = pygame.transform.rotozoom(wavysand, 180, 0.2)

    ywavy = HEIGHT - 150
    for x in range(150,WIDTH - 200,sand_square_tile_width):
        #blit the sand tile
        background.blit(scaled2_wavysand,(x,ywavy))


    #return background
    return background


