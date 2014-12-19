import OpenGL

import models


def test_basic_model_build():
    assert isinstance(models.ALIEN_1.material, models.datatypes.Material)


def test_model_faces_to_triangles():
    assert len(models.ALIEN_1.triangles) == len(models.data.alien1.faces)


def test_material_color_type():
    for light_type in ('ambient', 'diffuse', 'specular'):
        assert isinstance(getattr(models.ALIEN_1.material, light_type),
                          OpenGL.constants.GLfloat_4)
