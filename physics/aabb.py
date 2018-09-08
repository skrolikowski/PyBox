import copy
import pyglet

from math import radians
from pybox.math import util, vec2d

class AABB:
    """
        Axis-aligned bounding box.

        Stores area information and intersection/containing checks.
    """

    def __init__(self, left, bottom, right, top):
        self._left   = left
        self._bottom = bottom
        self._right  = right
        self._top    = top

    def area(self):
        """Returns area of AABB.

        Returns:
            float
        """

        return (self._right - self._left) * (self._top - self._bottom)

    def center(self):
        """Returns center of AABB.

        Returns:
            float, float
        """

        return self._left - self._right, self._top - self._bottom

    def clamp_vec2d(self, v):
        """ Returns copy of Vec2D clamped to the AABB.

        Args:
            v(Vec2D): vector

        Returns:
            Vec2D
        """

        return vec2d.Vec2D(
            util.clamp(v.x, self._left, self._right),
            util.clamp(v.y, self._bottom, self._top)
        )

    def contains(self, other):
        """ Returns true if this AABB completely contains other AABB.

        Args:
            other(AABB): other bounding box

        Returns:
            bool
        """

        return self._left <= other.left and \
               self._right >= other.right and \
               self._bottom <= other.bottom and \
               self._top >= other.top

    def contains_vec2d(self, v):
        """ Returns true if this AABB completely contains vector.

        Args:
            v(Vec2D): vector

        Returns:
            bool
        """

        return self._left <= v.x <= self._right and \
               self._bottom <= v.y <= self._top

    def copy(self):
        """Create a deep copy of this BB.

        Returns:
            AABB
        """

        return copy.deepcopy(self)

    def unpack(self):
        """Alias for `tuple()`."""
        return self.tuple()

    def tuple(self):
        """Unpacks bounding box bounds.

        Returns:
            float, float, float, float
        """

        return self._left, self._bottom, self._right, self._top

    def expand(self, v):
        """ Returns new minimal AABB that contains AABB and vector.

        Args:
            v(Vec2D): vector

        Returns:
            AABB
        """

        return AABB(
            min(self._left, v.x),
            min(self._bottom, v.y),
            max(self._right, v.x),
            max(self._top, v.y)
        )

    def intersects(self, other):
        """ Returns true if this AABB intersects other AABB.

        Args:
            other(AABB): other bounding box

        Returns:
            bool
        """

        return self._left <= other.right and \
               self._right >= other.left and \
               self._bottom <= other.top and \
               self._top >= other.bottom

    def merge(self, other):
        """ Returns minimal AABB that contains both AABBs.

        Args:
            other(AABB): other bounding box

        Returns:
            AABB
        """

        return AABB(
            min(self._left, other.left),
            min(self._bottom, other.bottom),
            max(self._right, other.right),
            max(self._top, other.top)
        )

    def merge_area(self, other):
        """ Returns area of combined AABBs.

        Args:
            other(AABB): other bounding box

        Returns:
            float
        """

        width  = max(self._right, other.right) - min(self._left, other.left)
        height = max(self._top, other.top) - min(self._bottom, other.bottom)

        return width * height

    def draw(self):
        x1, y1, x2, y2 = self.unpack()
        color = 255, 0, 0, 255

        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_LINES,
            [0, 1, 1, 2, 2, 3, 3, 0],
            ('v2f', (x1, y1, x2, y1, x2, y2, x1, y2)),
            ('c4B', color * 4)
        )

    @property
    def left(self):
        return self._left

    @property
    def bottom(self):
        return self._bottom

    @property
    def right(self):
        return self._right

    @property
    def top(self):
        return self._top

    def __repr__(self):
        return 'BB(%s, %s, %s, %s)' % (self._left, self._bottom, self._right, self._top)

    def __eq__(self, other):
        return self._left == other.left and \
               self._bottom == other.bottom and \
               self._right == other.right and \
               self._top == other.top

    def __ne__(self, other):
        return not self.__eq__(other)

    @staticmethod
    def compute(vertices, transform):
        xmin = float('inf')
        ymin = float('inf')
        xmax = 0
        ymax = 0

        for x, y in vertices:
            vertex = transform * vec2d.Vec2D(x, y)

            xmin = min(xmin, vertex.x)
            xmax = max(xmax, vertex.x)
            ymin = min(ymin, vertex.y)
            ymax = max(ymax, vertex.y)

        return AABB(xmin, ymin, xmax, ymax)