from CTCI.concepts.Node import Node


def is_palindrome(ll):
    slow = ll
    fast = ll
    stack = []
    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    
    if fast:
        slow = slow.next
    
    while stack:
        if slow.value != stack.pop():
            return False
        slow = slow.next
    return True


root = Node(6,Node(1,Node(6)))
print(is_palindrome(root))