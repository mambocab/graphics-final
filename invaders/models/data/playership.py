from .datatypes import Color, Material

vertices = ((-0.436981, -1.383279, 5.778708),
            (1.341083, -1.383279, 5.778708),
            (-3.993109, -1.383279, 0.444516),
            (-2.215045, -1.383279, -1.333548),
            (-0.436981, -1.383279, -4.889676),
            (0.452051, -1.383279, 5.778708),
            (2.230115, -1.383279, 5.778708),
            (-0.436981, -1.383279, 4.889676),
            (-1.326013, -1.383279, 4.000644),
            (2.230115, -1.383279, 4.000644),
            (-1.326013, -1.383279, 2.222580),
            (2.230115, -1.383279, 2.222580),
            (-2.215045, -1.383279, 1.333548),
            (-3.104077, -1.383279, 0.444516),
            (2.230115, -1.383279, 0.444516),
            (-3.993109, -1.383279, -0.444516),
            (-3.104077, -1.383279, -1.333548),
            (-1.326013, -1.383279, -1.333548),
            (2.230115, -1.383279, -1.333548),
            (-1.326013, -1.383279, -3.111612),
            (2.230115, -1.383279, -3.111612),
            (-1.326013, -1.383279, -4.889676),
            (2.230115, -1.383279, -4.889676),
            (-0.436981, -1.383279, -5.778708),
            (1.341083, -1.383279, -5.778708),
            (-1.326013, -1.383279, 4.889676),
            (2.230115, -1.383279, 4.889676),
            (-1.326013, -1.383279, 3.111612),
            (2.230115, -1.383279, 3.111612),
            (-3.104077, -1.383279, 1.333548),
            (-1.326013, -1.383279, 1.333548),
            (2.230115, -1.383279, 1.333548),
            (-3.104077, -1.383279, -0.444516),
            (2.230115, -1.383279, -0.444516),
            (-1.326013, -1.383279, -2.222580),
            (2.230115, -1.383279, -2.222580),
            (-1.326013, -1.383279, -4.000644),
            (2.230115, -1.383279, -4.000644),
            (0.452051, -1.383279, -5.778708),
            (2.230115, -1.383279, -5.778708),
            (-0.436981, 0.709375, 5.778708),
            (1.341083, 0.709375, 5.778708),
            (-0.436981, 0.709375, 4.000644),
            (1.341083, 0.709375, 4.000644),
            (-0.436981, 0.709375, 2.222580),
            (1.341083, 0.709375, 2.222580),
            (-3.993109, 0.709375, 0.444516),
            (-2.215045, 0.709375, 0.444516),
            (-0.436981, 0.709375, 0.444516),
            (1.341083, 0.709375, 0.444516),
            (-2.215045, 0.709375, -1.333548),
            (-0.436981, 0.709375, -1.333548),
            (1.341083, 0.709375, -1.333548),
            (-0.436981, 0.709375, -3.111612),
            (1.341083, 0.709375, -3.111612),
            (-0.436981, 0.709375, -4.889676),
            (1.341083, 0.709375, -4.889676),
            (0.452051, 0.709375, 5.778708),
            (2.230115, 0.709375, 5.778708),
            (-0.436981, 0.709375, 4.889676),
            (-1.326013, 0.709375, 4.000644),
            (1.341083, 0.709375, 4.889676),
            (0.452051, 0.709375, 4.000644),
            (2.230115, 0.709375, 4.000644),
            (-0.436981, 0.709375, 3.111612),
            (-1.326013, 0.709375, 2.222580),
            (1.341083, 0.709375, 3.111612),
            (0.452051, 0.709375, 2.222580),
            (2.230115, 0.709375, 2.222580),
            (-2.215045, 0.709375, 1.333548),
            (-3.104077, 0.709375, 0.444516),
            (-0.436981, 0.709375, 1.333548),
            (-1.326013, 0.709375, 0.444516),
            (1.341083, 0.709375, 1.333548),
            (0.452051, 0.709375, 0.444516),
            (2.230115, 0.709375, 0.444516),
            (-3.993109, 0.709375, -0.444516),
            (-2.215045, 0.709375, -0.444516),
            (-3.104077, 0.709375, -1.333548),
            (-0.436981, 0.709375, -0.444516),
            (-1.326013, 0.709375, -1.333548),
            (1.341083, 0.709375, -0.444516),
            (0.452051, 0.709375, -1.333548),
            (2.230115, 0.709375, -1.333548),
            (-0.436981, 0.709375, -2.222580),
            (-1.326013, 0.709375, -3.111612),
            (1.341083, 0.709375, -2.222580),
            (0.452051, 0.709375, -3.111612),
            (2.230115, 0.709375, -3.111612),
            (-0.436981, 0.709375, -4.000644),
            (-1.326013, 0.709375, -4.889676),
            (1.341083, 0.709375, -4.000644),
            (0.452051, 0.709375, -4.889676),
            (2.230115, 0.709375, -4.889676),
            (-0.436981, 0.709375, -5.778708),
            (1.341083, 0.709375, -5.778708),
            (-1.326013, 0.709375, 4.889676),
            (0.452051, 0.709375, 4.889676),
            (2.230115, 0.709375, 4.889676),
            (-1.326013, 0.709375, 3.111612),
            (0.452051, 0.709375, 3.111612),
            (2.230115, 0.709375, 3.111612),
            (-3.104077, 0.709375, 1.333548),
            (-1.326013, 0.709375, 1.333548),
            (0.452051, 0.709375, 1.333548),
            (2.230115, 0.709375, 1.333548),
            (-3.104077, 0.709375, -0.444516),
            (-1.326013, 0.709375, -0.444516),
            (0.452051, 0.709375, -0.444516),
            (2.230115, 0.709375, -0.444516),
            (-1.326013, 0.709375, -2.222580),
            (0.452051, 0.709375, -2.222580),
            (2.230115, 0.709375, -2.222580),
            (-1.326013, 0.709375, -4.000644),
            (0.452051, 0.709375, -4.000644),
            (2.230115, 0.709375, -4.000644),
            (0.452051, 0.709375, -5.778708),
            (2.230115, 0.709375, -5.778708),)


