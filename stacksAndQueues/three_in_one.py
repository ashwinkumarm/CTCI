class ThreeInOne:
    def __init__(self, size):
        self.arraySize = size
        self.list = [[] for _ in range(3)]

    def is_full(self, stack_no):
        if self.list[stack_no]:
            return len(self.list[stack_no]) == self.arraySize / 3
        return False

    def is_empty(self, stack_no):
        if self.list[stack_no]:
            return len(self.list[stack_no]) == 0
        return True

    def push(self, stack_no, value):
        if self.is_full(stack_no):
            raise Exception('Stack is full')
        self.list[stack_no].append(value)

    def pop(self, stack_no):
        if self.is_empty(stack_no):
            raise Exception('Stack is Empty')
        return self.list[stack_no].pop()

    def peek(self, stack_no):
        if self.is_empty(stack_no):
            raise Exception('Stack is Empty')
        ind_list = self.list[stack_no]
        return ind_list[-1]


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