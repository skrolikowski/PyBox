import pyglet
import pybox
import pyglet.gl as gl

class TransformGroup(pyglet.graphics.Group):
    def __init__(self, x=0, y=0, rotation=0, sx=1, sy=1, kx=0, ky=0, parent=None):
        super().__init__(parent=parent)

        self._x   = x
        self._y   = y
        self._sx  = sx
        self._sy  = sy
        self._kx  = kx
        self._ky  = ky
        self._rot = rotation

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def sx(self):
        return self._sx

    @sx.setter
    def sx(self, value):
        self._sx = value

    @property
    def sy(self):
        return self._sy

    @sy.setter
    def sy(self, value):
        self._sy = value

    @property
    def kx(self):
        return self._kx

    @kx.setter
    def kx(self, value):
        self._kx = value

    @property
    def ky(self):
        return self._ky

    @ky.setter
    def ky(self, value):
        self._ky = value

    @property
    def rotation(self):
        return self._rot

    @rotation.setter
    def rotation(self, value):
        self._rot = value

    @property
    def matrix(self):
        matrix = pybox.math.matrix.Matrix()
        matrix.translate(self._x, self._y)
        matrix.rotate(self._rot)
        matrix.scale(self._sx, self._sy)
        matrix.shear(self._kx, self._ky)

        return matrix

    def set_state(self):
        gl.glPushMatrix()

        gl.glLoadMatrixf(
            (gl.GLfloat * 16)
            (*(
                self.matrix.getColumn(0) +
                self.matrix.getColumn(1) +
                self.matrix.getColumn(2) +
                self.matrix.getColumn(3)
            ))
        )

    def unset_state(self):
        gl.glPopMatrix()