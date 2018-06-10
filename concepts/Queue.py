
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def enqueue(self, x):
        return self.items.insert(0, x)

    def dequeue(self):
        return self.items.pop()
    