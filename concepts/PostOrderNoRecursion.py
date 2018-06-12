from CTCI.concepts.TreeNode import TreeNode

def postOrder2Stacks(root):
    s1 = []
    s2 = []
    s1.append(root)
    while s1:
        n = s1.pop()
        s2.append(n)
        if n.left:
            s1.append(n.left)
        if n.right:
            s1.append(n.right)
    return reversed(s2)

def postOrder1Stacks(root):
    s1 = []
    while True:
        while root:
            if root.right is not None:
                s1.append(root.right)
            s1.append(root)
            root = root.left

        n = s1.pop()

        if n.right is not None and s1 and s1[-1] == n.right:
            s1.pop()
            s1.append(n)
            root = n.right
        else:
            print(n.key, end = " ")
            root = None

        if not s1:
            break

def postOrderWithSet(root):
    visited = set()
    temp = root
    while temp and not (temp in visited):
        if temp.left and temp.left not in visited:
            temp = temp.left
        elif temp.right and temp.right not in visited:
            temp = temp.right
        else:
            visited.add(temp)
            print(temp.key, end=' ')
            temp = root


root = TreeNode(5)
root.left = Node7 = TreeNode(3)
root.right = Node8 = TreeNode(7)
Node7.left = Node6 = TreeNode(1)
Node7.right = Node9 = TreeNode(4)
Node8.left = Node12 = TreeNode(6)
Node8.right = Node14 = TreeNode(8)

# postOrder = postOrder2Stacks(root)
#
# for p in postOrder:
#     print(p.key, end=" ")

#postOrder1Stacks(root)

postOrderWithSet(root)


