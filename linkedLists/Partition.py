'''
Created on 09-Jun-2018

@author: Ashwin
'''

from Node import Node

def partition(node, x):
    ll1 = Node(-1)
    ll2 = Node(-1)
    
    ll1Head = ll1
    ll2Head = ll2
    while node:
        if node.value < x:
            ll1.next = Node(node.value)
            ll1 = ll1.next
        else:
            ll2.next = Node(node.value)
            ll2 = ll2.next
        node = node.next
    
    ll1.next = ll2Head.next
    
    return ll1Head.next

root = Node(5)
root.next = node3 = Node(3)
node3.next = node7 = Node(7)
node7.next = node1 = Node(1)
node1.next =  node6 = Node(6)

partitoned = partition(root, 5)

while partitoned:
    print partitoned.value,
    partitoned = partitoned.next