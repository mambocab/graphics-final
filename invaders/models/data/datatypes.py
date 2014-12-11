from collections import namedtuple

ModelBase = namedtuple('ModelBase', 
                       ('vertices', 'faces', 'triangles', 'material'))

Vec3 = namedtuple('Vec3', ('x', 'y', 'z'))

class Model(ModelBase):
    def __new__(cls, vertices, faces, material):
        triangles = tuple(tuple(Vec3(*vertices[v - 1]) for v in f)
                          for f in faces)
        return super(Model, cls).__new__(cls,
                                         vertices=vertices,
                                         faces=faces,
                                         triangles=triangles,
                                         material=material)

    def __iter__(self):
        return self.triangles.__iter__()

    def __len__(self):
        return len(self.triangles)

Color = namedtuple('Color', ('r', 'g', 'b'))

Material = namedtuple('Material',
                      ('ambient', 'diffuse', 'specular',
                       'specular_exponent', 'refraction_index',
                       'dissolve', 'illum'))
