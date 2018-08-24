import pyglet
import pybox

from math import radians, cos, sin, pi

from pybox.variables import *
from pybox.math.vec2d import Vec2D
from pybox.graphics.groups import transform, blend, line

from pyglet.gl import gl


# ---------------------------
# Shape Class
class Shape:
    def __init__(self, x, y, vertices, vertex_mode, mode, batch):
        self._position  = Vec2D(x, y)
        self._angle     = 0
        self._sx        = 1
        self._sy        = 1
        self._batch     = batch
        self._mode      = mode
        self._lineWidth = 1

        self._vertex_list      = None
        self._vertex_groups    = {}
        self._vertices         = vertices
        self._vertex_mode      = vertex_mode
        self._vertex_color     = (255, 255, 255, 255)

        self._create_vertex_groups()
        self._create_vertex_list()

    def _create_vertex_list(self):
        vertex_count = len(self._vertices) // 2
        vertex_mode  = self._vertex_mode
        vertex_group = list(self._vertex_groups.values())[-1]

        self._vertex_list = self._batch.add(vertex_count, vertex_mode, vertex_group, "v2f", "c4B", "t3f")

        self._update_vertex_vertices()
        self._update_vertex_color()

    def _create_vertex_groups(self):
        transformGroup = transform.TransformGroup(
            self._position.x, self._position.y,
            self._angle,
            self._sx, self._sy
        )
        blendGroup = blend.BlendGroup(parent=transformGroup)
        lineGroup = line.LineGroup(self._lineWidth, parent=blendGroup)

        self._vertex_groups["transform"] = transformGroup
        self._vertex_groups["blend"] = blendGroup
        self._vertex_groups["line"] = lineGroup

    """
        Update vertex list vertices.
    """
    def _update_vertex_vertices(self):
        self._vertex_list.vertices = self._vertices

    """
        Update vertex list colors.
    """
    def _update_vertex_color(self):
        self._vertex_list.colors = self._vertex_color * self._vertex_list.get_size()

    """
        Update shape transformation.
    """
    def _update_vertex_transform(self, **kwargs):
        self._vertex_groups["transform"].x     = kwargs.get('x', self._position.x)
        self._vertex_groups["transform"].y     = kwargs.get('y', self._position.y)
        self._vertex_groups["transform"].angle = kwargs.get('angle', self._angle)
        self._vertex_groups["transform"].sx    = kwargs.get('sx', self._sx)
        self._vertex_groups["transform"].sy    = kwargs.get('sy', self._sy)

    def update(self, **kwargs):
        self._position.x = kwargs.get('x', self._position.x)
        self._position.y = kwargs.get('y', self._position.y)
        self._angle      = kwargs.get('angle', self._angle)
        self._sx         = kwargs.get('sx', self._sx)
        self._sy         = kwargs.get('sy', self._sy)

        self._update_vertex_transform(**kwargs)

    def delete(self):
        self._vertex_list.delete()

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
        self._update_vertex_transform()

    @property
    def x(self):
        return self._position

    @x.setter
    def x(self, value):
        self._position.x = value
        self._update_vertex_transform()

    @property
    def y(self):
        return self._position

    @y.setter
    def y(self, value):
        self._position.y = value
        self._update_vertex_transform()

    @property
    def sx(self):
        return self._sx

    @sx.setter
    def sx(self, value):
        self._sx = value
        self._update_vertex_transform()

    @property
    def sy(self):
        return self._sy

    @sy.setter
    def sy(self, value):
        self._sy = value
        self._update_vertex_transform()

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value
        self._update_vertex_transform()

    @property
    def color(self):
        return self._vertex_color

    @color.setter
    def color(self, value):
        self._vertex_color = value
        self._update_vertex_color()

    @property
    def lineWidth(self):
        return self._vertex_groups["line"].lineWidth

    @lineWidth.setter
    def lineWidth(self, value):
        self._vertex_groups["line"].lineWidth = value


