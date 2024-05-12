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
    