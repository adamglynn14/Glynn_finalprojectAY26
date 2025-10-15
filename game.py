# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()

#make screen properties
WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))   
clock = pygame.time.Clock()
running = True

################# TESTING ZONE ###################################

#make a tiled backgroud
water_tile_location = "Assets_and_images/PNG/Retina/Tiles/water_tile.png"
water_tile = pygame.image.load(water_tile_location)

# - gotta find a tile first (sand_tile = "Assets_and_images/PNG/Retina/Tiles/sand_tile.png")
# sand_tile_location = pygame.image.load(sand_tile_location)
#get the tile width, height


tile_width = water_tile.get_width()
tile_height = water_tile.get_height()

#make a new surface, background, with the same w,h as screen
background = pygame.Surface((WIDTH, HEIGHT))

#loop over the background and place tiles on it
for x in range(0,WIDTH,tile_width):
    for y in range(0,HEIGHT, tile_height):
        background.blit(water_tile, (x,y))


#make a row of sand
## y_sand = HEIGHT - tile_height
## for x in range(0, WIDTH, tile_width):
    #blit the sane tile
    # background.blit(sand_tile(x,y_sand))

#### random row of seaweed NOT FOR MY GAME
#### num_seaweed = 8
#### for i in range(num_seaweed)
    # x = randint(0,WIDTH)
    # y = HEIGHT - tile_height
    # background.blit(seaweed_tile,(x,y))




#blit the background to our screen
screen.blit(background,(0,0))


################################################################

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()