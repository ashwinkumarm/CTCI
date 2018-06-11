'''
Created on 10-Jun-2018

@author: Ashwin
'''

from CTCI.concepts.Node import Node

def intersection(l1, l2):
    tail1, size1 = getTailAndSize(l1)
    tail2, size2 = getTailAndSize(l2)
    
    if tail1 != tail2:
        return None
    
    longer = l1 if size1 > size2 else l2
    shorter = l1 if size1 < size2 else l2
    
    longer = moveByKDist(longer, abs(size1 - size2))
    
    while longer != shorter:
        longer = longer.next
        shorter = shorter.next
    
    return shorter
    
def getTailAndSize(l):
    s = 0
    while l and l.next:
        s +=1
        l = l.next
    s += 1
    
    return l,s

def moveByKDist(l, k):
    while k > 0:
        l = l.next
        k -= 1
        
    return l

node = Node(1, Node(6))
root1 = Node(7,node)
root2 = Node(5,Node(9,node))

print(intersection(root1, root2).value)