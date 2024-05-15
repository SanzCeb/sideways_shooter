import pytest
from mocks import mock_sideways_shooter

@pytest.fixture
def alien(mock_sideways_shooter):
    return mock_sideways_shooter.aliens.sprites()[0]

def test_alien_goes_up_and_down(mock_sideways_shooter, alien):
    alien.rect.center = mock_sideways_shooter.screen.get_rect().center

    init_pos = (alien.rect.x, alien.rect.y)

    mock_sideways_shooter.settings.fleet_direction = 1
    alien.update()
    assert init_pos[0] == alien.rect.x
    assert init_pos[1] < alien.rect.y

    mock_sideways_shooter.settings.fleet_direction = -1
    alien.update()
    assert init_pos[0] == alien.rect.x
    assert init_pos[1] == alien.rect.y


def test_alien_check_edges(mock_sideways_shooter, alien):
    mock_sideways_shooter.settings.fleet_speed = 100_000
    screen_height = mock_sideways_shooter.settings.screen_height

    alien.update()
    assert alien.rect.bottom <= screen_height

    mock_sideways_shooter.settings.fleet_direction *= -1
    alien.update()
    assert alien.rect.top >= 0