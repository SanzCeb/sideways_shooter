import sys
from random import randint

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
class SidewaysShooter:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        self.settings = Settings(self)
        self.ship = Ship(self)
        self.bullets = Group()
        self.aliens = Group()

        self._create_fleet()
        self._randomize_fleet()

    
    def _create_fleet(self):
        """Create the aliens at the start of the game."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien_x, alien_y = 2 * alien_width, alien_height

        while alien_x < (self.settings.screen_width - alien_width):
            while alien_y < (self.settings.screen_height - alien_height):
                new_alien = Alien(self, alien_x, alien_y)
                self.aliens.add(new_alien)
                alien_y += alien_height * 2
            alien_x += alien_width * 2
            alien_y = alien_height
        

    def _randomize_fleet(self):
        aliens_to_remove = round(
            len(self.aliens) * (1 - self.settings.fleet_density))
        while aliens_to_remove:
            index_to_remove = randint(0, len(self.aliens) - 1)
            alien_to_remove = self.aliens.sprites()[index_to_remove]
            self.aliens.remove(alien_to_remove)
            aliens_to_remove -= 1

    def run_game(self):
        """Run the main loop of the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _update_bullets(self):
        """Move the bullets and remove them if they are off the game"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)

    def _check_events(self):
        """Check the game events"""
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
        """Draw the new status of the objects on the screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.draw()        
        self._draw_bullets()
        self._draw_aliens()
        pygame.display.flip()

    def _draw_aliens(self):
        for alien in self.aliens:
            alien.draw()

    def _draw_bullets(self):
        for bullet in self.bullets:
            bullet.draw()

if __name__ == '__main__':
    SidewaysShooter().run_game()