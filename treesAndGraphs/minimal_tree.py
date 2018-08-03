from CTCI.concepts.TreeNode import TreeNode

def createBst(sortedArray):
    return _createBst(sortedArray, 0, len(sortedArray)-1)

def _createBst(sortedArray, s, e):
    if s > e:
        return None

    m = int((s + e) / 2)

    root = TreeNode(sortedArray[m])
    root.left = _createBst(sortedArray, s, m-1)
    root.right = _createBst(sortedArray, m+1, e)

    return root



sList = [2,3,5,7,9]
bst = createBst(sList)
