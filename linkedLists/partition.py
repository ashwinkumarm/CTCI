from CTCI.concepts.Node import Node


def partition(node, x):
    ll1 = Node(-1)
    ll2 = Node(-1)
    
    ll1_head = ll1
    ll2_head = ll2
    while node:
        if node.value < x:
            ll1.next = Node(node.value)
            ll1 = ll1.next
        else:
            ll2.next = Node(node.value)
            ll2 = ll2.next
        node = node.next
    
    ll1.next = ll2_head.next
    
    return ll1_head.next


root = Node(5)
root.next = node3 = Node(3)
node3.next = node7 = Node(7)
node7.next = node1 = Node(1)
node1.next = node6 = Node(6)
p = partition(root, 3)

while p:
    print(p.value, end='')
    p = p.next
