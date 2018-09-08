from itertools import chain
from math import radians, cos, sin
from pyglet.gl import gl
from app.variables import *
from pybox.graphics.drawables import fixture2d
from pybox.graphics.groups import transform, blend, line
from pybox.physics.aabb import AABB

# ---------------------------
# Shape2D Class
class Shape2D(fixture2d.Fixture2D):
    def __init__(self, x, y, vertices, vertex_mode, batch):
        self._batch     = batch
        self._lineWidth = 1
        self._vertices  = vertices

        self._vertex_list   = None
        self._vertex_groups = {}
        self._vertex_mode   = vertex_mode
        self._vertex_color  = (255, 255, 255, 255)

        super().__init__(x, y)

        self._create_vertex_groups()
        self._create_vertex_list_data()

    def _create_vertex_list_data(self):
        self._vertex_list = self._batch.add(
            len(self._vertices),                     # Vertex count
            self._vertex_mode,                       # Vertex draw mode
            list(self._vertex_groups.values())[-1],  # Vertex group
            "v2f", "c4B", "t3f"
        )

        self._update_vertex_vertices()
        self._update_vertex_color()

    def _create_vertex_groups(self):
        transformGroup = transform.TransformGroup(self._pos.x, self._pos.y, self._rot, self._sx, self._sy)
        blendGroup     = blend.BlendGroup(parent=transformGroup)
        lineGroup      = line.LineGroup(self._lineWidth, parent=blendGroup)

        self._vertex_groups["transform"] = transformGroup
        self._vertex_groups["blend"]     = blendGroup
        self._vertex_groups["line"]      = lineGroup

    """
        Update vertex list vertices.
    """
    def _update_vertex_vertices(self):
        self._vertex_list.vertices = list(chain.from_iterable(self._vertices))

    """
        Update vertex list colors.
    """
    def _update_vertex_color(self):
        self._vertex_list.colors = self._vertex_color * self._vertex_list.get_size()

    """
        Update shape transformation.
    """
    def _update_vertex_transform(self):
        self._vertex_groups["transform"].x        = self._pos.x
        self._vertex_groups["transform"].y        = self._pos.y
        self._vertex_groups["transform"].rotation = self._rot
        self._vertex_groups["transform"].sx       = self._sx
        self._vertex_groups["transform"].sy       = self._sy

    def _create_physical_body(self):
        return pymunk.Body(self._mass, self._inertia, self._body_type)

    def _create_physical_shape(self):
        return pymunk.Poly(self._body, self._vertices)

    def _get_inertia_for_shape(self):
        return pymunk.moment_for_poly(self._mass, self._vertices)

    def _get_bounding_box(self):
        return AABB.compute(self._vertices, self._vertex_groups["transform"].matrix)

    """
        Submit request for shape transformation properties
            to be updated.
    """
    def update(self, dt):
        super().update(dt)

        self._update_vertex_transform()

    """
        Force immediate removal of vertex list from video memory.
    """
    def delete(self):
        super().delete()

        self._vertex_list.delete()

    @property
    def vertices(self):
        return self._vertices

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
class Rectangle(Shape2D):
    def __init__(self, x, y, width, height, mode="line", batch=default_batch):
        self._width   = width
        self._height  = height

        vertices    = self._create_vertex_vertices()
        vertex_mode = gl.GL_LINE_LOOP if mode == "line" else gl.GL_QUADS

        super().__init__(x, y, vertices, vertex_mode, batch)

    def _create_vertex_vertices(self):
        return [
            (-self._width / 2,  self._height / 2),
            ( self._width / 2,  self._height / 2),
            ( self._width / 2, -self._height / 2),
            (-self._width / 2, -self._height / 2)
        ]

    def _get_inertia_for_shape(self):
        return pymunk.moment_for_box(self._mass, (self._width, self._height))

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

# ---------------------------
# Polygon Class
class Polygon(Shape2D):
    def __init__(self, vertices, mode="line", batch=default_batch):
        cx, cy, width, height, vertices = self._create_vertex_vertices(vertices)
        vertex_mode    = gl.GL_LINE_LOOP if mode == "line" else gl.GL_POLYGON

        self._cx = cx
        self._cy = cy
        self._width = width
        self._height = height

        super().__init__(cx, cy, vertices, vertex_mode, batch)

    def _create_vertex_vertices(self, vertices):
        signed_area = 0
        cx = 0
        cy = 0
        xmin = float('inf')
        ymin = float('inf')
        xmax = 0
        ymax = 0

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
            x = vertices[i][0]
            y = vertices[i][1]

            xmin = min(xmin, x)
            ymin = min(ymin, y)
            xmax = max(xmax, x)
            ymax = max(ymax, y)

            adjusted_vertices.append((x - cx, y - cy))

        return cx, cy, xmax-xmin, ymax-ymin, adjusted_vertices

    @property
    def cx(self):
        return self._cx

    @property
    def cy(self):
        return self._cy

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

