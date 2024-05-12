import pytest
import pygame

from bullet import Bullet
from mocks import mock_sideways_shooter

def test_bullet(mock_sideways_shooter):
    """Test that the bullet moves horizontally"""
    bullet = Bullet(mock_sideways_shooter)
    old_pos = (bullet.rect.x, bullet.rect.y)
    bullet.update()
    new_pos = (bullet.rect.x, bullet.rect.y)
    assert old_pos[0] < new_pos[0]
    assert old_pos[1] == new_pos[1]