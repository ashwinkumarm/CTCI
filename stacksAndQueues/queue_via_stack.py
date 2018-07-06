from CTCI.concepts.Stack import Stack


class QueueViaStack:
    def __init__(self):
        self.new = Stack()
        self.old = Stack()

    def add(self, item):
        self.new.push(item)

    def remove(self):
        self.shift_stacks()
        if self.old.is_empty():
            raise Exception("Stack is Empty")
        return self.old.pop()

    def shift_stacks(self):
        if self.old.is_empty():
            while not self.new.is_empty():
                self.old.push(self.new.pop())

    def peek(self):
        self.shift_stacks()
        return self.old.peek()


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
