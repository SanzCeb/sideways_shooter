import pytest
from mocks import mock_sideways_shooter

@pytest.fixture
def alien(mock_sideways_shooter):
    return mock_sideways_shooter.aliens.sprites()[0]

def test_alien_goes_up_and_down(mock_sideways_shooter, alien):
    """Test alien's vertical movement in sideways shooter."""
    
    # Center the alien
    alien.rect.center = mock_sideways_shooter.screen.get_rect().center
    init_pos = (alien.rect.x, alien.rect.y)

    # Test the alien moves downwards
    mock_sideways_shooter.settings.fleet_direction = 1
    alien.update()
    assert init_pos[0] == alien.rect.x
    assert init_pos[1] < alien.rect.y

    # Test the alien moves upwards
    mock_sideways_shooter.settings.fleet_direction = -1
    alien.update()
    assert init_pos[0] == alien.rect.x
    assert init_pos[1] == alien.rect.y


def test_alien_check_edges(mock_sideways_shooter, alien):
    """Test the alien's edge checking in sideways shooter."""
    assert not alien.check_edges()

    # Try forcing the fleet off the screen
    mock_sideways_shooter.settings.fleet_speed = 100_000
    alien.update()
    assert alien.check_edges()

    # Try the same with the opposite edge
    mock_sideways_shooter.settings.fleet_direction *= -1
    alien.update()
    alien.update()
    
    assert alien.check_edges()