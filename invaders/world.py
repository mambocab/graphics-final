from alienfield import AlienField

class World():
    def __init__(self):
        self.alien_field = AlienField()
        self._updatables = (self.alien_field,)

    def update(self):
        for x in self._updatables:
            x.update()
