import sys
from time import sleep
from random import randint

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
class SidewaysShooter:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        self.settings = Settings(self)
        self.game_stats = GameStats()
        self.ship = Ship(self)
        self.bullets = Group()
        self.aliens = Group()


        self.game_active = False
        self.play_button = Button(self, "Play")

    def _create_random_fleet(self):
        """Sets a fleet on aliens placed in random positions"""
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

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_fleet()

            self._update_screen()
            self.clock.tick(60)
    
    def _update_fleet(self):
        """Move the aliens towards the ship"""
        for alien in self.aliens:
            alien.update()
            if alien.check_edges():
                self.settings.fleet_direction *= -1
                for alien in self.aliens:
                    alien.rect.x -= self.settings.fleet_sideway_speed
                break
        
        self._check_ship_hit()

    def _check_ship_hit(self):
        """Reset the game if the ship is hit. The game is over
        when the ship is hit three times."""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.game_stats.ship_hit +=1
            self.bullets.empty()
            self.aliens.empty()
            self._create_random_fleet()
            sleep(0.5)        
        if self.game_stats.ship_hit > 3:
            self.game_active = False
            pygame.mouse.set_visible(True)


    def _update_bullets(self):
        """Move the bullets and remove them if they are off the game"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
        
        # Make aliens and bullets dissaper when both collide
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Check whether bullets and aliens have collided and act upon it."""
        pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            self.bullets.empty()
            self._create_random_fleet()
            self.settings.increase_speed()


    def _check_events(self):
        """Check the game events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.ship.direction = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings()
            self.game_stats.reset_stats()
            self.game_active = True

            self.bullets.empty()
            self.aliens.empty()

            self._create_random_fleet()
            self.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Handle game's behaviour when a key is pressed"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self.ship.direction = -1
        elif event.key == pygame.K_DOWN:
            self.ship.direction = 1
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def center_ship(self):
        """Center the ship on the screen."""
        self.ship.rect.midleft = self.screen.get_rect().midleft
    
    def _update_screen(self):
        """Draw the new status of the objects on the screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.draw()        
        self._draw_bullets()
        self._draw_aliens()

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _draw_aliens(self):
        for alien in self.aliens:
            alien.draw()

    def _draw_bullets(self):
        for bullet in self.bullets:
            bullet.draw()

if __name__ == '__main__':
    SidewaysShooter().run_game()