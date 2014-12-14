from functools import partial

from models import ALIEN_1, PLAYER
from linearalgebra import normal_vector
from contextlib import contextmanager
from collections import deque
from functools import wraps

from worlddatatypes import Position2


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

def consume(iterator):
    """
    consumes an entire iterator, returning nothing.
    from the functools recipes.
    """
    deque(iterator, maxlen=0)

@contextmanager
def orient_alien(gl):
    gl.glRotatef(90, 0, 0, 1)
    gl.glRotatef(90, 1, 0, 0)

    yield

    gl.glRotatef(-90, 1, 0, 0)
    gl.glRotatef(-90, 0, 0, 1)

@contextmanager
def orient_player(gl):
    gl.glRotatef(-90, 0, 0, 1)
    gl.glRotatef(90, 1, 0, 0)

    yield

    gl.glRotatef(90, 1, 0, 0)
    gl.glRotatef(-90, 0, 0, 1)


def draw_alien(gl):
    with orient_alien(gl):
        with gl_environment(gl, gl.GL_TRIANGLES):
            gl.glColor3f(1.0, 0.0, 0.0)
            for tri in ALIEN_1:
                consume(map(gl.glVertex3fv, tri))

def draw_player(gl, pos):
    with world_pos(gl, pos):
        with orient_player(gl):
            with gl_environment(gl, gl.GL_TRIANGLES):
                gl.glColor3f(0, 0, 1)
                for tri in PLAYER:
                    consume(map(gl.glVertex3fv, tri))


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
    world_x = lambda x: -100 + 10 * x
    world_y = lambda y: -70 + 10 * y
    gl.glTranslatef(world_x(p.x), -world_y(p.y), 0)
    yield
    gl.glTranslatef(-world_x(p.x), world_y(p.y), 0)

def draw_alien_field(gl, world):

    for alien_pos in world.alien_field.alien_positions():
        with world_pos(gl, alien_pos):
            # orient_alien_first_time()
            draw_alien(gl)


def draw_bullets(gl, glut, bullets):
    for bullet_pos in bullets.bullet_positions():
        with world_pos(gl, bullet_pos):
            gl.glColor3f(1, 1, 1)
            glut.glutSolidCube(1.5)


def draw_scene(gl, glut, world):
    pre_draw(gl, glut)

    first = True

    gl.glTranslatef(0, 0, -50)

    draw_alien_field(gl, world)
    # draw_barriers()
    draw_bullets(gl, glut, world.bullets)
    draw_player(gl, world.player.position)


    # since this is double buffered, swap buffers to display what we drew
    glut.glutSwapBuffers()

    world.update()

def get_display(gl, glut, world):
    def display_func():
        return draw_scene(gl, glut, world)
    return display_func
