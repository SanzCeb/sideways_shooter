from sideways_shooter import SidewaysShooter
from mocks import mock_sideways_shooter

def test_ship_init_position(mock_sideways_shooter):
    ship_rect = mock_sideways_shooter.ship.rect
    screen_rect = mock_sideways_shooter.screen.get_rect()
    assert ship_rect.midleft == screen_rect.midleft