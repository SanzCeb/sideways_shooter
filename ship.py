import pygame

class Ship:
    """Represent the player's ship in Sideways Shooter."""
    def __init__(self, ss_game):
        self.screen = ss_game.screen
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
    
    def draw(self):
        """Draw the ship on the screen"""
        self.screen.blit(self.image, self.rect)