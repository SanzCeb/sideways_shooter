import pygame

from mocks import mock_sideways_shooter
from pygame.event import Event

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