# ---------------------------
# Segment Class
class Segment(Shape2D):
    def __init__(self, x1, y1, x2, y2, batch=default_batch):
        cx, cy, vertices = self._create_vertex_vertices(x1, y1, x2, y2)

        self._cx     = cx
        self._cy     = cy
        self._width  = max(vertices[0][0], vertices[1][0]) - min(vertices[0][0], vertices[1][0])
        self._height = max(vertices[0][1], vertices[1][1]) - min(vertices[0][1], vertices[1][1])

        super().__init__(cx, cy, vertices, gl.GL_LINES, batch)

    def _create_vertex_vertices(self, x1, y1, x2, y2):
        cx       = (x2 + x1) / 2
        cy       = (y2 + y1) / 2
        vertices = [(x1 - cx, y1 - cy), (x2 - cx, y2 - cy)]

        return cx, cy, vertices

    def _create_physical_shape(self):
        return pymunk.Segment(
            self._body,
            (self._vertices[0][0], self._vertices[0][1]),
            (self._vertices[1][0], self._vertices[1][1]),
            0.0
        )

    def _get_inertia_for_shape(self):
        return pymunk.moment_for_segment(
            self._mass,
            (self._vertices[0][0], self._vertices[0][1]),
            (self._vertices[1][0], self._vertices[1][1]),
            0.0
        )

    @property
    def cx(self):
        return self._cx

    @property
    def cy(self):
        return self._cy

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

# ---------------------------
# Ellipse Class
class Ellipse(Shape2D):
    def __init__(self, x, y, radiusX, radiusY, segments=25, mode="line", batch=default_batch):
        self._radiusX = radiusX
        self._radiusY = radiusY
        self._segments = segments

        vertices    = self._create_vertex_vertices()
        vertex_mode = gl.GL_LINE_LOOP if mode == "line" else gl.GL_TRIANGLE_FAN

        super().__init__(x, y, vertices, vertex_mode, batch)

    def _create_vertex_vertices(self):
        vertices = []

        for i in range(self._segments):
            angle = radians(float(i) / self._segments * 360.0)
            x = self._radiusX * cos(angle)
            y = self._radiusY * sin(angle)

            vertices += [(x, y)]

        return vertices

    def _get_bounding_box(self):
        return AABB.compute([
            (-self._radiusX,  self._radiusY),
            ( self._radiusX,  self._radiusY),
            ( self._radiusX, -self._radiusY),
            (-self._radiusX, -self._radiusY)
        ], self._vertex_groups["transform"].matrix)

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

    @property
    def segments(self):
        return self._segments

    @segments.setter
    def segments(self, value):
        self._segments  = value
        self._vertices = self._create_vertex_vertices()
        self._update_vertex_vertices()


# ---------------------------
# Circle Class
class Circle(Ellipse):
    def __init__(self, x, y, radius, segments=25, mode="line", batch=default_batch):
        super().__init__(x, y, radius, radius, segments, mode, batch)

    def _create_physical_shape(self):
        return pymunk.Circle(self._body, self.radius)

    def _get_inertia_for_shape(self):
        return pymunk.moment_for_circle(self._mass, 0, self.radius)

# ---------------------------
# Arc Class
class Arc(Shape2D):
    def __init__(self, x, y, radius, angle1, angle2, segments=25, mode="line", batch=default_batch):
        self._radius = radius
        self._angle1 = angle1
        self._angle2 = angle2
        self._segments = segments

        vertices = self._create_vertex_vertices()
        vertex_mode = gl.GL_LINE_LOOP if mode == "line" else gl.GL_TRIANGLE_FAN

        super().__init__(x, y, vertices, vertex_mode, batch)

    def _create_vertex_vertices(self):
        vertices = [(0, 0)]

        for i in range(self._segments + 1):
            angle = radians(float(i) / self._segments * (self._angle2 - self._angle1))

            x = self._radius * cos(angle)
            y = self._radius * sin(angle)

            vertices.append((x, y))

        return vertices

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius  = value
        self._vertices = self._create_vertex_vertices()
        self._update_vertex_vertices()

    @property
    def segments(self):
        return self._segments

    @segments.setter
    def segments(self, value):
        self._segments  = value
        self._vertices = self._create_vertex_vertices()
        self._update_vertex_vertices()
