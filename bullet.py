import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """The bullet that the Ship fires in Sideways Shooter"""
    def __init__(self, ss_game):
        """Create a bullet as a rectangle next to the ship."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.rect = pygame.Rect(0, 0, 
                self.settings.bullet_width, self.settings.bullet_height)
        self.color = self.settings.bullet_color
        
        # Each bullet starts next to the ship
        self.rect.midleft = ss_game.ship.rect.midright
        self.x = float(self.rect.x)
    
    def update(self):
        """Make the bullet right across the screen"""
        self.x += self.settings.bullet_speed

        self.rect.x = self.x
    
    def draw(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)