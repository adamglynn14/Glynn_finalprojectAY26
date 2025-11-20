import pygame
from util_param import *
import math
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, enemy_group, x = 50, y= HEIGHT//5):
        pygame.sprite.Sprite.__init__(self) # init the sprite class
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.enemy_group = enemy_group
        self.base1_image = pygame.image.load('Assets_and_images/PNG/Retina/Ships/bluehorseship.png')
        # do any resize here
        self.base_image = pygame.transform.rotozoom(self.base1_image, 0, 0.4) 
        self.rect = self.base_image.get_rect()
        self.theta=0 # rad
        self.score = 0
        self.cball_x = x
        self.cball_y = y
        self.cball_vx = 0
        self.cball_vy = 0

        self.cball_surface = pygame.image.load("Assets_and_images/PNG/Retina/Ship parts/cannonBall.png")
        self.cball_surface = pygame.transform.rotozoom(self.cball_surface, 0, 0.4)

    def get_theta(self):
        # get our theta based on our vx and vy
        self.theta = math.atan2(self.vx,self.vy)
    
    def reset_bullet(self):
        # put the bullet back on the center of the player
        self.bullet_x = self.x
        self.bullet_y = self.y
    

    def update(self):
        #initial position vector for ship
        self.x += self.vx
        self.y += self.vy

        self.cball_vx = self.vx
        self.cball_vy = self.vy 

        #initial position vector of cannonball
        self.cball_x += self.cball_vx
        self.cball_y += self.cball_vy

        # update the rect for ship
        self.rect.center = (self.x, self.y)




        #update the theta value
        self.get_theta()

        # check for a ship collision
        colliding_enemy = pygame.sprite.spritecollide(self, self.enemy_group,0)
        # check for a collision
        if colliding_enemy:
            #self.hit_sound.play()
            self.score -= 50
            # move the collided to right of screen
            for f in colliding_enemy:
                f.x = WIDTH + 100
                f.y = randint(0,HEIGHT)

    
    


    def check_event(self, event):
        # pass an event and check for key moves
        if event.type == pygame.KEYDOWN:
            # we got a keydown event
            # check and see if it was W key
            if event.key == pygame.K_w:
                self.vy += -1
                # player goes up
            # check and see if it was a S key
            if event.key == pygame.K_s:
                # player goes down
                self.vy  += 1
            # move left and right
            if event.key == pygame.K_a:
                # player goes back
                self.vx += -1
            if event.key == pygame.K_d:
                # player goes forward
                self.vx += 1
            if event.key == pygame.K_t:
                # player goes forward
                self.vx *= 0.3
            if event.key == pygame.K_t:
                # player goes forward
                self.vy *= 0.3
            if event.key == pygame.K_SPACE:
                #bullet shoots
                self.cball_vx += 2
                self.cball_vy += 2


    def draw(self, screen):
        if self.theta>math.pi or self.theta <-math.pi:
            self.image = pygame.transform.flip(self.base_image,0,1)
        else:
            self.image = self.base_image

        # blit our ship to the screen
        self.image = pygame.transform.rotozoom(self.image, math.degrees(self.theta),1)
        self.rect = self.image.get_rect(center=self.rect.center)
        screen.blit(self.image, self.rect)
        screen.blit(self.cball_surface, (self.cball_x, self.cball_y))