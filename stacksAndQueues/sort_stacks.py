from CTCI.concepts.Stack import Stack


def sort_stack(stack):
    r = Stack()
    while not stack.is_empty():
        tmp = stack.pop()
        while not r.is_empty() and r.peek() > tmp:
            stack.push(r.pop())
        r.push(tmp)

    while not r.is_empty():
        stack.push(r.pop())


s = Stack()
s.push(2)
s.push(5)
s.push(1)
s.push(19)
sort_stack(s)

while not s.is_empty():
    print(s.pop(), end=' ')