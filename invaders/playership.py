from worlddatatypes import Position2, Owner
from enum import Enum, unique
import audio
from utils import collides


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
        self.actions.add(Actions.shoot)

    def receive_left(self):
        self.actions.add(Actions.left)

    def receive_right(self):
        self.actions.add(Actions.right)

    def _clip_x(self, x):
        return min(max(x, 0), 20)

    def collide(self, bullet):
        if collides(bullet, self.position, (-1.05, 1.05), (0, 1)):
            if bullet.owner is Owner.aliens:
                self.world.player_hit()
                return True

    def update(self):

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
