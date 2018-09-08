from pyglet.sprite import Sprite
from app.variables import *
from pybox.graphics.drawables import fixture2d
from pybox.physics.aabb import AABB


# ---------------------------
# Sprite2D Class
class Sprite2D(fixture2d.Fixture2D):
    def __init__(self, img, x, y, batch=default_batch, group=None):
        self._sprite = Sprite(img, x=x, y=y, batch=batch, group=group)

        super().__init__(x, y)

    def update(self, dt):
        super().update(dt)

        self._sprite.update(x=self._pos.x, y=self._pos.y, rotation=self._rot, scale_x=self._sx, scale_y=self._sy)

    def delete(self):
        super().delete()

        self._sprite.delete()

    def _create_physical_body(self):
        return pymunk.Body(self._mass, self._inertia, self._body_type)

    def _create_physical_shape(self):
        return pymunk.Poly(self._body, [
            (-self.width / 2,  self.height / 2),
            ( self.width / 2,  self.height / 2),
            ( self.width / 2, -self.height / 2),
            (-self.width / 2, -self.height / 2)
        ])

    def _get_inertia_for_shape(self):
        return pymunk.moment_for_poly(self._mass, [
            (-self.width / 2,  self.height / 2),
            ( self.width / 2,  self.height / 2),
            ( self.width / 2, -self.height / 2),
            (-self.width / 2, -self.height / 2)
        ])

    def _get_bounding_box(self):
        return AABB.computeAABB(self.x, self.y, self.width, self.height, self._rot)

    @property
    def width(self):
        return self._sprite.width

    @property
    def height(self):
        return self._sprite.height

    @property
    def batch(self):
        return self._sprite.batch

    @batch.setter
    def batch(self, value):
        self._sprite.batch = value

    @property
    def image(self):
        return self._sprite.image

    @image.setter
    def image(self, value):
        self._sprite.image = value

    @property
    def group(self):
        return self._sprite.group

    @group.setter
    def group(self, value):
        self._sprite.group = value

    @property
    def opacity(self):
        return self._sprite.opacity

    @opacity.setter
    def opacity(self, value):
        self._sprite.opacity = value

    @property
    def color(self):
        return self._sprite.color

    @color.setter
    def color(self, value):
        self._sprite.color = value

    @property
    def visible(self):
        return self._sprite.visible

    @visible.setter
    def visible(self, value):
        self._sprite.visible = value

