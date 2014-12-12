from .datatypes import Color, Material

vertices = ((1, 1, 1),
            (1, 1, -1),
            (1, -1, 1),
            (1, -1, -1),
            (-1, 1, 1),
            (-1, 1, -1),
            (-1, -1, 1),
            (-1, -1, -1),)


faces = ((1, 2, 3),
         (2, 3, 4),
         (3, 4, 7),
         (4, 7, 8),
         (2, 4, 8),
         (2, 6, 8),
         (5, 6, 8),
         (5, 7, 8),
         (1, 5, 7),
         (1, 3, 7),
         (1, 2, 6),
         (2, 5, 6))


material = Material(ambient=Color(r=0.000000, g=0.000000, b=0.000000),
                    diffuse=Color(r=0.000000, g=1.000000, b=0.000000),
                    specular=Color(r=0.333333, g=0.333333, b=0.333333),
                    specular_exponent=96.078431,
                    refraction_index=1.000000,
                    dissolve=1.000000,
                    illum=2)
