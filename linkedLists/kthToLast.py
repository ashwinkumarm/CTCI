'''
Created on 09-Jun-2018

@author: Ashwin
'''

from CTCI.linkedLists.Node import Node

class Index:
    def __init__(self):
        self.value = 0
        

def kthToLastRecursive(head, k):
    index = Index()
    v = 0
    return kthToLastRecursiveL(head, k)[0].value
    
def kthToLastRecursiveL(head, k):
    if head == None:
        return None,0
    
    node,v = kthToLastRecursiveL(head.next, k)
    v += 1
    
    if v == k:
        return head,v
    
    return node,v
    
def length(head):
    c = 0
    while head:
        c += 1
        head = head.next
    return c

def kthToLast(head,k):
    l = length(head)
    i = l - k
    while i > 0:
        head = head.next
        i -=1
    return head.value  

def kthToLast2Pointers(head, k):
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
node3t.next =  node6 = Node(6)

print(kthToLastRecursive(root,2))
#print(kthToLast2Pointers(root,2))
#print(kthToLast(root,2))