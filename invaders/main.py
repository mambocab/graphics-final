#!/usr/bin/env python

import argparse
import sys

# don't import submodules until logging & err handling is set
import OpenGL

parser = argparse.ArgumentParser(description='run space invaders')
prod_message = 'enable production mode (disables logging & error checking)'
parser.add_argument('--prod', dest='production_mode',
                    action='store_const', const=True, default=False,
                    help=prod_message)
parser.add_argument('--debug', dest='extra_debug',
                    action='store_const', const=False, default=True,
                    help="enables extra debugging")


config = parser.parse_args()

if config.production_mode:
    OpenGL.ERROR_CHECKING = False
    OpenGL.ERROR_LOGGING = False
else:
    from OpenGL.arrays import numpymodule
    numpymodule.NumpyHandler.ERROR_ON_COPY = True

#########

import OpenGL.GL as gl
import OpenGL.GLUT as glut

import keyboard
import display

def reshape(width,height):
    gl.glViewport(0, 0, width, height)

# started from http://www.labri.fr/perso/nrougier/teaching/opengl/
if __name__ == '__main__':
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE
                             | glut.GLUT_RGB
                             | glut.GLUT_DEPTH)
    glut.glutCreateWindow('Hello world!')
    glut.glutReshapeWindow(512,512)
    glut.glutReshapeFunc(reshape)
    glut.glutDisplayFunc(display.display(gl=gl, glut=glut))
    glut.glutKeyboardFunc(keyboard.keyboard)
    glut.glutMainLoop()
