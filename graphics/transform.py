from pybox.math.matrix import Matrix

class Transform:
    def __init__(self, x = 0, y = 0, angle = 0, sx = 1, sy = 1, ox = 0, oy = 0, kx = 0, ky = 0):
        self.matrix = Matrix()

        self.x = x
        self.y = y
        self.angle = angle
        self.sx = sx
        self.sy = sy
        self.ox = ox
        self.oy = oy
        self.kx = kx
        self.ky = ky

        self.matrix \
            .translate(-ox, -oy) \
            .scale(sx, sy) \
            .rotate(angle) \
            .translate(x, y) \
            .shear(kx, ky)

    def apply(self, other):
        """Multiplies this transform's matrix with anothers.

        Args:
            other(Transform): Transform to apply to this one.

        Return:
            Transform: new Transform
        """

        self.matrix = self.matrix * other.matrix

        return self

    def clone(self):
        """Copy object.

        Returns:
            Transform: copy of this Transform
        """

        transform = Transform()
        transform.matrix = self.matrix.clone()

        return transform

    def translate(self, tx, ty):
        self.matrix.translate(tx, ty)

    def scale(self, sx, sy):
        self.matrix.scale(sx, sy)

    def rotate(self, angle):
        self.matrix.rotate(angle)

    def shear(self, kx, ky):
        self.matrix.shear(kx, ky)

    def reflect(self):
        self.matrix.reflect()

    def __repr__(self):
        return 'Transform({},{},{},{},{},{},{},{},{})'.format(
            self.x, self.y, self.angle, self.sx, self.sy, self.ox, self.oy, self.kx, self.ky)

    def __str__(self):
        return str(self.matrix)