import pyglet
import pymunk


BODY_TYPE_RIGID     = pymunk.Body.DYNAMIC
BODY_TYPE_KINEMATIC = pymunk.Body.KINEMATIC
BODY_TYPE_STATIC    = pymunk.Body.STATIC


default_batch = pyglet.graphics.Batch()
