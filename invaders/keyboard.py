import sys
from OpenGL import GLUT as glut

def normal_keys(key, x, y, _exit=sys.exit):
    if key == b'q':
        _exit()


def get_special_keys(world):
    accepted_special_keys = {
        glut.GLUT_KEY_LEFT: world.receive_left,
        glut.GLUT_KEY_RIGHT: world.receive_right,
        glut.GLUT_KEY_UP: world.receive_up,
    }
    def special_keys(key, x, y):
        try:
            # print('got special key!')
            func = accepted_special_keys[key]()
        except KeyError:
            pass
    return special_keys
