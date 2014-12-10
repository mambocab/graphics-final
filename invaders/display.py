
def display(gl, glut):
    def display_func():
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glEnable(gl.GL_TEXTURE_2D)
        glut.glutSwapBuffers()
    return display_func
