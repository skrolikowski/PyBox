from math import degrees
from app.variables import *
from pybox.graphics.drawables import entity2d

class Fixture2D(entity2d.Entity2D):
    def __init__(self, x, y):
        super().__init__(x, y)

        self._body      = None
        self._shape     = None
        self._body_type = BODY_TYPE_KINEMATIC

    def add(self, space, **kwargs):
        self._mass      = kwargs.get('mass', self._mass)
        self._body_type = kwargs.get('body_type', BODY_TYPE_KINEMATIC)

        self._apply_physics()

        self.elasticity = kwargs.get('elasticity', self.elasticity)
        self.friction   = kwargs.get('friction', self.friction)

        space.add(self._body, self._shape)

    def update(self, dt):
        if self._body_type == BODY_TYPE_KINEMATIC:
            super().update(dt)
        else:
            self._pos.x = self._body.position.x
            self._pos.y = self._body.position.y
            self._rot   = degrees(-self._body.angle)

    def delete(self):
        if self._body and self._shape:
            for constraint in self._body.constraints:
                self.space.remove(constraint)

            self.space.remove(self._body, self._shape)

    def apply_force(self, force, point=(0,0)):
        if self._body:
            self._body.apply_force_at_local_point(force, point)
        else:
            super().apply_force(force, point)

    def apply_impulse(self, impulse, point=(0,0)):
        if self._body:
            self._body.apply_impulse_at_local_point(impulse, point)
        else:
            super().apply_impulse(impulse, point)

    def _apply_physics(self):
        self._inertia       = self._get_inertia_for_shape()
        self._body          = self._create_physical_body()
        self._body.position = self._pos.x, self._pos.y
        self._shape         = self._create_physical_shape()

    def _get_inertia_for_shape(self):
        """Override in child class."""
        pass

    def _create_physical_body(self):
        """Override in child class."""
        pass

    def _create_physical_shape(self):
        """Override in child class."""
        pass

    def _get_bounding_box(self):
        """Override in child class."""
        pass

    def debug(self):
        if self._shape is None:
            self.aabb.draw()

    def collision_begin(self, arbiter, space, data):
        raise NotImplementedError('abstract')

    def collision_pre_solve(self, arbiter, space, data):
        raise NotImplementedError('abstract')

    def collision_post_solve(self, arbiter, space, data):
        raise NotImplementedError('abstract')

    def collision_end(self, arbiter, space, data):
        raise NotImplementedError('abstract')

    @property
    def body(self):
        return self._body

    @property
    def shape(self):
        return self._shape

    @property
    def space(self):
        return self._shape.space

    @property
    def density(self):
        return self._shape.density

    @density.setter
    def density(self, value):
        self._shape.density = value

    @property
    def elasticity(self):
        return self._shape.elasticity

    @elasticity.setter
    def elasticity(self, value):
        self._shape.elasticity = value

    @property
    def friction(self):
        return self._shape.friction

    @friction.setter
    def friction(self, value):
        self._shape.friction = value

    @property
    def bounds(self):
        return self.aabb.left, self.aabb.bottom, self.aabb.right, self.aabb.top

    @property
    def aabb(self):
        if self._shape:
            return self._shape.bb
        else:
            return self._get_bounding_box()

    @property
    def collision_type(self):
        return self._shape.collision_type

    @collision_type.setter
    def collision_type(self, value):
        self._shape.collision_type = value