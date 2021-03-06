from CTCI.concepts.TreeNode import TreeNode


def validate_bst(root):
    return _validate_bst(root, None, None)


def _validate_bst(root, min, max):
    if root is None:
        return True

    if (min and root.key < min) or (max and root.key > max):
        return False

    if not _validate_bst(root.left, min, root.key) or not _validate_bst(root.right, root.key, max):
        return False

    return True


root = TreeNode(6)
root.left = Node7 = TreeNode(3)
root.right = Node8 = TreeNode(8)
Node7.left = Node6 = TreeNode(2)
Node7.right = Node9 = TreeNode(5)
Node8.left = Node12 = TreeNode(7)
Node8.right = Node14 = TreeNode(14)
Node9.left = Node15 = TreeNode(4)


print(validate_bst(root))