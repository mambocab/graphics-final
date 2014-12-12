from worlddatatypes import Velocity, Position2


def _clip_velocity(x):
    max_magnitude = .3
    return min(max_magnitude, max(-max_magnitude, x))


class AlienField():
    def __init__(self):
        field_width = 11
        field_height = 5
        self.field = tuple(tuple(True for _ in range(field_width))
                           for _ in range(field_height))

        self.width = .4
        self.position = Position2(0, 0)
        self.velocity = Velocity(-.009, 0)


        self._just_moved_down = False


    @property
    def right(self):
        return self.position.x + self.width
    @property
    def left(self):
        return self.position.x


    def update(self):
        # detect side collision
        if (self.right >= 1 or self.left <= 0) and not self._just_moved_down:
            self.velocity = Velocity(_clip_velocity(-self.velocity.x * 1.2),
                                     self.velocity.y)
            self.position = Position2(self.position.x,
                                      self.position.y + .05)
            self._just_moved_down = True
        else:
            self.position = Position2(self.position.x + self.velocity.x,
                                      self.position.y)
            self._just_moved_down = False
