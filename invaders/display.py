import time
from contextlib import contextmanager
from random import choice

from OpenGL import GL as gl
from OpenGL import GLUT as glut

from models import ALIEN_1, BARRIER, PLAYER
from utils import consume
from worlddatatypes import Owner


@contextmanager
def gl_environment(gl_env):
    gl.glBegin(gl_env)
    yield
    gl.glEnd()


@contextmanager
def orient_alien():
    gl.glRotatef(-90, 0, 0, 1)
    gl.glRotatef(90, 1, 0, 0)

    yield

    gl.glRotatef(-90, 1, 0, 0)
    gl.glRotatef(90, 0, 0, 1)


@contextmanager
def orient_player():
    gl.glRotatef(-90, 0, 0, 1)
    gl.glRotatef(90, 1, 0, 0)

    yield

    gl.glRotatef(90, 1, 0, 0)
    gl.glRotatef(-90, 0, 0, 1)


@contextmanager
def orient_barrier():
    gl.glRotatef(-90, 0, 0, 1)
    gl.glRotatef(90, 1, 0, 0)

    yield

    gl.glRotatef(-90, 1, 0, 0)
    gl.glRotatef(90, 0, 0, 1)


def pre_draw():
    # clears screen
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()


def draw_alien():
    with gl_scale_env(1, 1, .5):
        with orient_alien():
            with gl_environment(gl.GL_TRIANGLES):
                gl.glColor3f(1.0, 0.0, 0.0)
                for tri in ALIEN_1:
                    consume(map(gl.glVertex3fv, tri))


def draw_player(pos):
    with world_pos(pos):
        with orient_player():
            with gl_environment(gl.GL_TRIANGLES):
                gl.glColor3f(0, 0, 1)
                for tri in PLAYER:
                    consume(map(gl.glVertex3fv, tri))


_strength_to_color = {
    4: lambda: (1, 1, 1),
    3: lambda: (1, 0.658, 0.360),
    2: lambda: (0.992, 0.247, 0.247),
    1: lambda: choice(((1, 1, 1), (1, 0.658, 0.360), (0.992, 0.247, 0.247)))
}


@contextmanager
def gl_scale_env(*args):
    if len(args) == 1:
        a = args[0]
        scale_factor_x, scale_factor_y, scale_factor_z = a, a, a
    elif len(args) == 3:
        scale_factor_x = args[0]
        scale_factor_y = args[1]
        scale_factor_z = args[2]
    else:
        raise ValueError

    gl.glScale(scale_factor_x, scale_factor_y, scale_factor_z)
    yield
    gl.glScale(1/scale_factor_x, 1/scale_factor_y, 1/scale_factor_z)


def draw_barrier(strength):
    with gl_scale_env(22):
        with orient_barrier():
            with gl_environment(gl.GL_TRIANGLES):
                color = _strength_to_color[strength]()
                for tri in BARRIER:
                    gl.glColor3fv(color)
                    consume(map(gl.glVertex3fv, tri))


@contextmanager
def world_pos(p):
    world_x = lambda x: -100 + 10 * x
    world_y = lambda y: -70 + 10 * y
    gl.glTranslatef(world_x(p.x), -world_y(p.y), 0)
    yield
    gl.glTranslatef(-world_x(p.x), world_y(p.y), 0)


def draw_alien_field(alien_field):
    for alien_pos in alien_field.positions():
        with world_pos(alien_pos):
            draw_alien()


def draw_barriers(barriers):
    for pos, strength in barriers.positions(with_strength=True):
        with world_pos(pos):
            draw_barrier(strength)


bullet_colors = {
    Owner.aliens: (1, 1, .2),
    Owner.player: (0, .1, .3)
}


def draw_bullets(bullets):
    for b in bullets:
        gl.glColor3fv(bullet_colors[b.owner])
        with world_pos(b.position):
            glut.glutSolidCube(1.5)


def draw_scene(world):

    pre_draw()

    gl.glTranslatef(0, 0, -50)
    draw_alien_field(world.alien_field)
    draw_barriers(world.barriers)
    draw_bullets(world.bullets)
    draw_player(world.player.position)

    # since this is double buffered, swap buffers to display what we drew
    glut.glutSwapBuffers()

    if time.time() - world.last_updated > 1/60:
        world.update()


def get_display(world):
    def display_func():
        return draw_scene(world)
    return display_func
