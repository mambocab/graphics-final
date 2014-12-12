#!/usr/bin/env python

import argparse
import sys
import OpenGL

parser = argparse.ArgumentParser(description='run space invaders')
prod_message = 'enable production mode (disables logging & error checking)'
parser.add_argument('--prod', dest='production_mode',
                    action='store_const', const=True, default=False,
                    help=prod_message)
parser.add_argument('--fullscreen', dest='fullscreen_mode',
                    action='store_const', const=True, default=False,
                    help='enables fullsceen mode')

config = parser.parse_args()

if config.production_mode:
    OpenGL.ERROR_CHECKING = False
    OpenGL.ERROR_LOGGING = False

##############

from OpenGL import GL as gl
from OpenGL import GLU as glu
from OpenGL import GLUT as glut

import display
import keyboard

from world import World

# Number of the glut window.
window = 0


def get_aspect_ratio(width, height):
    try:
        return width / height
    except ZeroDivisionError:
        return width


def set_projection_matrix(width, height, reset_to_modelview=True):
    # reset projection matrix
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    # internally set aspect ratio
    glu.gluPerspective(120.0, get_aspect_ratio(width, height), 0.1, 100.0)

    if reset_to_modelview:
        gl.glMatrixMode(gl.GL_MODELVIEW)


def init_environment(width, height):
    '''initialize OpenGL environment'''
    # black background
    gl.glClearColor(0.0, 0.0, 0.0, 0.0)
    # enable depth buffer clearing
    gl.glClearDepth(1.0)
    # set depth test type and enable depth testing
    gl.glDepthFunc(gl.GL_LESS)
    gl.glEnable(gl.GL_DEPTH_TEST)
    # use smooth color shading
    gl.glShadeModel(gl.GL_SMOOTH)

    set_projection_matrix(width, height)


def resize_func(width, height):
    '''function to call when window is resized'''
    # reset viewport
    gl.glViewport(0, 0, width, height)
    set_projection_matrix(width, height)


if __name__ == '__main__':
    glut.glutInit(sys.argv)

    width, height = 640, 480

    glut.glutInitDisplayMode(glut.GLUT_RGBA
                             | glut.GLUT_DOUBLE
                             | glut.GLUT_DEPTH)
    glut.glutInitWindowSize(width, height)
    glut.glutInitWindowPosition(0, 0)

    # assign to global window variable
    window = glut.glutCreateWindow('Invaders')
    if config.fullscreen_mode:
        glut.glutFullScreen()

    world = World()

    # draw scene on display and between other calculations
    draw_func = display.get_display(gl, glut, world)
    glut.glutDisplayFunc(draw_func)

    glut.glutIdleFunc(draw_func)
    glut.glutReshapeFunc(resize_func)
    glut.glutKeyboardFunc(keyboard.normal_keys)

    init_environment(width, height)

    glut.glutMainLoop()
