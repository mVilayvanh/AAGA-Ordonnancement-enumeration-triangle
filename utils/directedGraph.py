class DirectedGraph:
    def __init__(self):
        self.edges = dict()
        self.nodes = set()
        
    def __str__(self):
        return str(self.adj)

    def add_edge(self, u, v):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append(v)
        self.nodes.add(u)
        self.nodes.add(v)


    def get_neighbors(self, node):
        return self.edges.get(node, [])

    def is_successor(self, u, v):
        return v in self.adj.get(u, [])
    
    def is_predecessor(self, u, v):
        return u in self.adj.get(v, [])

    def successors(self, node):
        return self.edges.get(node, [])
    
    def predecessors(self, node):
        preds = []
        for u in self.edges:
            if node in self.edges[u]:
                preds.append(u)
        return preds
