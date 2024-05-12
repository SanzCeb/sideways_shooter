import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Represent the enemy of Sideways Shooter"""
    def __init__(self, ss_game):
        super().__init__()
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()
        
        self.image = pygame.image.load('images/alien.bmp')
        self.image_rect = self.image.get_rect()
        
        self.image_rect.center = self.screen_rect.center

    def draw(self):
        self.screen.blit(self.image, self.image_rect)
