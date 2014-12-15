from worlddatatypes import Velocity, Position2, Owner
from collections import namedtuple
from enum import Enum

Bullet = namedtuple('Bullet', ('position', 'owner'))

_velocity = .5
_update_table = {Owner.player: -_velocity, Owner.aliens: _velocity}

class Bullets():
    def __init__(self):
        self.bullets = set()

    def add(self, pos, owner):
        self.bullets.add(Bullet(position=pos, owner=Owner[owner]))


    def __isub__(self, bullet_set):
        self.bullets = self.bullets - bullet_set
        return self

    def update(self):
        new_bullets = set()
        for b in self.bullets:
            if -2 < b.position.y < 18:
                new_pos = Position2(b.position.x,
                                    b.position.y + _update_table[b.owner])
                new_bullets.add(Bullet(position=new_pos, owner=b.owner))
        self.bullets = new_bullets

        # if self.bullets:
        #     print(self.bullets)

    def positions(self):
        for b in self.bullets:
            yield b.position

    def remove(self, bullet):
        self.bullets.remove(bullet)

    def __iter__(self):
        return self.bullets.__iter__()


