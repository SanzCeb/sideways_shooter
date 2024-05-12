import pytest
import pygame

from sideways_shooter import SidewaysShooter

@pytest.fixture
def mock_sideways_shooter(mocker):
    """Mocks the window and initializes the game"""
    _mock_window(mocker)
    return SidewaysShooter()


def _mock_window(mocker):
    mock_surface = _mock_surface(mocker)
    mocker.patch('pygame.display.flip')
    mock_set_mode = mocker.patch('pygame.display.set_mode')
    mock_set_mode.return_value = mock_surface

def _mock_surface(mocker):
    mock_surface = mocker.Mock()
    mock_surface.get_size.return_value = (1200, 800)
    mock_surface.get_rect.return_value = pygame.Rect(0, 0, 1200, 800)
    mock_surface.fill.return_value = mocker.Mock()
    mock_surface.blit.return_value = mocker.Mock()
    return mock_surface