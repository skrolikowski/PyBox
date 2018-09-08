from pybox.containers import stack

class GameStates:
    def __init__(self, window):
        self.window = window
        self.states = stack.Stack()

    def switch(self, state, *args, **kwargs):
        self.states.push(state)
        self.window.on_enter(self.current, self.states.peek(), *args, **kwargs)

    def push(self, state, *args, **kwargs):
        pass

    def pop(self, *args, **kwargs):
        if len(self.states.elements) <= 1:
            raise Exception("No states to pop!")

        self.window.on_leave(self.states.pop(), *args, **kwargs)
        self.window.on_resume(self.states.peek(), *args, **kwargs)

    def current(self):
        return self.states.peek()
