import pyglet

from pyglet.resource import ResourceNotFoundException

class ResourceManager:
    def __init__(self, path=None):
        self._resource = pyglet.resource
        self._images = {}

        self.path = path

    def add_image(self, name, index, flip_x=False, flip_y=False, rotate=0, atlas=True):
        try:
            image = self._resource.image(name, flip_x, flip_y, rotate, atlas)

            image.anchor_x = image.width // 2
            image.anchor_y = image.height // 2

            self._images[index] = image

        except ResourceNotFoundException as err:
            print("Resource Not Found: {0}".format(err))

    def get_image(self, index):
        return self._images[index]

    def get_image_texture(self, index, rectangle=False, force_rectangle=False):
        return self._images[index].get_texture(rectangle, forece_rectangle)

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
        self._resource.path = value
        self._resource.reindex()
