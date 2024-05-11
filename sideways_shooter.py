import sys

import pygame

from ship import Ship
class SidewaysShooter:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 800), vsync=60)
        self.bg_color = (230, 230, 230)
        self.ship = Ship(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.screen.blit(self.ship.image, self.ship.rect)
            pygame.display.flip()

if __name__ == '__main__':
    SidewaysShooter().run_game()