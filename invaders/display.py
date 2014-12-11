from functools import partial

from models import ALIEN_1
from linearalgebra import normal_vector
from contextlib import contextmanager

@contextmanager
def enabled(gl_setting):
    gl.glEnable(gl_setting)
    yield
    gl.glDisable(gl_setting)

@contextmanager
def gl_environment(gl, gl_env):
    gl.glBegin(gl_env)
    yield
    gl.glEnd()

@contextmanager
def gl_push_and_pop(gl):
    gl.glPushMatrix()
    yield
    gl.glPopMatrix()

def set_up(gl, glut):
    # clears screen
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    # gl magic
    gl.glEnable(gl.GL_TEXTURE_2D)
    # marks buffer for redrawing
    glut.glutPostRedisplay()

def set_vertices(gl):

    # set lighting values

    with gl_environment(gl, gl.GL_TRIANGLES):

        lightings = ((gl.GL_AMBIENT, ALIEN_1.material.ambient),
                     (gl.GL_DIFFUSE, ALIEN_1.material.diffuse),
                     (gl.GL_SPECULAR, ALIEN_1.material.specular))
        for lighting in lightings:
            gl.glMaterialfv(gl.GL_FRONT_AND_BACK, lighting[0], tuple(lighting[1]))

        # set norms for triangles
        # these are the norms for the surface, which is gross, but easy
        for tri in ALIEN_1.triangles:
            tri_norm = normal_vector(*tri)
            for x, y, z in ((v.x, v.y, v.z) for v in tri):
                gl.glNormal3f(*tri_norm)
                gl.glVertex3f(x, y, z)
            # # gl.glNormal3f(tri_norm.x, tri_norm.y, tri_norm.z)
            # gl.glVertex3f(B.x, B.y, B.z)
            # # gl.glNormal3f(tri_norm.x, tri_norm.y, tri_norm.z)
            # gl.glVertex3f(C.x, C.y, C.z)

    gl.glFlush()

def get_display(gl, glut):
    def display_func():
        set_up(gl, glut)

        with gl_push_and_pop(gl):
            set_vertices(gl)

        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        # glut.glutPostRedisplay()
        glut.glutSwapBuffers()
    return display_func

