from worlddatatypes import Velocity, Position2, Owner
import collections
import sys
from utils import tuple_replace
import time
from random import choice, random
from audio import alien_down, alien_fire


def _clip_velocity(x):
    max_magnitude = .3
    return min(max_magnitude, max(-max_magnitude, x))


def moves_printer(s, _d=collections.Counter()):
    _d += {s: 1}

    print('{} ({})'.format(s, _d[s]))


class AlienField():
    def __init__(self, world):
        field_width = 7
        field_height = 5
        self.field = tuple(tuple(True for _ in range(field_width))
                           for _ in range(field_height))
        self.remaining = field_width * field_height

        self.dist_between = .7

        self.width = field_width + (self.dist_between * (field_width - 1))
        self.position = Position2(0, 0)
        self.velocity = Velocity(.05, 0)

        self.alien_height = 1
        self.alien_width = 1.2

        self._just_moved_down = True
        self.last_shot_time = time.time()

        self.world = world

    def position_at(self, row, col):
        return Position2(self.position.x + (1 + self.dist_between) * col,
                         self.position.y + (1 + self.dist_between / 2) * row)

    def positions(self, include_empties=False):
        for row_i, row in enumerate(self.field):
            for a_i, a in enumerate(row):
                if self.field[row_i][a_i] or include_empties:
                    yield self.position_at(row_i, a_i)

    @property
    def right(self):
        rightmost = max(x for x in range(len(self.field[0]))
                        if any(self.field[n][x] for n in range(len(self.field))))
        return self.position_at(0, rightmost).x
    @property
    def left(self):
        leftmost = min(x for x in range(len(self.field[0]))
                       if any(self.field[n][x] for n in range(len(self.field))))
        return self.position_at(0, leftmost).x

    def delete_alien_at(self, row, col):
        new_row = tuple_replace(self.field[row],
                        col,
                        False)
        self.field = tuple_replace(self.field, row, new_row)
        self.remaining -= 1
        alien_down()

    def collide(self, bullet):
        bullet_x_compensate = .7
        bullet_y_compensate = 1

        if bullet.owner is Owner.aliens:
            return False

        for i, p in enumerate(self.positions(include_empties=True)):
            # calculate bounding box
            if (p.x < bullet.position.x + bullet_x_compensate < p.x + self.alien_width
                and p.y < bullet.position.y + bullet_y_compensate < p.y + self.alien_height):
                # get the current alien's position in the array
                row, col = i // len(self.field[0]), i % len(self.field[0])
                # print(i, row, col, sep=':', end='\t')
                # print(Position2(bullet.position.x + bullet_x_compensate,
                #                 bullet.position.y + bullet_y_compensate),
                #       p)
                # if that alien exists
                if self.field[row][col]:
                    # delete that alien
                    self.delete_alien_at(row, col)
                    return True

    def maybe_shoot(self):
        if self.world.mode == 'easy':
            return
        if time.time() - self.last_shot_time < 1 and (not self.world.mode == 'hard'):
            return
        if random() < (1 / 10) if self.world.mode == 'hard' else (1 / 40):
            self.world.add_bullet(choice(list(self.positions())), 'aliens')
            self.last_shot_time = time.time()
            # print('shot')
            alien_fire()

    def last_valid_row(self):
        for i, row in enumerate(reversed(self.field)):
            if any(row):
                return len(self.field) - i
        return False

    def update(self):

        if self.remaining <= 0:
            self.world.player_wins()

        # detect side collision
        if (self.right >= 20 or self.left <= 0) and not self._just_moved_down:
            self.velocity = Velocity(_clip_velocity(-self.velocity.x * 1.1),
                                     self.velocity.y)
            self.position = Position2(self.position.x,
                                      self.position.y + .5)

            print(self.last_valid_row())
            print(self.position_at(self.last_valid_row(), 0))

            if self.position_at(self.last_valid_row(), 0).y > 12:
                self.world.aliens_hit_barriers()

            if self.position_at(self.last_valid_row(), 0).y > 15:
                self.world.player_hit()

            self._just_moved_down = True
        else:
            self.position = Position2(self.position.x + self.velocity.x,
                                      self.position.y)
            self._just_moved_down = False

        self.maybe_shoot()
