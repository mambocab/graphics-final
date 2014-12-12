from collections import namedtuple

Velocity = namedtuple('Velocity', ('x', 'y'))
PositionBase = namedtuple('Position2', ('x', 'y'))

class Position2(PositionBase):
    def __new__(cls, x, y):
        return super(Position2, cls).__new__(cls,
                                             x=cls._clip(x),
                                             y=cls._clip(y))

    def _clip(x):
        return min(1, max(x, 0))

