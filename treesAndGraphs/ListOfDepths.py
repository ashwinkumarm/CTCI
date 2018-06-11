from CTCI.concepts.TreeNode import TreeNode

def listOfDepths(root):
    result = []
    current = []
    if root != None:
        current.append(root)

    while len(current) > 0:
        result.append(current)
        parents = current
        current = []
        for p in parents:
            if p.left:
                current.append(p.left)
            if p.right:
                current.append(p.right)

    return result



root = TreeNode(5)
root.left = Node7 = TreeNode(7)
root.right = Node8 = TreeNode(8)
Node7.left = Node6 = TreeNode(6)
Node7.right = Node9 = TreeNode(9)
Node8.left = Node12 = TreeNode(12)
Node8.right = Node14 = TreeNode(14)
Node9.left = Node15 = TreeNode(15)

lDepths = listOfDepths(root)
for l in lDepths:
    for ll in l:
        print(ll.key, end = " ")
    print()