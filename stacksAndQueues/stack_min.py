import sys


class StackMin:
    def __init__(self):
        self.items = []
        self.min = [sys.maxsize]

    def push(self, x):
        if x <= self.min[-1]:
            self.min.append(x)
        self.items.append(x)

    def pop(self):
        item = self.items.pop()
        if item == self.min[-1]:
            self.min.pop()
        return item

    def peek(self):
        return self.items[len(self.items) - 1]

    def get_min(self):
        return self.min[-1]


stack = StackMin()
stack.push(0)
stack.push(1)
stack.push(0)
print(stack.get_min())
print(stack.pop())
print(stack.get_min())

