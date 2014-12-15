from alienfield import AlienField
from barriers import Barriers
from playership import Player
from bullets import Bullets

import sys

class World():
    def __init__(self):
        self.alien_field = AlienField()
        self.player = Player(self)
        self.bullets = Bullets()
        self.barriers = Barriers()

        self._updatables = (self.alien_field,
                            self.player,
                            self.bullets)

        self._collidables = (self.alien_field, self.barriers, self.player)

    def update(self):
        for x in self._updatables:
            x.update()

        to_remove = set()
        for b in self.bullets:
            for c in self._collidables:
                if c.collide(b):
                    to_remove.add(b)

        self.bullets -= to_remove

    def receive_up(self):
        self.player.receive_up()

    def receive_left(self):
        self.player.receive_left()

    def receive_right(self):
        self.player.receive_right()

    def add_bullet(self, pos, owner):
        self.bullets.add(pos, owner)
