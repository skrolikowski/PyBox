from pybox.math import vec2d


class Entity2D:
    def __init__(self, x, y):
        self._pos = vec2d.Vec2D(x, y)

        self._vel = vec2d.Vec2D()
        self._av  = 0.0

        self._forces = vec2d.Vec2D()
        self._torque = 0.0
        self._cog    = vec2d.Vec2D()

        self._rot = 0
        self._sx  = 1
        self._sy  = 1

        self._mass      = 1
        self._inertia   = 100

        self._speed     = 10
        self._max_vel   = self._speed

    def update(self, dt):
        self._update_position(dt)

    def _update_position(self, dt):
        self._update_velocity(dt)

        self._pos += self._vel * dt
        self._rot += self._av * dt

    def _update_velocity(self, dt):
        # Apply world forces
        # self.apply_gravity(self._cell.gravity)
        # self.apply_force(self._cell.wind)
        # self.apply_friction(self._cell.friction)
        # self.apply_drag(self._cell.drag)

        # Velocity
        self._vel += (self._forces / self._mass) * dt
        self._vel.limit(self._max_vel)

        # Angular velocity
        self._av += (self._torque / self._inertia) * dt

        # Reset forces
        self._forces.scale(0)
        self._torque = 0.0

    def apply_force(self, force, point=(0, 0)):
        point  = vec2d.Vec2D(point[0], point[1])
        point -= self._cog

        force = vec2d.Vec2D(force[0], force[1])

        self._forces += force
        self._torque += point.cross(force)

    def apply_impulse(self, impulse, point=(0, 0)):
        point  = vec2d.Vec2D(point[0], point[1])
        point -= self._cog

        impulse  = vec2d.Vec2D(impulse[0], impulse[1])
        impulse /= self._mass

        self._vel += impulse
        self._av  += point.cross(impulse) / self._inertia

    def apply_friction(self, coefficent):
        force = self._vel.copy()
        force.normalize()
        force.scale(-1 * coefficent)

        self.apply_force(force)

    def apply_drag(self, coefficent):
        force = self._vel.copy()
        force.normalize()
        force.scale(coefficent * self._vel.magnitudeSq())

    def apply_gravity(self, gravity):
        self._vel += gravity

    @property
    def position(self):
        return self._pos

    @position.setter
    def position(self, value):
        self._pos = value

    @property
    def x(self):
        return self._pos.x

    @x.setter
    def x(self, value):
        self._pos.x = value

    @property
    def y(self):
        return self._pos.y

    @y.setter
    def y(self, value):
        self._pos.y = value

    @property
    def sx(self):
        return self._sx

    @sx.setter
    def sx(self, value):
        self._sx = value

    @property
    def sy(self):
        return self._sy

    @sy.setter
    def sy(self, value):
        self._sy = value

    @property
    def rotation(self):
        return self._rot

    @rotation.setter
    def rotation(self, value):
        self._rot = value

    @property
    def mass(self):
        return self._mass

    @property
    def inertia(self):
        return self._inertia

    @property
    def rotation_vector(self):
        return vec2d.Vec2D(1, 0).rotate(self._rot)

    @property
    def velocity(self):
        return self._vel

    @property
    def angular_velocity(self):
        return self._av

    @property
    def torque(self):
        return self._torque

    @property
    def forces(self):
        return self._forces
