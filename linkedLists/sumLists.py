'''
Created on 09-Jun-2018

@author: Ashwin
'''

from CTCI.linkedLists.Node import Node


def sumLists(ll1, ll2):
    c = 0
    return add2LL(ll1, ll2, c)


def add2LL(ll1, ll2, c):
    result = Node(-1)
    resultHead = result
    while ll1 or ll2:
        v1 = ll1.value if ll1 else 0
        v2 = ll2.value if ll2 else 0

        v = v1 + v2 + c
        
        c = int(v / 10)
        result.next = Node(v % 10)
        
        result = result.next
        ll1 = ll1.next if ll1 else None
        ll2 = ll2.next if ll2 else None
        
    if c != 0:
        result = Node(c)
        c = 0
    
    return resultHead.next
    

root1 = Node(7,Node(1,Node(6)))
root2 = Node(5,Node(9,Node(2,Node(2))))

r = sumLists(root1, root2)
        
while r:
    print(r.value, end='')
    r = r.next
