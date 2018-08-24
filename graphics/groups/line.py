import pyglet
import pybox
import pyglet.gl as gl

class LineGroup(pyglet.graphics.Group):
    def __init__(self, lineWidth=1, parent=None):
        super().__init__(parent=parent)

        self._lineWidth = lineWidth

    def set_state(self):
        gl.glLineWidth(self._lineWidth)

        gl.glEnable(gl.GL_LINE_SMOOTH)
        gl.glHint(gl.GL_LINE_SMOOTH_HINT, gl.GL_NICEST)
        gl.glHint(gl.GL_POLYGON_SMOOTH_HINT, gl.GL_NICEST)

    def unset_state(self):
        gl.glLineWidth(1.0)
        gl.glDisable(gl.GL_LINE_SMOOTH)

    @property
    def lineWidth(self):
        return self._lineWidth

    @lineWidth.setter
    def lineWidth(self, value):
        self._lineWidth = value