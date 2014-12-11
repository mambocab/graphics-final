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

import keyboard

# Number of the glut window.
window = 0

# Rotation angle for the triangle.
rtri = 0.0

# Rotation angle for the quadrilateral.
rquad = 0.0

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

    # reset projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # internally set aspect ratio
    glu.gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)

    # switch to model view so we can start building models
    glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def resize_func(width, height):
    if height == 0:  # Prevent A Divide By Zero If The Window Is Too Small
        height = 1

    glViewport(0, 0, width, height)  # Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glu.gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

# The main drawing function.
def DrawGLScene():
    global rtri, rquad

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear The Screen And The Depth Buffer
    glLoadIdentity()  # Reset The View
    glTranslatef(-1.5, 0.0, -6.0)  # Move Left And Into The Screen

    glRotatef(rtri, 0.0, 1.0, 0.0)  # Rotate The Pyramid On It's Y Axis

    glBegin(GL_TRIANGLES)  # Start Drawing The Pyramid

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

if __name__ == '__main__':
    glutInit(sys.argv)

    width, height = 640, 480

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)

    # assign to global window variable
    window = glutCreateWindow('Invaders')

    glutDisplayFunc(DrawGLScene)
    if config.fullscreen_mode:
        glutFullScreen()

    # redraw the scene between other calculations
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(resize_func)
    glutKeyboardFunc(keyboard.normal_keys)

    gl_init(width, height)

    glutMainLoop()
