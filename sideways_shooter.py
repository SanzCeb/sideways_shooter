import sys

import pygame

from ship import Ship
class SidewaysShooter:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        self.bg_color = (230, 230, 230)
        self.ship = Ship(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.ship.direction = 1
                    elif event.key == pygame.K_DOWN:
                        self.ship.direction = -1
                if event.type == pygame.KEYUP:
                    self.ship.direction = 0

            self.ship.update()
            self.screen.fill(self.bg_color)
            self.screen.blit(self.ship.image, self.ship.rect)
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    SidewaysShooter().run_game()