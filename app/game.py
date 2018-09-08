from .registry import Registry
from .window import GameWindow


class Game:
    registry = Registry()

    @classmethod
    def load(cls, func):
        cls.registry.add_command("load", func)
        return func

    @classmethod
    def update(cls, func):
        cls.registry.add_command("update", func)
        return func

    @classmethod
    def draw(cls, func):
        cls.registry.add_command("draw", func)
        return func

    @classmethod
    def key_press(cls, func):
        cls.registry.add_command("key_press", func)
        return func

    @classmethod
    def key_release(cls, func):
        cls.registry.add_command("key_release", func)
        return func

    @classmethod
    def key_down(cls, func):
        cls.registry.add_command("key_down", func)
        return func

    @classmethod
    def text(cls, func):
        cls.registry.add_command("key_text", func)
        return func

    @classmethod
    def mouse_drag(cls, func):
        cls.registry.add_command("mouse_drag", func)
        return func

    @classmethod
    def mouse_motion(cls, func):
        cls.registry.add_command("mouse_motion", func)
        return func

    @classmethod
    def mouse_press(cls, func):
        cls.registry.add_command("mouse_press", func)
        return func

    @classmethod
    def mouse_release(cls, func):
        cls.registry.add_command("mouse_release", func)
        return func

    @classmethod
    def mouse_scroll(cls, func):
        cls.registry.add_command("mouse_scroll", func)
        return func

    @classmethod
    def focus(cls, func):
        cls.registry.add_command("window_focus", func)
        return func

    @classmethod
    def blur(cls, func):
        cls.registry.add_command("window_blur", func)
        return func

    @classmethod
    def hide(cls, func):
        cls.registry.add_command("window_hide", func)
        return func

    @classmethod
    def show(cls, func):
        cls.registry.add_command("window_show", func)
        return func

    @classmethod
    def move(cls, func):
        cls.registry.add_command("window_move", func)
        return func

    @classmethod
    def enter(cls, func):
        cls.registry.add_command("state_enter", func)
        return func

    @classmethod
    def leave(cls, func):
        cls.registry.add_command("state_leave", func)
        return func

    @classmethod
    def resume(cls, func):
        cls.registry.add_command("state_resume", func)
        return func

    @classmethod
    def switch(cls, state, *args, **kwargs):
        cls.registry.switch(state, *args, **kwargs)

    @classmethod
    def push(cls, state, *args, **kwargs):
        cls.registry.push(state, *args, **kwargs)

    @classmethod
    def pop(cls, *args, **kwargs):
        cls.registry.pop(*args, **kwargs)

    @classmethod
    def run(cls, width=640, height=480, caption="Game"):
        cls.registry.window = GameWindow(cls.registry, width=width, height=height, caption=caption)


