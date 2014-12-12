from functools import partial

from models import ALIEN_1
from linearalgebra import normal_vector
from contextlib import contextmanager
from collections import deque
from functools import wraps

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
    gl.glLoadIdentity()

# Rotation angle for the triangle.
rtri = 0.0

# Rotation angle for the quadrilateral.
rquad = 0.0

consume = lambda iterator: deque(iterator, maxlen=0)

def draw_alien(gl):
    with gl_environment(gl, gl.GL_TRIANGLES):
        # gl.glScalef(.4, .4, .4)
        gl.glColor3f(1.0, 0.0, 0.0)
        for i, tri in enumerate(ALIEN_1):
            consume(map(gl.glVertex3fv, tri))

def orient_alien(gl):
    gl.glRotatef(90, 0, 0, 1)
    gl.glRotatef(90, 1, 0, 0)


class once():
    '''decorator to make sure something is called once'''
    def __init__(self, f, *args, **kwargs):
        self.executed = False
        self.f, self.args, self.kwargs = f, args, kwargs

    def __call__(self):
        if not self.executed:
            self.f(*self.args, **self.kwargs)
        self.executed = True

@contextmanager
def world_pos(gl, p):
    world_x = 70
    gl.glTranslatef(-70 * p.x, -20 * p.y, 0)
    yield
    gl.glTranslatef(70 * p.x, 20 * p.y, 0)


def draw_scene(gl, glut, world):
    global rtri, rquad

    pre_draw(gl, glut)

    first = True

    gl.glTranslatef(-70, 40, -70)
    down_frame_motion = 0
    frame_step_size = 10

    orient_alien_first_time = once(orient_alien, gl)
    # render alien field

    with world_pos(gl, world.alien_field.position):
        first_row = True
        row_pushes = 0
        for row in world.alien_field.field:
            if not first_row:
                gl.glTranslatef(frame_step_size, 0, 0)
                row_pushes += 1
            else:
                first_row = False

            orient_alien_first_time()

            first_alien = True
            alien_pushes = 0
            for a in row:
                if first_alien:
                    first_alien = False
                else:
                    alien_pushes += 1
                    gl.glTranslatef(0, 0, frame_step_size)
                if a:
                    draw_alien(gl)
            gl.glTranslatef(0, 0, -alien_pushes * frame_step_size)

        gl.glTranslatef(-row_pushes * frame_step_size, 0, 0)

    # since this is double buffered, swap buffers to display what we drew
    glut.glutSwapBuffers()

    world.update()

def get_display(gl, glut, world):
    def display_func():
        return draw_scene(gl, glut, world)
    return display_func
