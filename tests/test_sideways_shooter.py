import math

import pygame

from mocks import mock_sideways_shooter
from pygame.event import Event

from alien import Alien

def test_ship_init_position(mock_sideways_shooter):
    ship_rect = mock_sideways_shooter.ship.rect
    screen_rect = mock_sideways_shooter.screen.get_rect()
    assert ship_rect.midleft == screen_rect.midleft

def test_remove_bullet(mock_sideways_shooter):
    """Test that a bullet that goes off the screen is removed"""
    screen_width = mock_sideways_shooter.settings.screen_width
    mock_sideways_shooter.settings.bullet_speed = screen_width * 2

    keydown_space = Event(pygame.KEYDOWN, key=pygame.K_SPACE)
    mock_sideways_shooter._check_keydown_events(keydown_space)
    assert mock_sideways_shooter.bullets.sprites()
    mock_sideways_shooter._update_bullets()
    assert not mock_sideways_shooter.bullets.sprites()

def test_create_fleet(mock_sideways_shooter):
    """Test that the aliens created are the number expected"""
    alien = Alien(mock_sideways_shooter)
    screen_width, screen_height = mock_sideways_shooter.screen.get_rect().size
    
    game_width = screen_width - alien.rect.width
    game_height = screen_height - alien.rect.height

    num_aliens_row = int (game_width / (alien.rect.width * 2))
    num_aliens_col = int (game_height / (alien.rect.height * 2))
    num_aliens = num_aliens_row * num_aliens_col

    mock_sideways_shooter.aliens.empty()
    mock_sideways_shooter._create_fleet()

    assert len(mock_sideways_shooter.aliens) == num_aliens
    
def test_randomize_fleet(mock_sideways_shooter):

    # Cleaning the initial aliens will avoid side effects
    mock_sideways_shooter.aliens.empty()    
    mock_sideways_shooter._create_fleet()

    expected_num_aliens = round(
        len(mock_sideways_shooter.aliens)
          * mock_sideways_shooter.settings.fleet_density)
    
    mock_sideways_shooter._randomize_fleet()

    assert len(mock_sideways_shooter.aliens) == expected_num_aliens

def test_randomize_empty_fleet(mock_sideways_shooter):
    mock_sideways_shooter.aliens.empty()
    mock_sideways_shooter._randomize_fleet()
    assert not mock_sideways_shooter.aliens

def test_fleet_moves_toward_ship(mock_sideways_shooter):
    alien = mock_sideways_shooter.aliens.sprites()[0]
    previousx = alien.rect.x
    fleet_sideway_speed = mock_sideways_shooter.settings.fleet_sideway_speed
    mock_sideways_shooter.settings.fleet_speed = 100_000

    mock_sideways_shooter._update_fleet()
    
    assert alien.rect.x == (previousx - fleet_sideway_speed)
