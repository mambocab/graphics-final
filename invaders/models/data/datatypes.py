from collections import namedtuple

ModelBase = namedtuple('ModelBase', 
                       ('vertices', 'faces', 'triangles', 'material'))

class Model(ModelBase):
    def __new__(cls, vertices, faces, material):
        triangles = tuple(tuple(vertices[v - 1] for v in f) for f in faces)
        return super(Model, cls).__new__(cls,
                                         vertices=vertices,
                                         faces=faces,
                                         triangles=triangles,
                                         material=material)

    def __iter__(self):
        return self.faces.__iter__()

    def __len__(self):
        return len(self.faces)

Color = namedtuple('Color', ('r', 'g', 'b'))

Material = namedtuple('Material',
                      ('Ns', 'Ka', 'Kd', 'Ks', 'Ni', 'd', 'illum'))
