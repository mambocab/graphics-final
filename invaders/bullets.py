from worlddatatypes import Velocity, Position2
from collections import namedtuple
from enum import Enum

class Owner(Enum):
    player = 1
    aliens = 2

Bullet = namedtuple('Bullet', ('position', 'owner'))

_velocity = .5
_update_table = {Owner.player: -_velocity, Owner.aliens: _velocity}

class Bullets():
    def __init__(self):
        self.bullets = set()

    def add(self, pos, owner):
        self.bullets.add(Bullet(position=pos, owner=Owner[owner]))

    def update(self):
        new_bullets = set()
        for b in self.bullets:
            if -2 < b.position.y < 18:
                new_pos = Position2(b.position.x,
                                    b.position.y + _update_table[b.owner])
                new_bullets.add(Bullet(position=new_pos, owner=b.owner))
        self.bullets = new_bullets

        print(self.bullets)

    def bullet_positions(self):
        for b in self.bullets:
            yield b.position


