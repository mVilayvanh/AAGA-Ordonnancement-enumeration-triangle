import utils.directed_graph as DG

def rank_nodes_by_local_clustering_order(g : DG.DirectedGraph) -> list:
    """
    Evalue le rang de tous les noeuds par rapport au coefficient local de clustering
    """
    g.compute_clustering_coefficients()
    nodes = list(g.nodes)
    return sorted(nodes, key=lambda u: g.clustering_coefficients[u], reverse=True) 