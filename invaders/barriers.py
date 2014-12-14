from worlddatatypes import Position2

class Barriers():
    def __init__(self):
        self.field = tuple(4 for _ in range(3))
        self._gap = 4
        self.position = Position2(2, 12)

    def __iter__(self):
        for i, b in enumerate(self.field):
            if b:
                yield Position2(self.position.x + i * (4 + self._gap),
                                self.position.y)

