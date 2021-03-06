from .datatypes import Color, Material

vertices = ((0.075533, -0.151100, 0.482581),
            (-0.347453, -0.151100, 0.000000),
            (0.075533, -0.151100, -0.482581),
            (-0.135960, -0.151100, 0.482581),
            (0.287026, -0.151100, 0.482581),
            (-0.347453, -0.151100, 0.331700),
            (0.214515, -0.151100, 0.000000),
            (-0.347453, -0.151100, -0.331700),
            (-0.135960, -0.151100, -0.482581),
            (0.287026, -0.151100, -0.482581),
            (-0.135960, -0.151100, 0.399586),
            (0.214515, -0.151100, 0.241291),
            (-0.135960, -0.151100, -0.399587),
            (0.214515, -0.151100, -0.241291),
            (0.075533, 0.151100, 0.482581),
            (-0.347453, 0.151100, 0.000000),
            (0.075533, 0.151100, -0.482581),
            (-0.135960, 0.151100, 0.482581),
            (0.287026, 0.151100, 0.482581),
            (-0.347453, 0.151100, 0.331700),
            (0.214515, 0.151100, 0.000000),
            (-0.347453, 0.151100, -0.331700),
            (-0.135960, 0.151100, -0.482581),
            (0.287026, 0.151100, -0.482581),
            (-0.135960, 0.151100, 0.399586),
            (0.214515, 0.151100, 0.241291),
            (-0.135960, 0.151100, -0.399587),
            (0.214515, 0.151100, -0.241291),)

faces = ((2, 16, 22),
         (3, 9, 23),
         (9, 13, 8),
         (23, 22, 27),
         (7, 21, 26),
         (12, 26, 19),
         (6, 11, 4),
         (20, 18, 25),
         (10, 24, 28),
         (14, 28, 21),
         (3, 14, 2),
         (2, 12, 1),
         (7, 12, 2),
         (14, 7, 2),
         (10, 14, 3),
         (9, 3, 13),
         (8, 13, 2),
         (6, 2, 11),
         (4, 11, 1),
         (1, 12, 5),
         (22, 16, 27),
         (23, 27, 17),
         (24, 17, 28),
         (15, 19, 26),
         (18, 15, 25),
         (20, 25, 16),
         (4, 1, 15),
         (10, 3, 17),
         (6, 20, 16),
         (1, 5, 19),
         (26, 21, 16),
         (28, 16, 21),
         (28, 17, 16),
         (26, 16, 15),
         (25, 15, 16),
         (16, 17, 27),
         (1, 11, 2),
         (3, 2, 13),
         (9, 8, 22),
         (18, 20, 6),
         (8, 2, 22),
         (17, 3, 23),
         (12, 7, 26),
         (5, 12, 19),
         (14, 10, 28),
         (7, 14, 21),
         (18, 4, 15),
         (24, 10, 17),
         (2, 6, 16),
         (15, 1, 19),
         (23, 9, 22),
         (4, 18, 6),)


material = Material(ambient=Color(r=0.000000, g=0.000000, b=0.000000),
                    diffuse=Color(r=1.000000, g=1.000000, b=1.000000),
                    specular=Color(r=0.333333, g=0.333333, b=0.333333),
                    specular_exponent=96.078431,
                    refraction_index=1.000000,
                    dissolve=1.000000,
                    illum=2)
