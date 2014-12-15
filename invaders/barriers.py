from worlddatatypes import Position2, Owner


def tuple_replace(t, replace_at, value):
    return tuple(value if i == replace_at else v for i, v in enumerate(t))


class Barriers():
    def __init__(self):
        self.field = tuple(4 for _ in range(3))
        self._gap = 4
        self.position = Position2(2, 12)
        self.barrier_width = 4
        self.barrier_height = 2

    def positions(self):
        for i, b in enumerate(self.field):
            if b:
                yield Position2(self.position.x + i * (4 + self._gap),
                                self.position.y)

    def collide(self, bullet):
        for i, p in enumerate(self.positions()):
            if (p.x < bullet.position.x + 2 < p.x + self.barrier_width
                and p.y < bullet.position.y + 2 < p.y + self.barrier_height):
                if bullet.owner is Owner.aliens:
                    self.field = tuple_replace(self.field,
                                               i,
                                               self.field[i] - 1)
                print('collision with barrier', i)
                return True


