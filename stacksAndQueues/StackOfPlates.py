class StackOfPlates:
    def __init__(self, threshold):
        self.threshold = threshold
        self.items = []

    def push(self, item):
        if len(self.items) and len(self.items[-1]) < self.threshold:
            self.items[-1].append(item)
        else:
            self.items.append([item])

    def pop(self):
        if len(self.items) == 0:
            raise Exception('Stack is Empty')
        item = self.items[-1].pop()
        if len(self.items[-1]) == 0:
            self.items.pop()
        return item


s = StackOfPlates(3)
s.push(0)
print(s.pop())
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(len(s.items))
print(s.pop())
print(s.pop())
print(len(s.items))