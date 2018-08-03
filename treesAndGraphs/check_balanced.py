from CTCI.concepts.TreeNode import TreeNode


def is_balanced(root):
    if not root:
        return True, 0

    is_b, d_l = is_balanced(root.left)
    if not is_b:
        return False, None

    is_b, d_r = is_balanced(root.right)
    if not is_b:
        return False, None

    if abs(d_l - d_r) > 1:
        return False, None
    else:
        return True, max(d_l, d_r) + 1


root = TreeNode(5)
root.left = Node7 = TreeNode(7)
root.right = Node8 = TreeNode(8)
Node7.left = Node6 = TreeNode(6)
Node7.right = Node9 = TreeNode(9)
Node8.left = Node12 = TreeNode(12)
Node8.right = Node14 = TreeNode(14)
Node9.left = Node15 = TreeNode(15)
Node15.left = Node16 = TreeNode(16)

print(is_balanced(root))