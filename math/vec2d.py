import copy
from math import sqrt


class Vec2d:
    """Vec2d data structure.

    Args:
        x(mixed): x-coordinate
        y(mixed): y-coordinate
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def unpack(self):
        """Unpack Vec2d into x, y-coordinates.

        Examples:
            >>> v1 = Vec2d(1, 2)
            >>> x, y = v1.unpack()
            >>> print(x)
            1
            >>> print(y)
            2

        Returns:
            mixed, mixed
        """

        return self.x, self.y

    def copy(self):
        """Copy object.

        Examples:
            >>> v1 = Vec2d(1, 2)
            >>> v2 = v1.copy()
            >>> print(v1)
            (1, 2)
            >>> print(v1)
            (1, 2)

        Returns:
            Vec2d
        """

        return copy.deepcopy(self)

    def scale(self, factor):
        """Scale Vec2d by factor.

        Examples:
            >>> v1 = Vec2d(1, 2)
            >>> v1 = v1.scale(2)
            >>> print(v1)
            (2, 4)
        """

        self.x *= factor
        self.y *= factor

        return self

    def magnitude(self):
        """Alias for `length`

        Returns:
            mixed: length of Vec2d
        """

        return self.length()

    def length(self):
        """Get length of Vec2d.

        Examples:
            >>> v1 = Vec2d(3, 4)
            >>> l1 = v1.length()
            >>> print(l1)
            5.0

        Returns:
            float: length of Vec2d
        """

        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def magnitudeSq(self):
        """Alias for `lengthSq`

        Returns:
            mixed: length of Vec2d squared.
        """

        return self.length()

    def lengthSq(self):
        """Get length of Vec2d.

        Examples:
            >>> v1 = Vec2d(3, 4)
            >>> l1 = v1.lengthSq()
            >>> print(l1)
            25

        Returns:
            float: length of Vec2d squared
        """

        return pow(self.x, 2) + pow(self.y, 2)

    def distance(self, other):
        """Get length of Vec2d.

        Examples:
            >>> v1 = Vec2d(1, 2)
            >>> v2 = Vec2d(3, 4)
            >>> distance = v1.distance(v2)
            >>> print(distance)
            2.8284271247461903

        Returns:
            float: length of Vec2d squared
        """
        return sqrt(pow(other.x - self.x, 2) + pow(other.y - self.y, 2))

    def lerp(self, other, norm):
        """Linear interpolation between this and
        another vector.

        Note:
            `norm` must be a float value between 0 and 1.0

        Raises:
            Exception: If `norm` not between 0.0 and 1.0

        Args:
            other(Vec2d): comparing Vec2d
            norm(float): interpolation percentage

        Return:
            Vec2d

        Examples:
            >>> v1 = Vec2d(1, 2)
            >>> v2 = Vec2d(3, 4)
            >>> l1 = v1.lerp(v2, 0.25)
            >>> l2 = v1.lerp(v2, 0.5)
            >>> l3 = v1.lerp(v2, 0.75)
            >>> print(l1)
            (1.5, 2.5)
            >>> print(l2)
            (2.0, 3.0)
            >>> print(l3)
            (2.5, 3.5)
        """

        if norm < 0 or norm > 1:
            raise Exception('Second argument must be a float value between 0 and 1.0.')

        return self + (other - self) * norm

    def dot(self, other):
        """Calculate dot product between this vector and another.

        Args:
            other(Vec2d): other vector

        Returns:
            float

        Examples:
            >>> v1 = Vec2d(1, 2)
            >>> v2 = Vec2d(3, 4)
            >>> dp = v1.dot(v2)
            >>> print(dp)
            11
        """

        return self.x * other.x + self.y * other.y

    def cross(self, other):
        """Calculate cross product between this vector and another.

        Args:
            other(Vec2d): other vector

        Returns:
            float

        Examples:
            >>> v1 = Vec2d(1, 2)
            >>> v2 = Vec2d(3, 4)
            >>> dp = v1.cross(v2)
            >>> print(dp)
            -2
        """

        return self.x * other.y - self.y * other.x

    def normalize(self):
        """Normalize our vector to a length of one unit.

        Returns:
            float

        Examples:
            >>> v1 = Vec2d(1, 2)
            >>> v2 = Vec2d(3, 4)
            >>> v1 = v1.normalize()
            >>> v2 = v2.normalize()
            >>> print(v1)
            (0.447, 0.894)
            >>> print(v2)
            (0.6, 0.8)
        """

        length = self.length()

        if length > 0:
            return round(self.scale(1 / length), 3)

        return self

    def __add__(self, other):
        """Add two Vec2ds and return the resulting new Vec2d.

        Args:
            other(Vec2d): other vector

        Returns:
            Vec2d: new Vec2d
        """

        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtract two vectors and return the resulting new Vec2d.

        Args:
            other(Vec2d): other vector

        Returns:
            Vec2d: new Vec2d
        """

        return Vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """Multiply two vectors and return the resulting new Vec2d.

        Args:
            other(mixed): other vector

        Returns:
            Vec2d: new Vec2d
        """

        if type(other) == Vec2d:
            return Vec2d(self.x * other.x, self.y * other.y)

        return self.copy().scale(other)

    def __truediv__(self, other):
        """Divide two vectors and return the resulting new Vec2d.

        Args:
            other(Vec2d): other vector

        Returns:
            Vec2d: new Vec2d
        """

        if type(other) == Vec2d:
            if other.x == 0 or other.y == 0:
                raise ZeroDivisionError("Right-hand side Vec2d contains a 0. Cannot divide by 0.")

            return Vec2d(self.x / other.x, self.y / other.y)

        if other == 0:
            raise ZeroDivisionError("Right-hand side Vec2d contains a 0. Cannot divide by 0.")

        newVec2d = self.copy()
        newVec2d.x /= other
        newVec2d.y /= other

        return newVec2d

    def __lt__(self, other):
        """Test if lhs Vec2d is less than rhs Vec2d.

        Args:
            other(Vec2d): other vector

        Returns:
            bool: lhs < rhs
        """

        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        """Test if lhs Vec2d is greater than rhs Vec2d.

        Args:
            other(Vec2d): other vector

        Returns:
            bool: lhs > rhs
        """

        return self.x > other.x and self.y > other.y

    def __eq__(self, other):
        """Test if lhs Vec2d is equal to rhs Vec2d.

        Args:
            other(Vec2d): other vector

        Examples:
            >>> v1 = Vec2d(1, 2)
            >>> v2 = Vec2d(1, 3)
            >>> v3 = Vec2d(1, 3)
            >>> e1 = (v1 == v2)
            >>> print(e1)
            False
            >>> e2 = (v2 == v3)
            >>> print(e2)
            True

        Returns:
            bool: lhs == rhs
        """

        if type(other) == Vec2d:
            return self.x == other.x and self.y == other.y

        return self.x == other and self.x == other

    def __ne__(self, other):
        """Test if lhs Vec2d is not equal to rhs Vec2d.

        Args:
            other(Vec2d): other vector

        Examples:
            >>> v1 = Vec2d(1, 2)
            >>> v2 = Vec2d(1, 3)
            >>> v3 = Vec2d(1, 3)
            >>> e1 = (v1 != v2)
            >>> print(e1)
            True
            >>> e2 = (v2 != v3)
            >>> print(e2)
            False

        Returns:
            bool: lhs != rhs
        """

        if type(other) == Vec2d:
            return self.x != other.x or self.y != other.y

        return self.x != other and self.x != other

    def __abs__(self):
        self.x = abs(self.x)
        self.y = abs(self.y)

        return self

    def __round__(self, n=None):
        self.x = round(self.x, n)
        self.y = round(self.y, n)

        return self

    def __repr__(self):
        return 'Vec2d(x=%s, y=%s)' % (self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)
