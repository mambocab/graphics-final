from functools import partial

from models import ALIEN_1
from linearalgebra import normal_vector
from contextlib import contextmanager

from OpenGL.GL import *
from OpenGL.GLUT import *

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

def set_up(gl, glut):
    # clears screen
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    # gl magic
    gl.glEnable(gl.GL_TEXTURE_2D)
    # marks buffer for redrawing
    glut.glutPostRedisplay()

# Rotation angle for the triangle.
rtri = 0.0

# Rotation angle for the quadrilateral.
rquad = 0.0

def draw_scene():
    global rtri, rquad

    # clear screen & depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # reset view to initialized view
    glLoadIdentity()
    glTranslatef(-1.5, 0.0, -6.0)

    # rotate pyramid-building space by rtri on y axis
    glRotatef(rtri, 0.0, 1.0, 0.0)


    glBegin(GL_TRIANGLES)

    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Front)
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(-1.0, -1.0, 1.0)  # Left Of Triangle (Front)
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(1.0, -1.0, 1.0)

    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Right)
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(1.0, -1.0, 1.0)  # Left Of Triangle (Right)
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(1.0, -1.0, -1.0)  # Right

    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Back)
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(1.0, -1.0, -1.0)  # Left Of Triangle (Back)
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(-1.0, -1.0, -1.0)  # Right Of


    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(0.0, 1.0, 0.0)  # Top Of Triangle (Left)
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(-1.0, -1.0, -1.0)  # Left Of Triangle (Left)
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(-1.0, -1.0, 1.0)  # Right Of Triangle (Left)
    glEnd()

    # What values to use?  Well, if you have a FAST machine
    # and a FAST 3D Card, then large values make an unpleasant display
    # with flickering and tearing.  I found that smaller values work better,
    # but this was based on my experience.
    rtri = rtri + 0.2  # Increase The Rotation Variable For The Triangle
    rquad = rquad - 0.15  # Decrease The Rotation Variable For The Quad

    # since this is double buffered, swap buffers to display what we drew
    glutSwapBuffers()

def get_display(gl, glut):
    return draw_scene
