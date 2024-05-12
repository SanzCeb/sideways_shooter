import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from bullet import Bullet
class SidewaysShooter:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        self.settings = Settings(self)
        self.ship = Ship(self)
        self.bullets = Group()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.ship.direction = 0

    def _check_keydown_events(self, event):
        """Handle game's behaviour when a key is pressed"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.ship.direction = -1
        elif event.key == pygame.K_DOWN:
            self.ship.direction = 1
        elif event.key == pygame.K_SPACE:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.ship.image, self.ship.rect)
        for bullet in self.bullets:
            bullet.draw()
        pygame.display.flip()

if __name__ == '__main__':
    SidewaysShooter().run_game()