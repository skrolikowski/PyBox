import pyglet
import pybox.graphics
from pyglet.gl import *

window = pyglet.window.Window(640, 640, "OpenGL")
window.set_location(100, 100)

# gl.glViewport(0, 0, 640, 640)
# gl.glMatrixMode(gl.GL_PROJECTION)
# gl.glLoadIdentity()
# gl.glOrtho(0, 640-1, 0, 640-1, -1, 1)
# gl.glMatrixMode(gl.GL_MODELVIEW)
# gl.glLoadIdentity()


@window.event
def on_draw():
    window.clear()

    pybox.graphics.push()
    pybox.graphics.translate(200, 200)
    pybox.graphics.rotate(120)
    pybox.graphics.setColor(0, 0, 255, 255)
    pybox.graphics.setLineWidth(2)
    pybox.graphics.rectangle('line', 0, 0, 50, 50)
    pybox.graphics.pop()


    # pybox.graphics.push()
    # pybox.graphics.rotate(45)
    # pybox.graphics.translate(-75, -75)
    #
    # pybox.graphics.setColor(255, 0, 0, 255)
    # pybox.graphics.setLineWidth(2)
    # pybox.graphics.rectangle('line', 50, 50, 50, 50)
    #
    # pybox.graphics.pop()


if __name__ == '__main__':
    # t1 = pybox.graphics.transform.Transform()
    # t1.translate(1, 2)
    # t1.scale(0.5, 0.5)
    # print(t1)

    pyglet.app.run()
