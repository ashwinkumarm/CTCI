'''
Created on 09-Jun-2018

@author: Ashwin
'''

from CTCI.concepts.Node import Node


def remove_dup_temp_buffer(nodes):
    temp = set()
    prev = None
    while nodes:
        if nodes.value not in temp:
            temp.add(nodes.value)
            prev = nodes
        else:
            prev.next = nodes.next
        nodes = nodes.next


def remove_dups_no_buffer(nodes):
    while nodes:
        outer_value = nodes.value
        inner = nodes.next
        prev = None
        while inner:
            if inner.value == outer_value:
                prev.next = inner.next
            prev = inner
            inner = inner.next
        nodes = nodes.next
                

root = Node(5)
root.next = node3 = Node(3)
node3.next = node7 = Node(7)
node7.next = node1 = Node(1)
node1.next = node3t = Node(3)
node3t.next = node6 = Node(6)

remove_dups_no_buffer(root)
#removeDupsTempBuffer(root)

while root:
    print(root.value, end="")
    root = root.next
