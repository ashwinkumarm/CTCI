from CTCI.concepts.Node import Node


def sum_lists(ll1, ll2):
    return add_2linked_list(ll1, ll2, 0)


def add_2linked_list(ll1, ll2, c):
    result = Node(-1)
    result_head = result
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
        result.next = Node(c)
    
    return result_head.next
    

# root1 = Node(7,Node(1,Node(6)))
# root2 = Node(5,Node(9,Node(2,Node(2))))

root1 = Node(9,Node(9))
root2 = Node(1)

r = sum_lists(root1, root2)
while r:
    print(r.value, end='')
    r = r.next
