from pybox.containers import stack

class Registry:
    def __init__(self):
        self._window = None
        self._states = stack.Stack()
        self._init_states = []
        self._commands = {}

    def add_command(self, name, command):
        command_name = command.__qualname__
        state, func  = command_name.split(".")

        if name not in self._commands:
            self._commands[name] = {}

        if state not in self._commands[name]:
            self._commands[name][state] = []

        self._commands[name][state].append(command)

    def get_command(self, name):
        state = self.current.__class__.__name__

        if name in self._commands:
            if state in self._commands[name]:
                return self._commands[name][state]

        return []

    def change_state(self, from_state, to_state, *args, **kwargs):
        if from_state is not None:
            self._window.on_leave(*args, **kwargs)

        self._states.push(to_state)

        if to_state.__class__.__name__ not in self._init_states:
            self._window.on_load()
            self._init_states.append(to_state.__class__.__name__)

        self._window.on_enter(from_state, *args, **kwargs)

    def switch(self, state, *args, **kwargs):
        self.change_state(self._states.pop(), state, *args, **kwargs)

    def push(self, state, *args, **kwargs):
        self.change_state(self.current, state, *args, **kwargs)

    def pop(self, *args, **kwargs):
        if len(self._states) <= 1:
            raise Exception("Nothing to pop!")

        self._window.on_leave(*args, **kwargs)
        self._states.pop()
        self._window.on_resume(*args, **kwargs)

    @property
    def current(self):
        return self._states.peek()

    @property
    def states(self):
        return self._states

    @property
    def commands(self):
        return self._commands

    @property
    def window(self):
        return self._window

    @window.setter
    def window(self, value):
        self._window = value
