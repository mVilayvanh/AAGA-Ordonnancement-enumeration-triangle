class DirectedGraph:
    def __init__(self):
        self.edges = dict()
        self.nodes = set()
        self.in_degrees = {node: 0 for node in self.nodes}
        self.out_degrees = {node: 0 for node in self.nodes}
        self.computed_degrees = False
        
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

    def compute_degrees(self):
        if self.computed_degrees:
            return
        for u in self.edges:
            self.out_degrees[u] = len(self.edges[u])
            for v in self.edges[u]:
                self.in_degrees[v] += 1
        self.computed_degrees = True
    
    def get_in_degree(self, node):
        if not self.computed_degrees:
            self.compute_degrees()
        return self.in_degrees.get(node, 0)
    
    def get_out_degree(self, node):
        if not self.computed_degrees:
            self.compute_degrees()
        return self.out_degrees.get(node, 0)
    
    def get_degree(self, node):
        if not self.computed_degrees:
            self.compute_degrees()
        return self.get_in_degree(node) + self.get_out_degree(node)