faces = ((19, 84, 110),
         (3, 47, 77),
         (30, 103, 71),
         (26, 97, 61),
         (5, 56, 95),
         (36, 113, 84),
         (37, 114, 91),
         (12, 69, 102),
         (17, 79, 51),
         (9, 61, 100),
         (13, 70, 103),
         (8, 60, 97),
         (32, 106, 69),
         (31, 104, 70),
         (21, 89, 113),
         (22, 91, 56),
         (18, 81, 111),
         (27, 99, 59),
         (4, 51, 81),
         (33, 107, 79),
         (28, 100, 66),
         (38, 116, 89),
         (39, 117, 96),
         (6, 58, 41),
         (15, 76, 106),
         (2, 42, 58),
         (11, 66, 104),
         (1, 41, 60),
         (25, 96, 118),
         (34, 110, 76),
         (7, 59, 42),
         (14, 71, 47),
         (35, 111, 86),
         (10, 64, 99),
         (23, 94, 116),
         (24, 95, 117),
         (20, 86, 114),
         (29, 102, 64),
         (16, 77, 107),
         (40, 118, 94),
         (32, 12, 11),
         (12, 29, 28),
         (29, 10, 9),
         (27, 8, 9),
         (15, 32, 31),
         (19, 34, 18),
         (15, 31, 18),
         (18, 31, 13),
         (13, 14, 33),
         (16, 33, 14),
         (30, 14, 13),
         (17, 4, 33),
         (36, 19, 18),
         (21, 36, 35),
         (38, 21, 20),
         (37, 5, 23),
         (26, 9, 8),
         (22, 5, 37),
         (25, 23, 5),
         (6, 8, 27),
         (2, 27, 7),
         (1, 8, 6),
         (40, 23, 25),
         (24, 39, 5),
         (60, 43, 61),
         (62, 44, 63),
         (65, 45, 66),
         (67, 46, 68),
         (70, 48, 71),
         (72, 49, 73),
         (74, 50, 75),
         (78, 51, 79),
         (80, 52, 81),
         (82, 53, 83),
         (85, 54, 86),
         (87, 55, 88),
         (90, 56, 91),
         (92, 57, 93),
         (98, 63, 43),
         (58, 98, 60),
         (42, 62, 98),
         (99, 64, 44),
         (59, 99, 62),
         (43, 65, 100),
         (101, 68, 45),
         (63, 101, 65),
         (44, 67, 101),
         (102, 69, 46),
         (64, 102, 67),
         (104, 73, 48),
         (45, 72, 104),
         (105, 75, 49),
         (68, 105, 72),
         (46, 74, 105),
         (106, 76, 50),
         (69, 106, 74),
         (71, 107, 77),
         (48, 78, 107),
         (108, 81, 51),
         (73, 108, 78),
         (49, 80, 108),
         (109, 83, 52),
         (75, 109, 80),
         (50, 82, 109),
         (110, 84, 53),
         (76, 110, 82),
         (52, 85, 111),
         (112, 88, 54),
         (83, 112, 85),
         (53, 87, 112),
         (113, 89, 55),
         (84, 113, 87),
         (54, 90, 114),
         (115, 93, 56),
         (88, 115, 90),
         (55, 92, 115),
         (116, 94, 57),
         (89, 116, 92),
         (93, 117, 95),
         (57, 96, 117),
         (94, 118, 96),
         (34, 19, 110),
         (16, 3, 77),
         (14, 30, 71),
         (9, 26, 61),
         (24, 5, 95),
         (19, 36, 84),
         (22, 37, 91),
         (29, 12, 102),
         (4, 17, 51),
         (28, 9, 100),
         (30, 13, 103),
         (26, 8, 97),
         (12, 32, 69),
         (13, 31, 70),
         (36, 21, 113),
         (5, 22, 56),
         (35, 18, 111),
         (7, 27, 59),
         (18, 4, 81),
         (17, 33, 79),
         (11, 28, 66),
         (21, 38, 89),
         (25, 39, 96),
         (1, 6, 41),
         (32, 15, 106),
         (6, 2, 58),
         (31, 11, 104),
         (8, 1, 60),
         (40, 25, 118),
         (15, 34, 76),
         (2, 7, 42),
         (3, 14, 47),
         (20, 35, 86),
         (27, 10, 99),
         (38, 23, 116),
         (39, 24, 117),
         (37, 20, 114),
         (10, 29, 64),
         (33, 16, 107),
         (23, 40, 94),
         (31, 32, 11),
         (11, 12, 28),
         (28, 29, 9),
         (10, 27, 9),
         (34, 15, 18),
         (4, 18, 13),
         (4, 13, 33),
         (3, 16, 14),
         (35, 36, 18),
         (20, 21, 35),
         (37, 38, 20),
         (38, 37, 23),
         (39, 25, 5),
         (2, 6, 27),
         (97, 60, 61),
         (98, 62, 63),
         (100, 65, 66),
         (101, 67, 68),
         (103, 70, 71),
         (104, 72, 73),
         (105, 74, 75),
         (107, 78, 79),
         (108, 80, 81),
         (109, 82, 83),
         (111, 85, 86),
         (112, 87, 88),
         (114, 90, 91),
         (115, 92, 93),
         (60, 98, 43),
         (41, 58, 60),
         (58, 42, 98),
         (62, 99, 44),
         (42, 59, 62),
         (61, 43, 100),
         (65, 101, 45),
         (43, 63, 65),
         (63, 44, 101),
         (67, 102, 46),
         (44, 64, 67),
         (70, 104, 48),
         (66, 45, 104),
         (72, 105, 49),
         (45, 68, 72),
         (68, 46, 105),
         (74, 106, 50),
         (46, 69, 74),
         (47, 71, 77),
         (71, 48, 107),
         (78, 108, 51),
         (48, 73, 78),
         (73, 49, 108),
         (80, 109, 52),
         (49, 75, 80),
         (75, 50, 109),
         (82, 110, 53),
         (50, 76, 82),
         (81, 52, 111),
         (85, 112, 54),
         (52, 83, 85),
         (83, 53, 112),
         (87, 113, 55),
         (53, 84, 87),
         (86, 54, 114),
         (90, 115, 56),
         (54, 88, 90),
         (88, 55, 115),
         (92, 116, 57),
         (55, 89, 92),
         (56, 93, 95),
         (93, 57, 117),
         (57, 94, 96),)

material = Material(ambient=Color(r=0.000000, g=0.000000, b=0.000000),
                    diffuse=Color(r=0.057000, g=0.259799, b=0.019739),
                    specular=Color(r=0.333000, g=0.333000, b=0.333000),
                    specular_exponent=96.078431,
                    refraction_index=1.000000,
                    dissolve=1.000000,
                    illum=2)
