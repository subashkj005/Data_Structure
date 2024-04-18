class StackAsQueue:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return None
        elif len(self.stack) == 1:
            return self.stack.pop(0)
        else:
            n = len(self.stack)
            for _ in range(n - 1):
                self.stack.insert(0, self.stack.pop(-1))
            return self.stack.pop(-1)

    def peek(self):
        value = 0
        if self.is_empty():
            return None
        elif len(self.stack) == 1:
            return self.stack[0]
        else:
            for i in range(len(self.stack)):
                if i == len(self.stack) - 1:
                    value = self.stack[len(self.stack) - 1]
                self.stack.insert(0, self.stack.pop(-1))
            return value


x = StackAsQueue()
x.push(1)
x.push(2)
x.push(3)
x.push(4)
x.push(5)
# print(x.pop())
print(x.pop())
print(x.peek())
print(x.peek())

