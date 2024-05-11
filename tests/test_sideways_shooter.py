from sideways_shooter import SidewaysShooter

def test_ship_init_position():
    ss_game = SidewaysShooter()
    ship_rect = ss_game.ship.rect
    screen_rect = ss_game.screen.get_rect()
    assert ship_rect.midleft == screen_rect.midleft