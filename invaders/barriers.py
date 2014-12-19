from worlddatatypes import Position2, Owner
from utils import collides, tuple_replace


class Barriers():
    def __init__(self):
        self.field = tuple(4 for _ in range(3))
        self._gap = 4
        self.position = Position2(2, 12)

    def positions(self, with_strength=False):
        for i, b in enumerate(self.field):
            if b:
                p = Position2(self.position.x + i * (4 + self._gap),
                              self.position.y)
                if with_strength:
                    yield p, b
                else:
                    yield p

    def collide(self, bullet):
        for i, p in enumerate(self.positions()):
            if self.field[i]:
                if (collides(bullet, p, (-1.05, 1.05), (0, 1))):
                    if bullet.owner is Owner.aliens:
                        self.field = tuple_replace(self.field,
                                                   i,
                                                   self.field[i] - 1)
                    return True
