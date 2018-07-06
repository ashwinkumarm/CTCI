from CTCI.concepts.Node import Node


def intersection(l1, l2):
    tail1, size1 = get_tail_and_size(l1)
    tail2, size2 = get_tail_and_size(l2)
    
    if tail1 != tail2:
        return None
    
    longer = l1 if size1 > size2 else l2
    shorter = l1 if size1 < size2 else l2
    
    longer = move_k_dist(longer, abs(size1 - size2))
    
    while longer != shorter:
        longer = longer.next
        shorter = shorter.next
    
    return shorter


def get_tail_and_size(l):
    s = 0
    while l and l.next:
        s +=1
        l = l.next
    s += 1
    
    return l,s


def move_k_dist(l, k):
    while k > 0:
        l = l.next
        k -= 1
        
    return l


node = Node(1, Node(6))
root1 = Node(7,node)
root2 = Node(5,Node(9,node))

print(intersection(root1, root2).value)