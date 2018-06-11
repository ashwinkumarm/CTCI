class DirectedGraph:
    def __init__(self, dict = None):
        if dict is None:
            self.graphDict = {}
        else:
            self.graphDict = dict

    def addVertices(self, v):
        if v not in self.graphDict.keys():
            self.graphDict[v] = {}

    def getVerticesList(self):
        return list(self.graphDict.keys())

    def addEdge(self, e1,e2):
        if e1 in self.graphDict.keys():
            self.graphDict[e1].append(e2)
        else:
            self.graphDict[e1] = [e2]

    def getOutgoingEdges(self, v):
        if v in self.graphDict.keys():
            return self.graphDict[v]
        return None

    def getAllOutgoingEdges(self):
        edges = []
        for v in self.graphDict.keys():
            for n in self.graphDict[v]:
                if (v, n) not in edges:
                    edges.append((v,n))
        return edges


# g = { "a" : ["d"],
#           "b" : ["c"],
#           "c" : ["b", "c", "d", "e"],
#           "d" : ["a", "c"],
#           "e" : ["c"],
#           "f" : []
# }

g = {"a": ["b", "c"],
         "b": ["d"],
         "c": ["d"],
         "d": ["b"],
        }

# graph = DirectedGraph(g)
# print(graph.getOutgoingEdges('a'))
# print(graph.getAllOutgoingEdges())
