from alienfield import AlienField
from barriers import Barriers

class World():
    def __init__(self):
        self.alien_field = AlienField()
        self.barriers = Barriers()
        self._updatables = (self.alien_field,)

    def update(self):
        for x in self._updatables:
            x.update()
