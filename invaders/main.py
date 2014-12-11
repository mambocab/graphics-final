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
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

import keyboard
import display

def reshape(width,height):
    gl.glViewport(0, 0, width, height)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(60.0, width / height, 1.0, 8.0)

    gl.glMatrixMode(gl.GL_MODELVIEW)
    glu.gluLookAt(0, 0, 10,
                  0, 0, 0,
                  0, 1, 0)



# started from http://www.labri.fr/perso/nrougier/teaching/opengl/
if __name__ == '__main__':
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE
                             | glut.GLUT_RGB
                             | glut.GLUT_DEPTH)
    # turns on depth testing -- should we test to see if things are behind it or not?
    glut.glutCreateWindow('Hello world!')


    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glClearColor(0.0, 0.0, 0.0, 0.0)

    # specify pixels are byte-aligned while unpacking from memory
    gl.glPixelStorei(gl.GL_UNPACK_ALIGNMENT, 1)
    # set up shading
    gl.glShadeModel(gl.GL_SMOOTH)

    #make light0 exist
    gl.glEnable(gl.GL_LIGHTING)
    #set ambient lighting (via www.videotutorialsrock.com/opengl_tutorial/lighting/text.php)
    # gl.glLightModelfv(gl.GL_LIGHT_MODEL_AMBIENT, (.6, .6, .6, 1))


    # set up light position and intensity input
    intensity_val = 15
    light_intensity = (intensity_val, intensity_val, intensity_val, 1)
    light_position = (0, 5, 0, 1)

    # set light position and intensity
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_DIFFUSE, light_intensity)
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_SPECULAR, light_intensity)
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, light_position)
    gl.glEnable(gl.GL_LIGHT0)



    glut.glutReshapeWindow(1024, 1024)
    glut.glutReshapeFunc(reshape)
    glut.glutDisplayFunc(display.get_display(gl=gl, glut=glut))
    glut.glutKeyboardFunc(keyboard.keyboard)
    glut.glutMainLoop()












