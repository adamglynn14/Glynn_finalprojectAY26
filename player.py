import pygame
from util_param import *
import math
from random import randint
#from gameover import Over_Text

class Player(pygame.sprite.Sprite):
    def __init__(self, loot_group, enemy_group, background, x = 50, y= HEIGHT//5):
        pygame.sprite.Sprite.__init__(self) # init the sprite class
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.enemy_group = enemy_group
        self.loot_group = loot_group
        self.damagedship = pygame.transform.rotozoom(pygame.image.load("Assets_and_images/PNG/Retina/Ships/bleuhorsegone.png"),0,0.4)
        self.base1_image = pygame.image.load('Assets_and_images/PNG/Retina/Ships/bluehorseship.png')
        # do any resize here
        self.base_image = pygame.transform.rotozoom(self.base1_image, 0, 0.4) 
        self.rect = self.base_image.get_rect()
        self.theta=0 # rad
        self.score = 0
        self.background = background #lets the ship stop if it hits sand
        self.loot_sound = pygame.mixer.Sound("Assets_and_images/Audio/impactWood_light_003.ogg")
        self.ship_sound = pygame.mixer.Sound("Assets_and_images/Audio/impactMetal_light_000.ogg")



    def get_theta(self):
        # get our theta based on our vx and vy
        self.theta = math.atan2(self.vx,self.vy)
    
    def check_boundaries(self):
        # make our ship remains in boundaries
        #if self.x <0:



        # check topright of our ship
        if self.rect.top<0:
            self.vy = 0
            self.base_image = self.damagedship

        # check to make sure it only stays on water
        front_color = self.background.get_at(self.rect.bottomright)
        if front_color[2]<150: # to see if the ship is not touching blue
            self.vy = -self.vy * 0.6
            self.vx = -self.vx * 0.6
            self.base_image = self.damagedship


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

        #check for loot collisions
        colliding_loot = pygame.sprite.spritecollide(self,self.loot_group,0)
        if colliding_loot:
            #play a sound
            self.loot_sound.play()
            self.score += 20
            #randomize a new location
            for l in colliding_loot:
                l.x = randint(0,WIDTH)
                l.y = randint(20,HEIGHT)

            

        # check for a ship collision
        colliding_enemy = pygame.sprite.spritecollide(self, self.enemy_group,0)
        # check for a collision with an enemy ship
        if colliding_enemy:
            self.ship_sound.play()
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