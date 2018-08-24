import pybox
import pymunk

from pybox.variables import *


# ---------------------------
# Shape Class
class Shape(pybox.graphics.shape2d.Shape):

    def update(self, **kwargs):
        self.radius = self._shape.radius

        super().update(
            x=self._body.position.x,
            y=self._body.position.y,
            angle=self._body.angle
        )

    def delete(self, space):
        space.remove(self._shape, self._body)

        super().delete()

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value):
        self._mass = value
        self._body.mass = value

    @property
    def moment(self):
        return self._moment

    @moment.setter
    def moment(self, value):
        self._moment = value
        self._body.moment = value

    @property
    def body(self):
        return self._body

    @property
    def shape(self):
        return self._shape

    @property
    def area(self):
        return self._shape.area

    @property
    def angular_velocity(self):
        return self._body.angular_velocity

    @property
    def center_of_gravity(self):
        return self._body.center_of_gravity


    @property
    def body_type(self):
        return self._body_type

    @body_type.setter
    def body_type(self, value):
        self._body_type = value
        self._body.body_type = value

# ---------------------------
# Rectangle Class
class Rectangle(pybox.graphics.shape2d.Rectangle, Shape):
    def __init__(self, x, y, width, height, mode="line", mass=1, body_type=BODY_TYPE_RIGID, batch=default_batch):
        super().__init__(x, y, width, height, mode, batch)

        self._mass = mass
        self._moment = pymunk.moment_for_box(mass, (width, height))
        self._body_type = body_type
        self._body = pymunk.Body(mass, self._moment, body_type)
        self._body.position = x, y

        self._shape = pymunk.Poly(self._body, [
                (-width / 2, -height / 2),
                ( width / 2, -height / 2),
                ( width / 2,  height / 2),
                (-width / 2,  height / 2)
            ], None, 0.0)


