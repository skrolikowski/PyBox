import copy
import math
from . import util

class Vec2D:
    """Vec2D data structure.

    Args:
        x(mixed): x-coordinate
        y(mixed): y-coordinate
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def unpack(self):
        """Alias for `tuple()`."""
        return self.tuple()

    def tuple(self):
        """Returns Vec2D as (x, y) tuple.

        Examples:
            >>> v1 = Vec2D(1, 2)
            >>> x, y = v1.tuple()
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
            >>> v1 = Vec2D(1, 2)
            >>> v2 = v1.copy()
            >>> print(v1)
            (1, 2)
            >>> print(v1)
            (1, 2)

        Returns:
            Vec2D
        """

        return copy.deepcopy(self)

    def scale(self, factor):
        """Scale Vec2D by factor.

        Args:
            factor(float): scale factor

        Examples:
            >>> v1 = Vec2D(1, 2)
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
            mixed: length of Vec2D
        """

        return self.length()

    def setMagnitude(self, mag):
        """Set new magnitude for vector.

        Args:
            mag(integer): new magnitude

        Returns:
            void
        """

        angle = self.heading()

        self.x = math.cos(angle) * mag
        self.y = math.sin(angle) * mag

    def length(self):
        """Get length of Vec2D.

        Examples:
            >>> v1 = Vec2D(3, 4)
            >>> l1 = v1.length()
            >>> print(l1)
            5.0

        Returns:
            float: length of Vec2D
        """

        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def setLength(self, length):
        """Alias for `setMagnitude`

        Args:
            length(integer): new length

        Returns:
            void
        """

        self.setMagnitude(length)

    def magnitudeSq(self):
        """Alias for `lengthSq`

        Returns:
            mixed: length of Vec2D squared.
        """

        return self.length()

    def lengthSq(self):
        """Get length of Vec2D.

        Examples:
            >>> v1 = Vec2D(3, 4)
            >>> l1 = v1.lengthSq()
            >>> print(l1)
            25

        Returns:
            float: length of Vec2D squared
        """

        return pow(self.x, 2) + pow(self.y, 2)

    def distance(self, other):
        """Get length of Vec2D.

        Examples:
            >>> v1 = Vec2D(1, 2)
            >>> v2 = Vec2D(3, 4)
            >>> distance = v1.distance(v2)
            >>> print(distance)
            2.8284271247461903

        Returns:
            float: length of Vec2D squared
        """
        return math.sqrt(pow(other.x - self.x, 2) + pow(other.y - self.y, 2))

    def heading(self):
        """Get vector's angle.

        Examples:
            >>> v1 = Vec2D(3, 4)
            >>> h1 = v1.heading()
            >>> print(h1, math.degrees(h1))
            0.9272952180016122 53.13010235415598

        Return:
            float
        """

        return math.atan2(self.y, self.x)

    def setHeading(self, angle):
        """Set new heading for vector.

        Args:
            angle(float): new heading

        Return:
            void
        """

        length = self.length()

        self.x = math.cos(angle)
        self.y = math.sin(angle)

        if length != 0:
            self.x *= length
            self.y *= length

    def rotate(self, angle):
        """Rotate vector by delta heading.

        Args:
            angle(float): delta heading

        Return:
            Vec2D
        """

        cos  = math.cos(angle)
        sin  = math.sin(angle)
        x, y = self.tuple()

        self.x = cos * x - sin * y
        self.y = sin * x + cos * y

        return self

    def perpendicular(self):
        """Reverse y-direction

        Return:
            Vec2D
        """

        self.y *= -1

        return self

    def normal(self):
        """Returns new normal vector.

        Return:
            Vec2D: new normal vector
        """

        return Vec2D(self.y * -1, self.x)

    def lerp(self, other, norm):
        """Linear interpolation between this and
        another vector.

        Note:
            `norm` must be a float value between 0 and 1.0

        Examples:
            >>> v1 = Vec2D(1, 2)
            >>> v2 = Vec2D(3, 4)
            >>> l1 = v1.lerp(v2, 0.25)
            >>> l2 = v1.lerp(v2, 0.5)
            >>> l3 = v1.lerp(v2, 0.75)
            >>> print(l1)
            (1.5, 2.5)
            >>> print(l2)
            (2.0, 3.0)
            >>> print(l3)
            (2.5, 3.5)

        Raises:
            Exception: If `norm` not between 0.0 and 1.0

        Args:
            other(Vec2D): comparing Vec2D
            norm(float): interpolation percentage

        Return:
            Vec2D
        """

        if norm < 0 or norm > 1:
            raise Exception('Second argument must be a float value between 0 and 1.0.')

        return self + (other - self) * norm

    def dot(self, other):
        """Calculate dot product between this vector and another.

        Args:
            other(Vec2D): other vector

        Returns:
            float

        Examples:
            >>> v1 = Vec2D(1, 2)
            >>> v2 = Vec2D(3, 4)
            >>> dp = v1.dot(v2)
            >>> print(dp)
            11
        """

        return self.x * other.x + self.y * other.y

    def cross(self, other):
        """Calculate cross product between this vector and another.

        Args:
            other(Vec2D): other vector

        Returns:
            float

        Examples:
            >>> v1 = Vec2D(1, 2)
            >>> v2 = Vec2D(3, 4)
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
            >>> v1 = Vec2D(1, 2)
            >>> v2 = Vec2D(3, 4)
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

    def angleBetween(self, other):
        dotmag2 = self.dot(other) / (self.length() * other.length())
        dotmag2 = util.clamp(dotmag2, -1, 1)

        return math.acos(dotmag2)

    def clamp(self, low, high):
        """Clamp vector's magnitude between min/max values.

        Args:
            low(integer): lower limit
            high(integer): upper limit

        Returns:
            Vec2D

        Examples:
            >>> v1 = Vec2D(3, 4)
            >>> v1 = v1.clamp(2, 3)
            >>> print(v1)
            (1.8000000000000003, 2.4)
        """

        length = self.length()

        self.setMagnitude(
            util.clamp(length, low, high)
        )

        return self

    def limit(self, value):
        """Limit magnitude of vector by max value.

        Args:
            value(integer): max value

        Return:
            Vec2D
        """

        if self.length() > value:
            return self.normalize().scale(value)

        return self

    def __add__(self, other):
        """Add two Vec2Ds and return the resulting new Vec2D.

        Args:
            other(Vec2D): other vector

        Returns:
            Vec2D: new Vec2D
        """

        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtract two vectors and return the resulting new Vec2D.

        Args:
            other(Vec2D): other vector

        Returns:
            Vec2D: new Vec2D
        """

        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """Multiply two vectors and return the resulting new Vec2D.

        Args:
            other(mixed): other vector

        Returns:
            Vec2D: new Vec2D
        """

        if type(other) == Vec2D:
            return Vec2D(self.x * other.x, self.y * other.y)

        return self.copy().scale(other)

    def __truediv__(self, other):
        """Divide two vectors and return the resulting new Vec2D.

        Args:
            other(mixed): other vector

        Returns:
            Vec2D: new Vec2D
        """

        if type(other) == Vec2D:
            if other.x == 0 or other.y == 0:
                raise ZeroDivisionError("Right-hand side Vec2D contains a 0. Cannot divide by 0.")

            return Vec2D(self.x / other.x, self.y / other.y)

        if other == 0:
            raise ZeroDivisionError("Right-hand side Vec2D contains a 0. Cannot divide by 0.")

        newVec2D = self.copy()
        newVec2D.x /= other
        newVec2D.y /= other

        return newVec2D

    def __lt__(self, other):
        """Test if lhs Vec2D is less than rhs Vec2D.

        Args:
            other(Vec2D): other vector

        Returns:
            bool: lhs < rhs
        """

        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        """Test if lhs Vec2D is greater than rhs Vec2D.

        Args:
            other(Vec2D): other vector

        Returns:
            bool: lhs > rhs
        """

        return self.x > other.x and self.y > other.y

    def __eq__(self, other):
        """Test if lhs Vec2D is equal to rhs Vec2D.

        Args:
            other(Vec2D): other vector

        Examples:
            >>> v1 = Vec2D(1, 2)
            >>> v2 = Vec2D(1, 3)
            >>> v3 = Vec2D(1, 3)
            >>> e1 = (v1 == v2)
            >>> print(e1)
            False
            >>> e2 = (v2 == v3)
            >>> print(e2)
            True

        Returns:
            bool: lhs == rhs
        """

        if type(other) == Vec2D:
            return self.x == other.x and self.y == other.y

        return self.x == other and self.x == other

    def __ne__(self, other):
        """Test if lhs Vec2D is not equal to rhs Vec2D.

        Args:
            other(Vec2D): other vector

        Examples:
            >>> v1 = Vec2D(1, 2)
            >>> v2 = Vec2D(1, 3)
            >>> v3 = Vec2D(1, 3)
            >>> e1 = (v1 != v2)
            >>> print(e1)
            True
            >>> e2 = (v2 != v3)
            >>> print(e2)
            False

        Returns:
            bool: lhs != rhs
        """

        if type(other) == Vec2D:
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
        return 'Vec2D(x=%s, y=%s)' % (self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)
