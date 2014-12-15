from worlddatatypes import Velocity, Position2
from enum import Enum, unique

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
        pass

    def update(self):

        old_pos = self.position

        if len(self.actions) == 0:
            return

        if Actions.shoot in self.actions:
            bpos = Position2(self.position.x, self.position.y - .2)
            self.world.add_bullet(bpos, 'player')

        if Actions.left in self.actions:
            self.position = Position2(
                self._clip_x(self.position.x - self.move_amount),
                self.position.y)

        if Actions.right in self.actions:
            self.position = Position2(
                self._clip_x(self.position.x + self.move_amount),
                self.position.y)

        self.actions = set()
