import pytest 

from ship import Ship
from sideways_shooter import SidewaysShooter

@pytest.fixture
def ship():
    ss_game = SidewaysShooter()
    ship = Ship(ss_game)
    return ship


def test_ship_move_up(ship):
    old_pos = (ship.rect.x, ship.rect.y)
    ship.direction = -1
    ship.update()
    new_pos = (ship.rect.x, ship.rect.y)
    assert old_pos[0] == old_pos[0]
    assert old_pos[1] > new_pos[1]

def test_ship_move_down(ship):
    old_pos = (ship.rect.x, ship.rect.y)
    ship.direction = 1
    ship.update()
    new_pos = (ship.rect.x, ship.rect.y)
    assert old_pos[0] == old_pos[0]
    assert old_pos[1] < new_pos[1]
