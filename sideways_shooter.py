import sys

import pygame

from settings import Settings
from ship import Ship
class SidewaysShooter:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        self.settings = Settings(self)
        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self.ship.direction = 0

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.direction = -1
        elif event.key == pygame.K_DOWN:
            self.ship.direction = 1
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.ship.image, self.ship.rect)
        pygame.display.flip()

if __name__ == '__main__':
    SidewaysShooter().run_game()