class ThreeInOne:
    def __init__(self, size):
        self.arraySize = size
        self.list = [[] for _ in range(3)]

    def isFull(self, stackNo):
        if self.list[stackNo]:
            return len(self.list[stackNo]) == self.arraySize / 3

        return False

    def isEmpty(self, stackNo):
        if self.list[stackNo]:
            return len(self.list[stackNo]) == 0

        return True

    def push(self, stackNo, value):
        if self.isFull(stackNo):
            raise Exception('Stack is full')
        self.list[stackNo].append(value)

    def pop(self, stackNo):
        if self.isEmpty(stackNo):
            raise Exception('Stack is Empty')

        return self.list[stackNo].pop()

    def peek(self, stackNo):
        if self.isEmpty(stackNo):
            raise Exception('Stack is Empty')

        indList = self.list[stackNo]
        return indList[len(indList) - 1]


a = ThreeInOne(15)
a.push(0,2)
a.push(1,2)
a.push(2,2)
print(a.pop(0))
a.push(0, 1)
a.push(1, 1)
a.push(2, 1)
print(a.pop(0))
print(a.pop(1))
print(a.peek(2))
a.push(2, 3)
a.push(2, 4)
a.push(2, 5)
#a.push(2, 6)
#print(a.peek(2))
#print(a.pop(0))