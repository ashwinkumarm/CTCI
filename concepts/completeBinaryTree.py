def solution(root):

    result = traverse_complete(root)
    print(result)

def traverse_complete(root):

    if root:
        left = traverse_complete(root.l)
        right = traverse_complete(root.r)
        max_complete = max(left[0], right[0])
        max_height = max(left[1], right[1])
        left_child_only = 1 if (left[2] == 1 and right[0] == 0) or (left[0] == 1 and right[0] == 0) else 0

        # 5 conditions need to pass before left and right can be joined by this node
        # to create a complete subtree.
        if left[0] < right[0]:
            return [max_complete, 0, 2]
        if left[2] == 2 or right[2] == 2:
            return [max_complete, 0, 2]
        if abs(left[1]-right[1]) > 1:
            return [max_complete, 0, 2]
        if (left[2] == 1 and right[2] == 1) or (left[2] == 0 and right[2] == 1):
            return [max_complete, 0, 2]
        if left[0] == right[0] and left[0] != 2**left[0] - 1:
            return [max_complete, 0, 2]
        return [left[0] + right[0] + 1, max_height + 1, left_child_only]
    else:
        return [0,0,0]

class Tree:
    def __init__(self, x, l = None, r= None):
        self.x = x
        self.l = l
        self.r = r

node65 = Tree(65, None, None)
node6 = Tree(6, None, None)
node2 = Tree(2, node65, node6)
node10 = Tree(10, None, None)
node13 = Tree(13, None, None)
node9 = Tree(9, node10, node13)
node1 = Tree(1, node2, node9)

solution(node1)