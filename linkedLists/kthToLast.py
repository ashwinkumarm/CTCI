'''
Created on 09-Jun-2018

@author: Ashwin
'''

from CTCI.concepts.Node import Node


def kth_last_recursive(head, k):
    return _kth_last_recursive(head, k)[0].value


def _kth_last_recursive(head, k):
    if head is None:
        return None, 0
    
    node, v = _kth_last_recursive(head.next, k)
    v += 1
    
    if v == k:
        return head, v
    
    return node, v

    
def length(head):
    c = 0
    while head:
        c += 1
        head = head.next
    return c

def kth_last(head, k):
    l = length(head)
    i = l - k
    while i > 0:
        head = head.next
        i -= 1
    return head.value  


def kth_last_pointers(head, k):
    pointer1 = head
    pointer2 = head
    while k > 0:
        pointer2 = pointer2.next
        k -= 1
    
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    
    return pointer1.value


root = Node(5)
root.next = node3 = Node(3)
node3.next = node7 = Node(7)
node7.next = node1 = Node(1)
node1.next = node3t = Node(3)
node3t.next = node6 = Node(6)

print(kth_last_recursive(root, 2))
#print(kthToLast2Pointers(root,2))
#print(kthToLast(root,2))