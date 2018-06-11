class IteratorUpperLimit:

    def __init__(self, high):
        self.high = high

    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        if self.x >= self.high:
            raise StopIteration

        self.x += 1
        return self.x

class Repeater:

    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value



iter = IteratorUpperLimit(15)

for i in iter:
    print(i, end = '')

for r in Repeater('a'):
    print(r, end = '')


