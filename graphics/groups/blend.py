import pyglet
import pybox
import pyglet.gl as gl

class BlendGroup(pyglet.graphics.Group):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def set_state(self):
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

    def unset_state(self):
        gl.glDisable(gl.GL_BLEND)