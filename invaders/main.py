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

# A general OpenGL initialization function.  Sets all of the initial parameters.
def InitGL(Width, Height):  # We call this right after our OpenGL window is created.
    glClearColor(0.0, 0.0, 0.0, 0.0)  # This Will Clear The Background Color To Black
    glClearDepth(1.0)  # Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)  # The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)  # Enables Depth Testing
    glShadeModel(GL_SMOOTH)  # Enables Smooth Color Shading

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Reset The Projection Matrix
    # Calculate The Aspect Ratio Of The Window
    glu.gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(width, height):
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
    glTranslatef(-1.5,0.0,-6.0)  # Move Left And Into The Screen

    glRotatef(rtri,0.0,1.0,0.0)  # Rotate The Pyramid On It's Y Axis

    glBegin(GL_TRIANGLES)  # Start Drawing The Pyramid

    glColor3f(1.0,0.0,0.0)  # Red
    glVertex3f( 0.0, 1.0, 0.0)  # Top Of Triangle (Front)
    glColor3f(0.0,1.0,0.0)  # Green
    glVertex3f(-1.0,-1.0, 1.0)  # Left Of Triangle (Front)
    glColor3f(0.0,0.0,1.0)  # Blue
    glVertex3f( 1.0,-1.0, 1.0)

    glColor3f(1.0,0.0,0.0)  # Red
    glVertex3f( 0.0, 1.0, 0.0)  # Top Of Triangle (Right)
    glColor3f(0.0,0.0,1.0)  # Blue
    glVertex3f( 1.0,-1.0, 1.0)  # Left Of Triangle (Right)
    glColor3f(0.0,1.0,0.0)  # Green
    glVertex3f( 1.0,-1.0, -1.0)  # Right

    glColor3f(1.0,0.0,0.0)  # Red
    glVertex3f( 0.0, 1.0, 0.0)  # Top Of Triangle (Back)
    glColor3f(0.0,1.0,0.0)  # Green
    glVertex3f( 1.0,-1.0, -1.0)  # Left Of Triangle (Back)
    glColor3f(0.0,0.0,1.0)  # Blue
    glVertex3f(-1.0,-1.0, -1.0)  # Right Of


    glColor3f(1.0,0.0,0.0)  # Red
    glVertex3f( 0.0, 1.0, 0.0)  # Top Of Triangle (Left)
    glColor3f(0.0,0.0,1.0)  # Blue
    glVertex3f(-1.0,-1.0,-1.0)  # Left Of Triangle (Left)
    glColor3f(0.0,1.0,0.0)  # Green
    glVertex3f(-1.0,-1.0, 1.0)  # Right Of Triangle (Left)
    glEnd()


    glLoadIdentity()
    glTranslatef(1.5,0.0,-7.0)  # Move Right And Into The Screen
    glRotatef(rquad,1.0,1.0,1.0)  # Rotate The Cube On X, Y & Z
    glBegin(GL_QUADS)  # Start Drawing The Cube


    glColor3f(0.0,1.0,0.0)  # Set The Color To Blue
    glVertex3f( 1.0, 1.0,-1.0)  # Top Right Of The Quad (Top)
    glVertex3f(-1.0, 1.0,-1.0)  # Top Left Of The Quad (Top)
    glVertex3f(-1.0, 1.0, 1.0)  # Bottom Left Of The Quad (Top)
    glVertex3f( 1.0, 1.0, 1.0)  # Bottom Right Of The Quad (Top)

    glColor3f(1.0,0.5,0.0)  # Set The Color To Orange
    glVertex3f( 1.0,-1.0, 1.0)  # Top Right Of The Quad (Bottom)
    glVertex3f(-1.0,-1.0, 1.0)  # Top Left Of The Quad (Bottom)
    glVertex3f(-1.0,-1.0,-1.0)  # Bottom Left Of The Quad (Bottom)
    glVertex3f( 1.0,-1.0,-1.0)  # Bottom Right Of The Quad (Bottom)

    glColor3f(1.0,0.0,0.0)  # Set The Color To Red
    glVertex3f( 1.0, 1.0, 1.0)  # Top Right Of The Quad (Front)
    glVertex3f(-1.0, 1.0, 1.0)  # Top Left Of The Quad (Front)
    glVertex3f(-1.0,-1.0, 1.0)  # Bottom Left Of The Quad (Front)
    glVertex3f( 1.0,-1.0, 1.0)  # Bottom Right Of The Quad (Front)

    glColor3f(1.0,1.0,0.0)  # Set The Color To Yellow
    glVertex3f( 1.0,-1.0,-1.0)  # Bottom Left Of The Quad (Back)
    glVertex3f(-1.0,-1.0,-1.0)  # Bottom Right Of The Quad (Back)
    glVertex3f(-1.0, 1.0,-1.0)  # Top Right Of The Quad (Back)
    glVertex3f( 1.0, 1.0,-1.0)  # Top Left Of The Quad (Back)

    glColor3f(0.0,0.0,1.0)  # Set The Color To Blue
    glVertex3f(-1.0, 1.0, 1.0)  # Top Right Of The Quad (Left)
    glVertex3f(-1.0, 1.0,-1.0)  # Top Left Of The Quad (Left)
    glVertex3f(-1.0,-1.0,-1.0)  # Bottom Left Of The Quad (Left)
    glVertex3f(-1.0,-1.0, 1.0)  # Bottom Right Of The Quad (Left)

    glColor3f(1.0,0.0,1.0)  # Set The Color To Violet
    glVertex3f( 1.0, 1.0,-1.0)  # Top Right Of The Quad (Right)
    glVertex3f( 1.0, 1.0, 1.0)  # Top Left Of The Quad (Right)
    glVertex3f( 1.0,-1.0, 1.0)  # Bottom Left Of The Quad (Right)
    glVertex3f( 1.0,-1.0,-1.0)  # Bottom Right Of The Quad (Right)
    glEnd()  # Done Drawing The Quad

    # What values to use?  Well, if you have a FAST machine
    # and a FAST 3D Card, then large values make an unpleasant display
    # with flickering and tearing.  I found that smaller values work better,
    # but this was based on my experience.
    rtri  = rtri + 0.2  # Increase The Rotation Variable For The Triangle
    rquad = rquad - 0.15  # Decrease The Rotation Variable For The Quad


    # since this is double buffered, swap the buffers to display what just got drawn.
    glutSwapBuffers()

if __name__ == '__main__':
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)

    # assign to global window variable
    window = glutCreateWindow('Invaders')

    glutDisplayFunc(DrawGLScene)
    if config.fullscreen_mode:
        glutFullScreen()

    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyboard.normal_keys)

    InitGL(640, 480)

    glutMainLoop()
