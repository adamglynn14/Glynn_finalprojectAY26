import pygame
from util_param import *
import math
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self, enemy_group, background, x = 50, y= HEIGHT//5):
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
        self.background = background #lets the ship stop if it hits sand


    def get_theta(self):
        # get our theta based on our vx and vy
        self.theta = math.atan2(self.vx,self.vy)
    
    def check_boundaries(self):
        # make our ship remains in boundaries
        y_bounds = (0,HEIGHT)
        x_bounds = (0,WIDTH)

        # check topright of our ship
        if self.rect.top<0 or self.rect.right>WIDTH:
            self.vy = 0
            self.base_image = pygame.transform.rotozoom(pygame.image.load("Assets_and_images/PNG/Retina/Ships/bleuhorsegone.png"),0,0.4)

        # check to make sure it only stays on water
        front_color = self.background.get_at(self.rect.bottomright)
        if front_color[2]<200: # if not blue
            self.vy=0
            self.vx =0
            self.rect.bottom = self.rect.bottom -10


    def update(self):
        #initial position vector for ship
        self.x += self.vx
        self.y += self.vy

        # update the rect for ship
        self.rect.center = (self.x, self.y)

        #check for boundary collisons
        self.check_boundaries()

        #update the theta value
        self.get_theta()

        # check for a ship collision
        colliding_enemy = pygame.sprite.spritecollide(self, self.enemy_group,0)
        # check for a collision with an enemy ship
        if colliding_enemy:
            #self.hit_sound.play()
            self.score -= 50
            # move the collided to right of screen to avoid constant collison
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



    def draw(self, screen):
        #update the rotation on the image to face direction travelling
        if self.theta>math.pi or self.theta <-math.pi:
            self.image = pygame.transform.flip(self.base_image,0,1)
        else:
            self.image = self.base_image

        # blit our ship to the screen
        self.image = pygame.transform.rotozoom(self.image, math.degrees(self.theta),1)
        self.rect = self.image.get_rect(center=self.rect.center)
        screen.blit(self.image, self.rect)