import pyglet

from pybox.graphics import window


class GameWindow(window.Window):
    def __init__(self, registry, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._registry = registry
        self._keys = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self._keys)

        # View all events
        # self.push_handlers(pyglet.window.event.WindowEventLogger())

    def on_load(self):
        """ On load event. Called once and only once. """

        for func in self._registry.get_command("load"):
            func(self._registry.current, self)

    def on_enter(self, prev, *args, **kwargs):
        for func in self._registry.get_command("state_enter"):
            func(self._registry.current, prev, *args, **kwargs)

    def on_leave(self, *args, **kwargs):
        for func in self._registry.get_command("state_leave"):
            func(self._registry.current, *args, **kwargs)

    def on_resume(self):
        for func in self._registry.get_command("state_resume"):
            func(self._registry.current)

    def on_update(self, dt):
        for func in self._registry.get_command("update"):
            func(self._registry.current, dt)

        self.on_key_down()

    def on_draw(self):
        super().on_draw()

        for func in self._registry.get_command("draw"):
            func(self._registry.current)

        super().debug()

    def on_key_press(self, symbol, modifiers):
        for func in self._registry.get_command("key_press"):
            func(self._registry.current, symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        for func in self._registry.get_command("key_release"):
            func(self._registry.current, symbol, modifiers)

    def on_key_down(self):
        for func in self._registry.get_command("key_down"):
            func(self._registry.current, self._keys)

    def on_text(self, text):
        for func in self._registry.get_command("key_text"):
            func(self._registry.current, text)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        for func in self._registry.get_command("mouse_drag"):
            func(self._registry.current, x, y, dx, dy, buttons, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        for func in self._registry.get_command("mouse_motion"):
            func(self._registry.current, x, y, dx, dy)

    def on_mouse_press(self, x, y, button, modifiers):
        for func in self._registry.get_command("mouse_press"):
            func(self._registry.current, x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        for func in self._registry.get_command("mouse_release"):
            func(self._registry.current, x, y, button, modifiers)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        for func in self._registry.get_command("mouse_scroll"):
            func(self._registry.current, x, y, scroll_x, scroll_y)

    def on_activate(self):
        for func in self._registry.get_command("window_focus"):
            func(self._registry.current)

    def on_deactivate(self):
        for func in self._registry.get_command("window_blur"):
            func(self._registry.current)

    def on_hide(self):
        for func in self._registry.get_command("window_hide"):
            func(self._registry.current)

    def on_show(self):
        for func in self._registry.get_command("window_show"):
            func(self._registry.current)

    def on_move(self, x, y):
        for func in self._registry.get_command("window_move"):
            func(self._registry.current, x, y)