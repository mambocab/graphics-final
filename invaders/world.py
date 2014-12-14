from alienfield import AlienField
from barriers import Barriers
from playership import Player

class World():
    def __init__(self):
        self.alien_field = AlienField()
        self.player = Player()

        self.barriers = Barriers()
        self._updatables = (self.alien_field, self.player)

    def update(self):
        for x in self._updatables:
            x.update()

    def receive_up(self):
        print(self, 'up')
        self.player.receive_up()

    def receive_left(self):
        print(self, 'left')
        self.player.receive_left()

    def receive_right(self):
        print(self, 'right')
        self.player.receive_right()
