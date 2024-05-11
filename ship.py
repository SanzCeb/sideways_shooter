import pygame

class Ship:
    def __init__(self, ss_game):
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = ss_game.screen.get_rect().midleft