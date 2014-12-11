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

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL import GLU as glu

import display
import keyboard

# Number of the glut window.
window = 0

def get_aspect_ratio(width, height):
    try:
        return width / height
    except ZeroDivisionError:
        return width


def set_projection_matrix(width, height, reset_to_modelview=True):
    # reset projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # internally set aspect ratio
    glu.gluPerspective(45.0, get_aspect_ratio(width, height), 0.1, 100.0)

    if reset_to_modelview:
        glMatrixMode(GL_MODELVIEW)


def gl_init(width, height):
    '''initialize OpenGL environment'''
    # black background
    glClearColor(0.0, 0.0, 0.0, 0.0)
    # enable depth buffer clearing
    glClearDepth(1.0)
    # set depth test type and enable depth testing
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    # use smooth color shading
    glShadeModel(GL_SMOOTH)

    set_projection_matrix(width, height)


def resize_func(width, height):
    '''function to call when window is resized'''
    # reset viewport
    glViewport(0, 0, width, height)
    set_projection_matrix(width, height)


if __name__ == '__main__':
    glutInit(sys.argv)

    width, height = 640, 480

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)

    # assign to global window variable
    window = glutCreateWindow('Invaders')

    glutDisplayFunc(display.draw_scene)
    if config.fullscreen_mode:
        glutFullScreen()

    # redraw the scene between other calculations
    glutIdleFunc(display.get_display(None, None))
    glutReshapeFunc(resize_func)
    glutKeyboardFunc(keyboard.normal_keys)

    gl_init(width, height)

    glutMainLoop()
