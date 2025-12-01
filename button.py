import pygame

class Button:
    def __init__(self, x, y, width, height, fg, bg, words, size):
        self.font = pygame.font.Font('Assets_and_images/fonts/28-days-later/28 Days Later.ttf', 20)
        self.words = words
        self.x = x
        self.y = y 
        self.width = 40
        self.height = 20
        self.fg = fg
        self.bg = bg
        self.size = size

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.words, 1, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return 1
            return 0
        return 0
    
    