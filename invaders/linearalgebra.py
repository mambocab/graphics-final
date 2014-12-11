from collections import namedtuple

Vec3 = namedtuple('Vec3', ('x', 'y', 'z'))
Ray = namedtuple('Ray', ('init', 'slope'))

def ray_from(a, b):
    return Ray(init=a, slope=Vec3(x=(a.x - b.x),
                                  y=(a.y - b.y),
                                  z=(a.z - b.z)))

def cross_product(a, b):
    return Vec3(x=(a.y * b.z - a.z * b.y),
                y=(a.z * b.x - a.x * b.z),
                z=(a.x * b.y - a.y * b.x))


def normal_vector(a, b, c):
    ab = ray_from(a, b)
    bc = ray_from(b, c)

    return cross_product(ab.slope, bc.slope)

