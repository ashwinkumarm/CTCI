from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.oe = set()
        self.ie = set()

    def add_outgoing_edges(self, e):
        self.oe.add(e)

    def add_incoming_edges(self, e):
        self.ie.add(e)

    def no_of_incoming_edges(self):
        return len(self.ie)

    def get_outgoing_edges(self):
        return self.oe

    def remove_incoming_edge(self, e):
        self.ie.remove(e)


def build_order(projects, dependencies):
    dict = {}
    for p in projects:
        dict[p] = Node(p)

    for d in dependencies:
        p = dict[d[0]]
        c = dict[d[1]]
        p.add_outgoing_edges(c)
        c.add_incoming_edges(p)

    b_order = []
    q = deque()

    for p in projects:
        if dict[p].no_of_incoming_edges() == 0:
            q.append(dict[p])

    while q:
        n = q.popleft()
        b_order.append(n.val)
        for oe in n.get_outgoing_edges():
            dict[oe.val].remove_incoming_edge(n)
            if dict[oe.val].no_of_incoming_edges() == 0:
                q.append(dict[oe.val])

        if len(b_order) > len(projects):
            raise Exception

    return b_order


projects = ["A", "B", "C", "D", "E", "F"]
dependencies = [("A", "D"), ("F", "B"), ("B", "D"), ("F", "A"), ("D", "C")]

print(build_order(projects, dependencies))