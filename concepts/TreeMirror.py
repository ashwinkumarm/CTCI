from CTCI.concepts.TreeNode import TreeNode

def treeMirror(root):
    return _treeMirror(root.left, root.right)

def _treeMirror(lTree, rTree):
    if lTree is None or rTree is None:
        return lTree is None and rTree is None

    return lTree.key == rTree.key and _treeMirror(lTree.left, rTree.right) and _treeMirror(lTree.right, rTree.left)

root = TreeNode(1)
root.left = Node7 = TreeNode(2)
root.right = Node8 = TreeNode(2)
Node7.left = Node6 = TreeNode(3)
Node7.right = Node9 = TreeNode(4)
Node8.left = Node12 = TreeNode(4)
Node8.right = Node14 = TreeNode(3)

print(treeMirror(root))