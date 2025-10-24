# Parse un fichier vers la classe DirectedGraph

import utils.directed_graph as DG

# Format:
# [id_u] [id_v]
# Chaque ligne représente une arête dirigée de u vers v
def parse_file_to_directed_graph(file_path: str) -> DG.DirectedGraph:
    '''
    Parse un fichier et retourne un DirectedGraph.
    '''
    graph = DG.DirectedGraph()
    with open(file_path, 'r') as f:
        for line in f:
            u, v = map(int, line.strip().split())
            graph.add_edge(u, v)
    return graph

