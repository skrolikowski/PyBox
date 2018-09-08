from pybox.math.matrix import Matrix

class Transform:
    def __init__(self, x=0, y=0, z=1, angle=0, sx=1, sy=1, sz=1, kx=0, ky=0):
        self._matrix = Matrix() \
            .translate(x, y, z) \
            .rotate(angle) \
            .scale(sx, sy, sz) \
            .shear(kx, ky)

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = self._matrix

    def apply(self, other):
        """Multiplies this transform's matrix with anothers.

        Args:
            other(Transform): Transform to apply to this one.

        Return:
            Transform: new Transform
        """

        self._matrix = self._matrix * other._matrix

        return self

    def clone(self):
        """Copy object.

        Returns:
            Transform: copy of this Transform
        """

        transform = Transform()
        transform._matrix = self._matrix.clone()

        return transform

    def translate(self, tx, ty, tz=0):
        self._matrix.translate(tx, ty, tz)

    def scale(self, sx, sy, sz=1):
        self._matrix.scale(sx, sy, sz)

    def rotate(self, angle, x=0, y=0, z=1):
        self._matrix.rotate(angle, x, y, z)

    def shear(self, kx, ky):
        self._matrix.shear(kx, ky)

    def reflect(self):
        self._matrix.reflect()

    def inverse(self):
        self._matrix.inverse()

    def __repr__(self):
        raise NotImplementedError

    def __str__(self):
        return str(self._matrix)