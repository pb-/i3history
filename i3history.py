import i3ipc


class History(object):
    def __init__(self, max_size):
        self.max_size = max_size
        self.undo = []
        self.redo = []

    def push(self, current):
        if self.undo and self.undo[-1] == current:
            return current

        self.undo.append(current)
        self.undo = self.undo[-self.max_size:]
        self.redo = []
        return current

    @staticmethod
    def _move(from_stack, to_stack, current):
        try:
            new = from_stack.pop()
            to_stack.append(current)
            return new
        except IndexError:
            return None

    def backward(self, current):
        return self._move(self.undo, self.redo, current)

    def forward(self, current):
        return self._move(self.redo, self.undo, current)


def navigate(i3, num):
    if num is not None:
        i3.ignore = True
        i3.command('workspace {}'.format(num))


def current_workspace(i3):
    focused = i3.get_tree().find_focused()
    if focused.type == 'workspace':
        return focused
    else:
        return focused.workspace()


def on_binding(i3, e):
    cmd = e.binding.command
    current = current_workspace(i3).num

    if cmd == 'nop history_backward':
        navigate(i3, i3.history.backward(current))
    elif cmd == 'nop history_forward':
        navigate(i3, i3.history.forward(current))


def on_workspace_focus(i3, e):
    if not i3.ignore:
        i3.history.push(e.old.num)

    i3.ignore = False


def run():
    i3 = i3ipc.Connection()
    i3.ignore = False
    i3.history = History(10)
    i3.on('binding', on_binding)
    i3.on('workspace::focus', on_workspace_focus)

    i3.main()
