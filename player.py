import pygame
from util_param import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x = WIDTH, y= HEIGHT):
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

    def check_event(self, event):
        #give the player a position and speed
        player_pos = pygame.Vector2(400, 300)
        player_speed = 5
        #make a mouse position
        mouse_pos = pygame.mouse.get_pos()
        #make a direction vector
        direction_vector = (pygame.Vector2(mouse_pos) - player_pos)
        # pass an event and check for mouse movement
        if direction_vector.length() > 0:
            direction_vector.normalize_ip()
            vel = (direction_vector * player_speed)
            player_pos += vel

    def draw(self, screen):
        # blit our ship to the screen
        screen.blit(self.image, self.rect)