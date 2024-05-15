import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Represent the enemy of Sideways Shooter"""
    def __init__(self, ss_game, rectx=0, recty=0):
        super().__init__()
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ss_game.settings
        
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.x = rectx
        self.rect.y = recty

    
    def update(self):
        """Move the alien toward the ship"""
        self.rect.y += int(self.settings.fleet_direction 
                        * self.settings.fleet_speed)
    
    def check_edges(self):
        """Return true if the alien is off the screen."""
        return (self.rect.bottom >= self.settings.screen_height or 
                self.rect.top <= 0)

    def draw(self):
        self.screen.blit(self.image, self.rect)
