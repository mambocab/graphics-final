from collections import namedtuple
from enum import Enum

Velocity = namedtuple('Velocity', ('x', 'y'))
PositionBase = namedtuple('Position2', ('x', 'y'))

class Position2(PositionBase):
    def __new__(cls, x, y):
        return super(Position2, cls).__new__(cls, x, y)

class Owner(Enum):
    player = 1
    aliens = 2
