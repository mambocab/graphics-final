from alienfield import AlienField
from barriers import Barriers
from playership import Player
from bullets import Bullets

import sys

class World():
    def __init__(self):
        self.alien_field = AlienField(self)
        self.player = Player(self)
        self.bullets = Bullets()
        self.barriers = Barriers()

        self._updatables = (self.alien_field,
                            self.player,
                            self.bullets)

        self._collidables = (self.alien_field, self.barriers, self.player)

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

    def receive_up(self):
        self.player.receive_up()

    def receive_left(self):
        self.player.receive_left()

    def receive_right(self):
        self.player.receive_right()

    def add_bullet(self, pos, owner):
        self.bullets.add(pos, owner)
