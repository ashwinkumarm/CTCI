from collections import deque

class ZigZag():
    def __init__(self, *lists):
        self.queue = deque()
        for list in lists:
            self.queue.append(list)

    def next(self):
        while self.queue:
            list = self.queue.popleft()
            if list:
                ele = list[0]
                self.queue.append(list[1:])
                return ele
        else:
            raise StopIteration()

    def __iter__(self):
        return self


z = ZigZag([1,2,3,4,5], [6,7,8], [9,10,11])
i = 0
while z:
    print(z.next())
