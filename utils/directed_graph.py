
# Structure inspirée de EdgeList du dépôt GitHub :
# https://github.com/lecfab/volt
# de Fabrice Lecruyer mentionné dans l'article :
# Tailored vertex ordering for faster triangle listing in large graphs

class DirectedGraph:
    def __init__(self) -> None:
        self.successors = dict()
        self.predecessors = dict()
        
        self.nodes = set()
        self.num_edges = 0

        self.in_degrees = dict()
        self.out_degrees = dict()

        self.computed_degrees = False
        
    def __str__(self) -> str:
        return str(self.successors)

    def add_edge(self, u, v) -> None:
        if u not in self.successors:
            self.successors[u] = set()
        if v not in self.predecessors:
            self.predecessors[v] = set()
        self.predecessors[v].add(u)
        self.successors[u].add(v)
        self.nodes.add(u)
        self.nodes.add(v)
        self.num_edges += 1

    def successors_of_node(self, node) -> list:
        return self.successors.get(node, [])
    
    def predecessors_of_node(self, node) -> list:
        return self.predecessors.get(node, [])

    def compute_degrees(self) -> None:
        if self.computed_degrees:
            return
        for u in self.successors:
            self.out_degrees[u] = len(self.successors[u])
            for v in self.successors[u]:
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
    
    def get_num_nodes(self) -> int:
        return len(self.nodes)
    
    def get_num_edges(self) -> int:
        return self.num_edges