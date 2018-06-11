
from CTCI.concepts.TreeNode import TreeNode

def isBalanced(root):
    if not root:
        return True, 0

    isB, dL = isBalanced(root.left)
    if not isB:
        return False, None

    isB, dR = isBalanced(root.right)
    if not isB:
        return False, None

    if abs(dL - dR) > 1:
        return False, None
    else:
        return True, max(dL, dR) + 1


root = TreeNode(5)
root.left = Node7 = TreeNode(7)
root.right = Node8 = TreeNode(8)
Node7.left = Node6 = TreeNode(6)
Node7.right = Node9 = TreeNode(9)
Node8.left = Node12 = TreeNode(12)
Node8.right = Node14 = TreeNode(14)
Node9.left = Node15 = TreeNode(15)
Node15.left = Node16 = TreeNode(16)

print(isBalanced(root))