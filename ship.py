import pygame

class Ship:
    def __init__(self, ss_game):
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = ss_game.screen.get_rect().midleft

        self.y = float(self.rect.y)
        self.direction = 0
    
    def update(self):
        """Update the position of the ship"""
        if self.direction:
            self.y += self.direction
            self.rect.y = self.y