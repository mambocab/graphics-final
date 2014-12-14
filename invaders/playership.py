from worlddatatypes import Velocity, Position2
from enum import Enum, unique

@unique
class Actions(Enum):
    left = 0
    right = 1
    shoot = 2


class Player():
    def __init__(self):
        self.position = Position2(0, 8)
        self.actions = set()

        self.move_amount = 5


    def receive_up(self):
        print(self, 'up')
        self.actions.add(Actions.shoot)

    def receive_left(self):
        print(self, 'left')
        self.actions.add(Actions.left)

    def receive_right(self):
        print(self, 'right')
        self.actions.add(Actions.right)

    def update(self):

        old_pos = self.position

        if len(self.actions) == 0:
            return

        if Actions.shoot in self.actions:
            pass
            # self.shoot()

        if Actions.left in self.actions:
            self.position = Position2(self.position.x - self.move_amount,
                                      self.position.y)

        if Actions.right in self.actions:
            self.position = Position2(self.position.x + self.move_amount,
                                      self.position.y)

        if old_pos is not self.position:
            print(self.position.x)

        self.actions = set()
