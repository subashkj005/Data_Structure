class StackImplementation:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty:
            return self.stack.pop(-1)
        return []

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return []
