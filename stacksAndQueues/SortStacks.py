from CTCI.concepts.Stack import Stack


def sortStack(s):
    r = Stack()
    while not s.isEmpty():
        tmp = s.pop()
        while not r.isEmpty() and r.peek() > tmp:
            s.push(r.pop())
        r.push(tmp)

    while not r.isEmpty():
        s.push(r.pop())



s = Stack()
s.push(2)
s.push(5)
s.push(1)
s.push(19)

sortStack(s)

while not s.isEmpty():
    print s.pop(),



