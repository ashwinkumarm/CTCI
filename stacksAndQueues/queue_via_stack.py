from CTCI.concepts.Stack import Stack


class QueueViaStack:
    def __init__(self):
        # self.new = Stack()
        # self.old = Stack()
        self.new = []
        self.old = []

    def add(self, item):
        self.new.append(item)

    def remove(self):
        self.shift_stacks()
        if len(self.old) == 0:
            raise Exception("Stack is Empty")
        return self.old.pop()

    def shift_stacks(self):
        if len(self.old) == 0:
            while not len(self.new) == 0:
                self.old.append(self.new.pop())

    def peek(self):
        self.shift_stacks()
        return self.old[-1]


q = QueueViaStack()
q.add(1)
q.add(2)
q.add(3)
print(q.peek())
print(q.remove())
q.add(4)
print(q.remove())
print(q.remove())
print(q.remove())
