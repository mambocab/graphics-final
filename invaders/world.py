from alienfield import AlienField
from barriers import Barriers
from playership import Player
from bullets import Bullets
from audio import you_lose, congratulations
import sys

class World():
    def __init__(self, mode='normal'):
        self.alien_field = AlienField(self)
        self.player = Player(self)
        self.bullets = Bullets()
        self.barriers = Barriers()

        self._updatables = (self.alien_field,
                            self.player,
                            self.bullets)

        self._collidables = (self.alien_field, self.barriers, self.player)

        if mode == 'easy':
            self.easy = True
        else:
            self.easy = False

    def get_collisions(self):
        to_remove = None
        for b in self.bullets:
            if to_remove is not None:
                break
            for c in self._collidables:
                if c.collide(b):
                    to_remove = b

        if to_remove is not None:
            self.bullets.remove(to_remove)
            return True
        return False

    def update(self):
        for x in self._updatables:
            x.update()

        while True:
            if not self.get_collisions():
                break

    def disable_update(self):
        self._update = self.update
        self.update = lambda: None

    def player_hit(self):
        self.disable_update()
        you_lose()

    def player_wins(self):
        self.disable_update()
        congratulations()

    def aliens_hit_barriers(self):
        self.barriers.field = (0, 0, 0)

    def receive_up(self):
        self.player.receive_up()

    def receive_left(self):
        self.player.receive_left()

    def receive_right(self):
        self.player.receive_right()

    def add_bullet(self, pos, owner):
        self.bullets.add(pos, owner)
