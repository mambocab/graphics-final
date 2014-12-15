from worlddatatypes import Velocity, Position2, Owner
from enum import Enum, unique
import audio

@unique
class Actions(Enum):
    left = 0
    right = 1
    shoot = 2

class Player():
    def __init__(self, world):
        self.position = Position2(0, 15)
        self.actions = set()

        self.world = world
        self.move_amount = 1

    def receive_up(self):
        # print(self, 'up')
        self.actions.add(Actions.shoot)

    def receive_left(self):
        # print(self, 'left')
        self.actions.add(Actions.left)

    def receive_right(self):
        # print(self, 'right')
        self.actions.add(Actions.right)

    def _clip_x(self, x):
        # print('clipping {}'.format(x))
        return min(max(x, 0), 20)


    def collide(self, bullet):
        p = self.position
        if (p.x - 1.05 < bullet.position.x < p.x + 1.05
            and p.y < bullet.position.y < p.y + 1):
            if bullet.owner is Owner.aliens:
                self.world.player_hit()
                return True


    def update(self):

        old_pos = self.position

        if len(self.actions) == 0:
            return

        if Actions.shoot in self.actions:
            bpos = Position2(self.position.x, self.position.y - .2)
            self.world.add_bullet(bpos, 'player')
            audio.player_fire()

        if Actions.left in self.actions:
            self.position = Position2(
                self._clip_x(self.position.x - self.move_amount),
                self.position.y)

        if Actions.right in self.actions:
            self.position = Position2(
                self._clip_x(self.position.x + self.move_amount),
                self.position.y)

        self.actions = set()
