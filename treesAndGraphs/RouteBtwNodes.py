from CTCI.concepts.DirectedGraph import DirectedGraph
from collections import deque

def routeBtwNodes(g, s, e):
    visited , q = set(),deque(s)
    while q:
        node = q.popleft()
        if node == e:
            return True
        if node not in visited:
            visited.add(node)
            for n in g.getOutgoingEdges(node):
                q.append(n)
    return False

s = "a"
e = "d"
graph = {"a": ["b", "c","d"],
         "b": [],
         "c": ["d"],
         "d": ["c"]
        }
g = DirectedGraph(graph)
print(routeBtwNodes(g, s, e))





