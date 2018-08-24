import pyglet

class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._fps_display = pyglet.window.FPSDisplay(self)
        self.fps = 1 / 120.0

    @property
    def fps(self):
        return self._fps

    @fps.setter
    def fps(self, value):
        self._fps = value

        pyglet.clock.unschedule(self.tick)
        pyglet.clock.schedule_interval(self.tick, value)

    def tick(self, dt):
        self.on_update(dt)
        self.on_draw()

    def on_update(self, dt):
        """override this"""
        pass

    def on_draw(self):
        self.clear()

    def debug(self):
        self._fps_display.draw()
