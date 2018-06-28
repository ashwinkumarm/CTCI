from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.oe = set()
        self.ie = set()

    def addOutgoingEdges(self, e):
        self.oe.add(e)

    def addIncomingEdges(self, e):
        self.ie.add(e)

    def no_of_incomingedges(self):
        return len(self.ie)

    def get_outgoing_edges(self):
        return self.oe

    def remove_incomingEdge(self, e):
        self.ie.remove(e)


def build_order(projects, dependencies):
    dict = {}
    for p in projects:
        dict[p] = Node(p)

    for d in dependencies:
        p = dict[d[0]]
        c = dict[d[1]]
        p.addOutgoingEdges(c)
        c.addIncomingEdges(p)

    buildorder = []
    q = deque()

    for p in projects:
        if dict[p].no_of_incomingedges() == 0:
            q.append(dict[p])

    while q:
        n = q.popleft()
        buildorder.append(n.val)
        for oe in n.get_outgoing_edges():
            dict[oe.val].remove_incomingEdge(n)
            if dict[oe.val].no_of_incomingedges() == 0:
                q.append(dict[oe.val])

        if len(buildorder) > len(projects):
            raise Exception


    return buildorder

projects = ["A", "B", "C", "D", "E", "F"]
dependencies = [("A", "D"), ("F", "B"), ("B", "D"), ("F", "A"), ("D", "C")]

print(build_order(projects, dependencies))