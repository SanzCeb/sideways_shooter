import pygame

class Ship:
    def __init__(self, ss_game):
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = ss_game.screen.get_rect().midleft

        self.y = float(self.rect.y)
    
    def move_up(self):
        self.y -= 1
        self.rect.y = self.y
    
    def move_down(self):
        self.y += 1
        self.rect.y = self.y