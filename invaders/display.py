from functools import partial

from models import ALIEN_1
from linearalgebra import normal_vector
from contextlib import contextmanager
from collections import deque

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

def pre_draw(gl, glut):
    # clears screen
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    # marks buffer for redrawing
    gl.glLoadIdentity()

# Rotation angle for the triangle.
rtri = 0.0

# Rotation angle for the quadrilateral.
rquad = 0.0

consume = lambda iterator: deque(iterator, maxlen=0)

def draw_scene(gl, glut):
    global rtri, rquad

    pre_draw(gl, glut)

    # reset view to initialized view
    # gl.glTranslatef(-1.5, 0.0, -6.0)

    # rotate pyramid-building space by rtri on y axis
    gl.glRotatef(rtri, 0.0, 1.0, 0.0)

    with gl_environment(gl, gl.GL_TRIANGLES):
        gl.glColor3f(1.0, 0.0, 0.0)
        for i, tri in enumerate(ALIEN_1):
            consume(map(gl.glVertex3fv, tri))

        # gl.glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Front)
        # gl.glColor3f(0.0, 1.0, 0.0)  # Green
        # gl.glVertex3f(-1.0, -1.0, 1.0)  # Left Of Triangle (Front)
        # gl.glColor3f(0.0, 0.0, 1.0)  # Blue
        # gl.glVertex3f(1.0, -1.0, 1.0)

        # gl.glColor3f(1.0, 0.0, 0.0)  # Red
        # gl.glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Right)
        # gl.glColor3f(0.0, 0.0, 1.0)  # Blue
        # gl.glVertex3f(1.0, -1.0, 1.0)  # Left Of Triangle (Right)
        # gl.glColor3f(0.0, 1.0, 0.0)  # Green
        # gl.glVertex3f(1.0, -1.0, -1.0)  # Right

        # gl.glColor3f(1.0, 0.0, 0.0)  # Red
        # gl.glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Back)
        # gl.glColor3f(0.0, 1.0, 0.0)  # Green
        # gl.glVertex3f(1.0, -1.0, -1.0)  # Left Of Triangle (Back)
        # gl.glColor3f(0.0, 0.0, 1.0)  # Blue
        # gl.glVertex3f(-1.0, -1.0, -1.0)  # Right Of


        # gl.glColor3f(1.0, 0.0, 0.0)  # Red
        # gl.glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Left)
        # gl.glColor3f(0.0, 0.0, 1.0)  # Blue
        # gl.glVertex3f(-1.0, -1.0, -1.0)  # Left Of Triangle (Left)
        # gl.glColor3f(0.0, 1.0, 0.0)  # Green
        # gl.glVertex3f(-1.0, -1.0, 1.0)  # Right Of Triangle (Left)

    # What values to use?  Well, if you have a FAST machine
    # and a FAST 3D Card, then large values make an unpleasant display
    # with flickering and tearing.  I found that smaller values work better,
    # but this was based on my experience.
    rtri = rtri + 0.2  # Increase The Rotation Variable For The Triangle
    rquad = rquad - 0.15  # Decrease The Rotation Variable For The Quad

    # since this is double buffered, swap buffers to display what we drew
    glut.glutSwapBuffers()

def get_display(gl, glut):
    def display_func():
        return draw_scene(gl, glut)
    return display_func
