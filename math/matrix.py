import copy
import math

from pybox.math import vec2d, util


class Matrix:
    def __init__(self, rows = 4, cols = 4):
        self._matx = Matrix.identity(rows, cols)
        self._rows = rows
        self._cols = cols

    def clone(self):
        """Copy object.

        Returns:
            Matrix: copy of this Matrix
        """

        return copy.deepcopy(self)

    def translate(self, tx, ty, tz=0):
        assert self._rows == 4 and self._cols == 4, 'Translations require a 4x4 matrix.'

        tmp = Matrix()
        tmp._matx = Matrix.identity(4, 4)

        tmp._matx[0][3] = tx
        tmp._matx[1][3] = ty
        tmp._matx[2][3] = tz

        self._matx = Matrix.mul(self, tmp)

        return self

    def scale(self, sx, sy, sz=1):
        assert self._rows == 4 and self._cols == 4, 'Scaling require a 4x4 matrix.'

        tmp = Matrix()
        tmp._matx = Matrix.identity(4, 4)

        tmp._matx[0][0] = sx
        tmp._matx[1][1] = sy
        tmp._matx[2][2] = sz

        self._matx = Matrix.mul(self, tmp)

        return self

    def rotate(self, angle, x=0, y=0, z=1):
        assert self._rows == 4 and self._cols == 4, 'Rotations require a 4x4 matrix.'

        tmp = Matrix()
        tmp._matx = Matrix.identity(4, 4)

        r = math.radians(angle)
        c = math.cos(r)
        s = math.sin(r)
        o = 1.0 - c

        tmp._matx[0][0] = x * o + c
        tmp._matx[0][1] = x * y * o - z * s
        tmp._matx[0][2] = x * z * o + y * s
        tmp._matx[1][0] = y * x * o + z * s
        tmp._matx[1][1] = y * o + c
        tmp._matx[1][2] = y * z * o - x * s
        tmp._matx[2][0] = x * z * o - y * s
        tmp._matx[2][1] = y * z * o + x * s
        tmp._matx[2][2] = z * o + c

        self._matx = Matrix.mul(self, tmp)

        return self

    def shear(self, kx, ky):
        assert self._rows == 4 and self._cols == 4, 'Shearing require a 4x4 matrix.'

        tmp = Matrix()
        tmp._matx = Matrix.identity(4, 4)

        tmp._matx[0][1] = kx
        tmp._matx[1][0] = ky

        self._matx = Matrix.mul(self, tmp)

        return self

    def reflect(self):
        return self.rotate(math.radians(180))

    def transpose(self):
        tmp = Matrix()

        col0 = self.getColumn(0)
        col1 = self.getColumn(1)
        col2 = self.getColumn(2)
        col3 = self.getColumn(3)

        tmp._matx[0][0] = col0[0]
        tmp._matx[0][1] = col0[1]
        tmp._matx[0][2] = col0[2]
        tmp._matx[0][3] = col0[3]
        tmp._matx[1][0] = col1[0]
        tmp._matx[1][1] = col1[1]
        tmp._matx[1][2] = col1[2]
        tmp._matx[1][3] = col1[3]
        tmp._matx[2][0] = col2[0]
        tmp._matx[2][1] = col2[1]
        tmp._matx[2][2] = col2[2]
        tmp._matx[2][3] = col2[3]
        tmp._matx[3][0] = col3[0]
        tmp._matx[3][1] = col3[1]
        tmp._matx[3][2] = col3[2]
        tmp._matx[3][3] = col3[3]

        return tmp

    def inverse(self):
        raise NotImplementedError

    def determinant(self):
        raise NotImplementedError

    def getRow(self, r):
        """Get a list of element in the `r` row.

        Args:
            r(int): row index

        Return:
            List
        """

        return self._matx[r]

    def getColumn(self, c):
        """Get a list of element in the `c` column.

        Args:
            c(int): column index

        Return:
            List
        """

        return [self._matx[r][c] for r in range(self._rows)]

    def __mul__(self, other):
        return Matrix.mul(self, other)

    @staticmethod
    def mul(a, b):
        """Matrix multiplication.
        Matrices can be multiplied by:
          - scalar value (int or float)
          - Vec2D
          - another Matrix

        Raises:
            AttributeError: Attribute `b` either must be a scalar value, Vec2D or another Matrix.
            ArithmeticError: First Matrix column count doesn't match second Matrix row count.

        Args:
            a(Matrix): Matrix to update
            b(mixed): scaling value

        Return mixed
        """

        if type(b) == vec2d.Vec2D:
            result = vec2d.Vec2D(
                util.dot(a.getRow(0), [b.x, b.y, 1, 1]),
                util.dot(a.getRow(1), [b.x, b.y, 1, 1])
            )

        elif type(b) == Matrix:
            if a._cols != b._rows:
                raise ArithmeticError("First Matrix column count doesn't match second Matrix row count.")

            result = Matrix.new(a._rows, b._cols)

            for r in range(a._rows):
                rowValues = a.getRow(r)

                for c in range(b._cols):
                    result[r][c] = util.dot(rowValues, b.getColumn(c))

        elif type(b) == int or type(b) == float:
            result = Matrix.new(a._rows, b._cols)

            for r in range(a._rows):
                for c in range(a._cols):
                    result[r][c] = a._matx[r][c] * b
        else:
            raise AttributeError("Attribute either must be a scalar value, Vec2D or another Matrix.")

        return result

    def __eq__(self, other):
        equals = True

        for r in range(self._rows):
            for c in range(self._cols):
                if self._matx[r][c] != other._matx[r][c]:
                    equals = False

        return equals

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        raise NotImplementedError

    def __str__(self):
        result = ''

        for row in self._matx:
            result += str(row) + "\n"

        return result

    # Identity Matrix
    @staticmethod
    def new(rows, cols):
        """Create new Matrix initialized to 0 values.

        Args:
            rows(int): number of rows
            cols(int): number of columns

        Return:
            List
        """

        return [[0 for r in range(rows)] for c in range(cols)]

    # Identity Matrix
    @staticmethod
    def identity(rows, cols):
        """Create new identity Matrix.

        Args:
            rows(int): number of rows
            cols(int): number of columns

        Return:
            List
        """

        matrix = Matrix.new(rows, cols)

        for r in range(rows):
            for c in range(cols):
                if r == c:
                    matrix[r][c] = 1

        return matrix
