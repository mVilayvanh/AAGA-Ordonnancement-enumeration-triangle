
# Structure inspirée de EdgeList du dépôt GitHub :
# https://github.com/lecfab/volt
# de Fabrice Lecruyer mentionné dans l'article :
# Tailored vertex ordering for faster triangle listing in large graphs

class DirectedGraph:
    def __init__(self) -> None:
        self.edges = dict()
        self.nodes = set()
        self.in_degrees = dict()
        self.out_degrees = dict()
        self.computed_degrees = False
        
    def __str__(self) -> str:
        return str(self.edges)

    def add_edge(self, u, v) -> None:
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append(v)
        self.nodes.add(u)
        self.nodes.add(v)


    def get_neighbors(self, node) -> list:
        return self.edges.get(node, [])

    def is_successor(self, u, v) -> bool:
        return v in self.edges.get(u, [])
    
    def is_predecessor(self, u, v) -> bool:
        return u in self.edges.get(v, [])

    def successors(self, node) -> list:
        return self.edges.get(node, [])
    
    def predecessors(self, node) -> list:
        preds = []
        for u in self.edges:
            if node in self.edges[u]:
                preds.append(u)
        return preds

    def compute_degrees(self) -> None:
        if self.computed_degrees:
            return
        for u in self.edges:
            self.out_degrees[u] = len(self.edges[u])
            for v in self.edges[u]:
                if v in self.in_degrees:
                    self.in_degrees[v] += 1
                else:
                    self.in_degrees[v] = 1
        self.computed_degrees = True
    
    def get_in_degree(self, node) -> int:
        if not self.computed_degrees:
            self.compute_degrees()
        return self.in_degrees.get(node, 0)
    
    def get_out_degree(self, node) -> int:
        if not self.computed_degrees:
            self.compute_degrees()
        return self.out_degrees.get(node, 0)
    
    def get_degree(self, node) -> int:
        if not self.computed_degrees:
            self.compute_degrees()
        return self.get_in_degree(node) + self.get_out_degree(node)
