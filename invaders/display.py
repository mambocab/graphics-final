from models import ALIEN_1, PLAYER, BARRIER
from contextlib import contextmanager

from utils import consume

from worlddatatypes import Owner
from random import choice
import time


@contextmanager
def gl_environment(gl, gl_env):
    gl.glBegin(gl_env)
    yield
    gl.glEnd()


@contextmanager
def orient_alien(gl):
    gl.glRotatef(-90, 0, 0, 1)
    gl.glRotatef(90, 1, 0, 0)

    yield

    gl.glRotatef(-90, 1, 0, 0)
    gl.glRotatef(90, 0, 0, 1)


@contextmanager
def orient_player(gl):
    gl.glRotatef(-90, 0, 0, 1)
    gl.glRotatef(90, 1, 0, 0)

    yield

    gl.glRotatef(90, 1, 0, 0)
    gl.glRotatef(-90, 0, 0, 1)


@contextmanager
def orient_barrier(gl):
    gl.glRotatef(-90, 0, 0, 1)
    gl.glRotatef(90, 1, 0, 0)

    yield

    gl.glRotatef(-90, 1, 0, 0)
    gl.glRotatef(90, 0, 0, 1)


def pre_draw(gl, glut):
    # clears screen
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()


def draw_alien(gl):
    with gl_scale_env(gl, 1, 1, .5):
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


_strength_to_color = {
    4: lambda: (1, 1, 1),
    3: lambda: (1, 0.658, 0.360),
    2: lambda: (0.992, 0.247, 0.247),
    1: lambda: choice(((1, 1, 1), (1, 0.658, 0.360), (0.992, 0.247, 0.247)))
}


@contextmanager
def gl_scale_env(gl, *args):
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


def draw_barrier(gl, strength):
    with gl_scale_env(gl, 22):
        with orient_barrier(gl):
            with gl_environment(gl, gl.GL_TRIANGLES):
                color = _strength_to_color[strength]()
                for tri in BARRIER:
                    gl.glColor3fv(color)
                    consume(map(gl.glVertex3fv, tri))


@contextmanager
def world_pos(gl, p):
    world_x = lambda x: -100 + 10 * x
    world_y = lambda y: -70 + 10 * y
    gl.glTranslatef(world_x(p.x), -world_y(p.y), 0)
    yield
    gl.glTranslatef(-world_x(p.x), world_y(p.y), 0)


def draw_alien_field(gl, alien_field):
    for alien_pos in alien_field.positions():
        with world_pos(gl, alien_pos):
            # orient_alien_first_time()
            draw_alien(gl)


def draw_barriers(gl, barriers):
    for pos, strength in barriers.positions(with_strength=True):
        with world_pos(gl, pos):
            draw_barrier(gl, strength)


bullet_colors = {
    Owner.aliens: (1, 1, .2),
    Owner.player: (0, .1, .3)
}


def draw_bullets(gl, glut, bullets):
    for b in bullets:
        gl.glColor3fv(bullet_colors[b.owner])
        with world_pos(gl, b.position):
            glut.glutSolidCube(1.5)


def draw_scene(gl, glut, world):

    pre_draw(gl, glut)

    gl.glTranslatef(0, 0, -50)
    draw_alien_field(gl, world.alien_field)
    draw_barriers(gl, world.barriers)
    draw_bullets(gl, glut, world.bullets)
    draw_player(gl, world.player.position)

    # since this is double buffered, swap buffers to display what we drew
    glut.glutSwapBuffers()

    if time.time() - world.last_updated > 1/60:
        world.update()


def get_display(gl, glut, world):
    def display_func():
        return draw_scene(gl, glut, world)
    return display_func
