def successor(n):
    if n is None:
        return None

    if n.right:
        return leftMost(n.right)
    else:
        x = n
        p = x.parent
        while p and p.left is not x:
            x = p
            p = p.parent

        return p

def leftMost(n):
    if n is None:
        return None

    while n.left:
        n = n.left
    return n