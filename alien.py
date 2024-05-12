import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Represent the enemy of Sideways Shooter"""
    def __init__(self, ss_game, rectx=0, recty=0):
        super().__init__()
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()
        
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = rectx
        self.rect.y = recty

    def draw(self):
        self.screen.blit(self.image, self.rect)
