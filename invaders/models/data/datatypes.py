from collections import namedtuple

from OpenGL.constants import GLfloat_3 as Vec3
from OpenGL.constants import GLfloat_4 as Vec4

ColorBase = namedtuple('Color', ('r', 'g', 'b'))


class Color(ColorBase):
    @property
    def vec4(self, i=1, _cache={}):
        try:
            return _cache[i]
        except KeyError:
            _cache[i] = Vec4(self.r, self.g, self.b, i)
        return _cache[i]

MaterialBase = namedtuple('Material',
                          ('ambient', 'diffuse', 'specular',
                           'specular_exponent', 'refraction_index',
                           'dissolve', 'illum'))


class Material(MaterialBase):
    def __new__(cls, ambient, diffuse, specular, **kw):
        return super(Material, cls).__new__(cls,
                                            ambient=ambient.vec4,
                                            diffuse=diffuse.vec4,
                                            specular=specular.vec4,
                                            **kw)

ModelBase = namedtuple('ModelBase',
                       ('vertices', 'faces', 'triangles', 'material'))


class Model(ModelBase):
    def __new__(cls, vertices, faces, **kw):
        triangles = tuple(tuple(Vec3(*vertices[v - 1]) for v in f)
                          for f in faces)
        return super(Model, cls).__new__(cls,
                                         vertices=vertices,
                                         faces=faces,
                                         triangles=triangles,
                                         **kw)

    def __iter__(self):
        return self.triangles.__iter__()

    def __len__(self):
        return len(self.triangles)