# ---------------------------
# Rectangle Class
class Rectangle(Shape):
    def __init__(self, x, y, width, height, mode="line", batch=default_batch):
        self._width  = width
        self._height = height

        vertices    = self._create_vertex_vertices()
        vertex_mode = gl.GL_LINE_LOOP if mode == "line" else gl.GL_QUADS

        super().__init__(x, y, vertices, vertex_mode, mode, batch)

    def _create_vertex_vertices(self):
        return [
            -self._width / 2,  self._height / 2,
             self._width / 2,  self._height / 2,
             self._width / 2, -self._height / 2,
            -self._width / 2, -self._height / 2
        ]

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width    = value
        self._vertices = self._create_vertex_vertices()
        self._update_vertex_vertices()

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height   = value
        self._vertices = self._create_vertex_vertices()
        self._update_vertex_vertices()

    @property
    def lineWidth(self):
        return self._lineWidth

    @lineWidth.setter
    def lineWidth(self, value):
        self._lineWidth = lineWidth
        self._update_vertex_vertices()


# ---------------------------
# Triangle Class
class Polygon(Shape):
    def __init__(self, vertices, mode="line", batch=default_batch):
        x, y, vertices = self._create_vertex_vertices(vertices)
        vertex_mode    = gl.GL_LINE_LOOP if mode == "line" else gl.GL_POLYGON

        super().__init__(x, y, vertices, vertex_mode, mode, batch)

    def _create_vertex_vertices(self, vertices):
        signed_area = 0
        cx = 0
        cy = 0

        for i in range(len(vertices)):
            vertex       = (vertices[i], vertices[(i+1) % len(vertices)])
            area         = vertex[0][0] * vertex[1][1] - vertex[1][0] * vertex[0][1]
            signed_area += area
            cx          += (vertex[0][0] + vertex[1][0]) * area
            cy          += (vertex[0][1] + vertex[1][1]) * area

        signed_area /= 2
        cx          /= 6 * signed_area
        cy          /= 6 * signed_area

        adjusted_vertices = []

        for i in range(len(vertices)):
            adjusted_vertices.append(vertices[i][0] - cx)
            adjusted_vertices.append(vertices[i][1] - cy)

        return cx, cy, adjusted_vertices

# ---------------------------
# Line Class
class Line(Shape):
    def __init__(self, x1, y1, x2, y2, batch=default_batch):
        x = (x2 + x1) / 2
        y = (y2 + y1) / 2

        vertices = []
        vertices.append(x1 - x)
        vertices.append(y1 - y)
        vertices.append(x2 - x)
        vertices.append(y2 - y)

        super().__init__(x, y, vertices, gl.GL_LINES, "line", batch)

# ---------------------------
# Ellipse Class
class Ellipse(Shape):
    def __init__(self, x, y, radiusX, radiusY, mode="line", batch=default_batch):
        self._radiusX = radiusX
        self._radiusY = radiusY

        vertices    = self._create_vertex_vertices()
        vertex_mode = gl.GL_LINE_LOOP if mode == "line" else gl.GL_TRIANGLE_FAN

        super().__init__(x, y, vertices, vertex_mode, mode, batch)

    def _create_vertex_vertices(self):
        vertices = []
        vertex_count = 100

        for i in range(vertex_count):
            angle = radians(float(i) / vertex_count * 360.0)
            x = self._radiusX * cos(angle)
            y = self._radiusY * sin(angle)

            vertices += [x, y]

        return vertices

    @property
    def radiusX(self):
        return self._radiusX

    @radiusX.setter
    def radiusX(self, value):
        self._radiusX  = value
        self._vertices = self._create_vertex_vertices()
        self._update_vertex_vertices()

    @property
    def radiusY(self):
        return self._radiusY

    @radiusY.setter
    def radiusY(self, value):
        self._radiusY  = value
        self._vertices = self._create_vertex_vertices()
        self._update_vertex_vertices()

    @property
    def radius(self):
        return max(self._radiusX, self._radiusY)

    @radius.setter
    def radius(self, value):
        self._radiusX  = value
        self._radiusY  = value
        self._vertices = self._create_vertex_vertices()
        self._update_vertex_vertices()


# ---------------------------
# Circle Class
class Circle(Ellipse):
    def __init__(self, x, y, radius, mode="line", batch=default_batch):
        super().__init__(x, y, radius, radius, mode, batch)