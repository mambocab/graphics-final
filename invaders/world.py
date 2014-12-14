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

    def update(self):
        for x in self._updatables:
            x.update()

    def receive_up(self):
        self.player.receive_up()

    def receive_left(self):
        self.player.receive_left()

    def receive_right(self):
        self.player.receive_right()

    def add_bullet(self, pos, owner):
        self.bullets.add(pos, owner)
