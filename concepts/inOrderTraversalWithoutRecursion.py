from CTCI.concepts.TreeNode import TreeNode


def pushAllLeft(n, s):
    while n:
        s.append(n)
        n = n.left


def inOrderNoRecursion(root):
    s = []
    pushAllLeft(root, s)
    while s:
        n = s.pop()
        print(n.key)
        if n.right:
            s.append(n.right)
            pushAllLeft(n.right.left, s)

root = TreeNode(6)
root.left = Node7 = TreeNode(3)
root.right = Node8 = TreeNode(8)
Node7.left = Node6 = TreeNode(2)
Node7.right = Node9 = TreeNode(5)
Node8.left = Node12 = TreeNode(7)
Node8.right = Node14 = TreeNode(14)
Node9.left = Node15 = TreeNode(4)

inOrderNoRecursion(root)