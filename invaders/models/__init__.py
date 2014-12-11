from .data import datatypes
from .data.datatypes import Model
from .data import alien1

__all__ = ('ALIEN_1', 'datatypes')

ALIEN_1 = Model(vertices=alien1.vertices,
                faces=alien1.faces,
                material=alien1.material)
