import copy
import math

from pybox.math import vec2d, util


class Matrix:
    def __init__(self, rows = 4, cols = 4):
        self.matx = Matrix.identity(rows, cols)
        self.rows = rows
        self.cols = cols

    def clone(self):
        """Copy object.

        Returns:
            Matrix: copy of this Matrix
        """

        return copy.deepcopy(self)

    def translate(self, tx, ty, tz=0):
        assert self.rows == 4 and self.cols == 4, 'Translations require a 4x4 matrix.'

        tmp = Matrix()
        tmp.matx = Matrix.identity(4, 4)

        tmp.matx[0][3] = tx
        tmp.matx[1][3] = ty
        tmp.matx[2][3] = tz

        self.matx = Matrix.mul(self, tmp)

        return self

    def scale(self, sx, sy, sz=1):
        assert self.rows == 4 and self.cols == 4, 'Scaling require a 4x4 matrix.'

        tmp = Matrix()
        tmp.matx = Matrix.identity(4, 4)

        tmp.matx[0][0] = sx
        tmp.matx[1][1] = sy
        tmp.matx[2][2] = sz

        self.matx = Matrix.mul(self, tmp)

        return self

    def rotate(self, angle, x=0, y=0, z=1):
        assert self.rows == 4 and self.cols == 4, 'Rotations require a 4x4 matrix.'

        tmp = Matrix()
        tmp.matx = Matrix.identity(4, 4)

        r = -math.radians(angle)
        c = math.cos(r)
        s = math.sin(r)
        o = 1.0 - c

        tmp.matx[0][0] = x * o + c
        tmp.matx[0][1] = x * y * o - z * s
        tmp.matx[0][2] = x * z * o + y * s
        tmp.matx[1][0] = y * x * o + z * s
        tmp.matx[1][1] = y * o + c
        tmp.matx[1][2] = y * z * o - x * s
        tmp.matx[2][0] = x * z * o - y * s
        tmp.matx[2][1] = y * z * o + x * s
        tmp.matx[2][2] = z * o + c

        self.matx = Matrix.mul(self, tmp)

        return self

    def shear(self, kx, ky):
        assert self.rows == 4 and self.cols == 4, 'Shearing require a 4x4 matrix.'

        tmp = Matrix()
        tmp.matx = Matrix.identity(4, 4)

        tmp.matx[0][1] = kx
        tmp.matx[1][0] = ky

        self.matx = Matrix.mul(self, tmp)

        return self

    def reflect(self):
        return self.rotate(math.radians(180))

    def getRow(self, r):
        """Get a list of element in the `r` row.

        Args:
            r(int): row index

        Return:
            List
        """

        return self.matx[r]

    def getColumn(self, c):
        """Get a list of element in the `c` column.

        Args:
            c(int): column index

        Return:
            List
        """

        return [self.matx[r][c] for r in range(self.rows)]

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
                util.dot(a.getRow(0), [b.unpack(), 1]),
                util.dot(a.getRow(1), [b.unpack(), 1])
            )

        elif type(b) == Matrix:
            if a.cols != b.rows:
                raise ArithmeticError("First Matrix column count doesn't match second Matrix row count.")

            result = Matrix.new(a.rows, b.cols)

            for r in range(a.rows):
                rowValues = a.getRow(r)

                for c in range(b.cols):
                    result[r][c] = util.dot(rowValues, b.getColumn(c))

        elif type(b) == int or type(b) == float:
            result = Matrix.new(a.rows, b.cols)

            for r in range(a.rows):
                for c in range(a.cols):
                    result[r][c] = a.matx[r][c] * b
        else:
            raise AttributeError("Attribute either must be a scalar value, Vec2D or another Matrix.")

        return result

    def __eq__(self, other):
        equals = True

        for r in range(self.rows):
            for c in range(self.cols):
                if self.matx[r][c] != other.matx[r][c]:
                    equals = False

        return equals

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return 'Matrix()'

    def __str__(self):
        result = ''

        for row in self.matx:
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
