from worlddatatypes import Velocity, Position2, Owner
import collections
import sys
from utils import tuple_replace


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

        self.alien_height = 1
        self.alien_width = 1.2

        self._just_moved_down = False

    def positions(self, include_empties=False):
        for row_i, row in enumerate(self.field):
            for a_i, a in enumerate(row):
                if self.field[row_i][a_i] or include_empties:
                    yield Position2(
                        self.position.x + (1 + self.dist_between) * a_i,
                        self.position.y + (1 + self.dist_between / 2) * row_i)


    @property
    def right(self):
        return self.position.x + self.width
    @property
    def left(self):
        return self.position.x

    def delete_alien_at(self, row, col):
        new_row = tuple_replace(self.field[row],
                        col,
                        False)
        self.field = tuple_replace(self.field, row, new_row)

    def collide(self, bullet):
        bullet_x_compensate = .7
        bullet_y_compensate = 1

        for i, p in enumerate(self.positions(include_empties=True)):
            # calculate bounding box
            if (p.x < bullet.position.x + bullet_x_compensate < p.x + self.alien_width
                and p.y < bullet.position.y + bullet_y_compensate < p.y + self.alien_height):
                # if the bullet is from the player
                if bullet.owner is Owner.player:
                    # get the current alien's position in the array
                    row, col = i // len(self.field[0]), i % len(self.field[0])
                    print(i, row, col, sep=':', end='\t')
                    print(Position2(bullet.position.x + bullet_x_compensate,
                                    bullet.position.y + bullet_y_compensate),
                          p)
                    # if that alien exists
                    if self.field[row][col]:
                        # delete that alien
                        self.delete_alien_at(row, col)
                        return True

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
