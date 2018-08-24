import pyglet
from pybox.graphics import window

class GameWindow(window.Window):
    def __init__(self, registry, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.registry = registry
        self.keys = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keys)

        # View all events
        # self.push_handlers(pyglet.window.event.WindowEventLogger())

    def run(self):
        pyglet.app.run()

    def on_load(self):
        """ On load event. """

        for func in self.registry["load"]:
            func(self.registry["app"])

        self.run()

    def on_update(self, dt):
        if "down" in self.registry["key"]:
            self.registry["key"]["down"](self.keys)

        for func in self.registry["update"]:
            func(dt)

    def on_draw(self):
        super().on_draw()

        for func in self.registry["draw"]:
            func()

        super().debug()

    def on_key_press(self, symbol, modifiers):
        if "press" in self.registry["key"]:
            self.registry["key"]["press"](symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        if "release" in self.registry["key"]:
            self.registry["key"]["release"](symbol, modifiers)

    def on_text(self, text):
        if "text" in self.registry["key"]:
            self.registry["key"]["text"](text)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if "drag" in self.registry["mouse"]:
            self.registry["mouse"]["drag"](x, y, dx, dy, buttons, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        if "motion" in self.registry["mouse"]:
            self.registry["mouse"]["motion"](x, y, dx, dy)

    def on_mouse_press(self, x, y, button, modifiers):
        if "press" in self.registry["mouse"]:
            self.registry["mouse"]["press"](x, y, button, modifiers)

    def on_mouse_release(self, x, y, button, modifiers):
        if "release" in self.registry["mouse"]:
            self.registry["mouse"]["release"](x, y, button, modifiers)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        if "scroll" in self.registry["mouse"]:
            self.registry["mouse"]["scroll"](x, y, scroll_x, scroll_y)

    def on_activate(self):
        if "focus" in self.registry["window"]:
            self.registry["window"]["focus"]()

    def on_deactivate(self):
        if "blur" in self.registry["window"]:
            self.registry["window"]["blur"]()

    def on_hide(self):
        if "hide" in self.registry["window"]:
            self.registry["window"]["hide"]()

    def on_show(self):
        if "show" in self.registry["window"]:
            self.registry["window"]["show"]()

    def on_move(self, x, y):
        if "move" in self.registry["window"]:
            self.registry["window"]["move"](x, y)

class Game():
    registry = {
        "load": [],
        "update": [],
        "draw": [],
        "key": {},
        "mouse": {},
        "focus": {},
        "window": {},
        "app": None
    }

    @classmethod
    def load(cls, func):
        cls.registry["load"].append(func)
        return func

    @classmethod
    def update(cls, func):
        cls.registry["update"].append(func)
        return func

    @classmethod
    def draw(cls, func):
        cls.registry["draw"].append(func)
        return func

    @classmethod
    def key_press(cls, func):
        cls.registry["key"]["press"] = func
        return func

    @classmethod
    def key_release(cls, func):
        cls.registry["key"]["release"] = func
        return func

    @classmethod
    def key_down(cls, func):
        cls.registry["key"]["down"] = func
        return func

    @classmethod
    def text(cls, func):
        cls.registry["key"]["text"] = func
        return func

    @classmethod
    def mouse_drag(cls, func):
        cls.registry["mouse"]["drag"] = func
        return func

    @classmethod
    def mouse_motion(cls, func):
        cls.registry["mouse"]["motion"] = func
        return func

    @classmethod
    def mouse_press(cls, func):
        cls.registry["mouse"]["press"] = func
        return func

    @classmethod
    def mouse_release(cls, func):
        cls.registry["mouse"]["release"] = func
        return func

    @classmethod
    def mouse_scroll(cls, func):
        cls.registry["mouse"]["scroll"] = func
        return func

    @classmethod
    def focus(cls, func):
        cls.registry["window"]["focus"] = func
        return func

    @classmethod
    def blur(cls, func):
        cls.registry["window"]["blur"] = func
        return func

    @classmethod
    def hide(cls, func):
        cls.registry["window"]["hide"] = func
        return func

    @classmethod
    def show(cls, func):
        cls.registry["window"]["show"] = func
        return func

    @classmethod
    def move(cls, func):
        cls.registry["window"]["move"] = func
        return func

    @classmethod
    def run(cls, width=640, height=480, caption="Game"):
        cls.registry["app"] = GameWindow(
            cls.registry,
            width=width,
            height=height,
            caption=caption
        )

        cls.registry["app"].on_load()

