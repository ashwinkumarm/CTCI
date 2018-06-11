from CTCI.concepts.TreeNode import TreeNode

def preOrderNoRecursion(root):
    s = []
    s.append(root)

    while s:
        n = s.pop()
        print(n.key, end = ' ')

        if n.right:
            s.append(n.right)
        if n.left:
            s.append(n.left)


root = TreeNode(5)
root.left = Node7 = TreeNode(3)
root.right = Node8 = TreeNode(7)
Node7.left = Node6 = TreeNode(1)
Node7.right = Node9 = TreeNode(4)
Node8.left = Node12 = TreeNode(6)
Node8.right = Node14 = TreeNode(8)

preOrderNoRecursion(root)

