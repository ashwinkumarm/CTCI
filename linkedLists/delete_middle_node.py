def del_middle_node(node):
    if node is None or node.next is None:
        return False
    
    node.value = node.next.value
    node.next = node.next.next
    return True
