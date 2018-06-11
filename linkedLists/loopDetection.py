'''
Created on 10-Jun-2018

@author: Ashwin
'''
from CTCI.linkedLists.Node import Node

def intersection(ll):
    slow = ll
    fast = ll
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    if fast is None or fast.next is None:
        return None
    
    slow = ll
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow
    
root = Node(1)
node2 = Node(2)
node3 = Node(3)

root.next = node2
node2.next = node3
node3.next = node2

print(intersection(root).value)
