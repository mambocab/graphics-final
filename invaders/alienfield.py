from worlddatatypes import Velocity, Position2
import collections
import sys


def _clip_velocity(x):
    max_magnitude = .3
    return min(max_magnitude, max(-max_magnitude, x))

def moves_printer(s, _d=collections.Counter()):
    _d += {s: 1}

    print('{} ({})'.format(s, _d[s]))


class AlienField():
    def __init__(self):
        field_width = 7
        field_height = 5
        self.field = tuple(tuple(True for _ in range(field_width))
                           for _ in range(field_height))

        self.dist_between = .7

        self.width = field_width + (self.dist_between * (field_width - 1))
        self.position = Position2(0, 0)
        self.velocity = Velocity(.05, 0)

        self._just_moved_down = False

    def alien_positions(self):
        for row_i, row in enumerate(self.field):
            for a_i, a in enumerate(row):
                if self.field[row_i][a_i]:
                    yield Position2(
                        self.position.x + (1 + self.dist_between) * a_i,
                        self.position.y + (1 + self.dist_between / 2) * row_i)


    @property
    def right(self):
        return self.position.x + self.width
    @property
    def left(self):
        return self.position.x

    def detect(self):
        pass


    def update(self):
        # detect side collision
        # print('right:', self.right, 'left:', self.left)
        if (self.right >= 20 or self.left <= 0) and not self._just_moved_down:
            self.velocity = Velocity(_clip_velocity(-self.velocity.x * 1.2),
                                     self.velocity.y)
            self.position = Position2(self.position.x,
                                      self.position.y + .04)
            self._just_moved_down = True
        else:
            # moves_printer('moving!')
            self.position = Position2(self.position.x + self.velocity.x,
                                      self.position.y)
            self._just_moved_down = False
