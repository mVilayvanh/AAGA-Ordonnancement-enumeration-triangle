import utils.directed_graph as DG

def rank_nodes_by_sum_successors_degree(g : DG.DirectedGraph) -> list:
    """
        Evalue un rang pour le noeud u par rapport à la somme des degrés de ses successeurs.

        Args:
            g: DirectedGraph

        Returns:
            ordered_nodes: list of nodes ordered by their degrees score
    """

    degree_score = {}
    for u in g.nodes:
        neighbors = list(g.successors_of_node(u))
        if len(neighbors) < 2:
            degree_score[u] = 0
            continue
        deg_sum = 0
        pairs = 0
        for i in range(len(neighbors)):
            deg_sum += g.get_degree(neighbors[i])
            pairs += 1
        degree_score[u] = deg_sum / pairs if pairs > 0 else 0

    ordered_nodes = sorted(degree_score.keys(),
                           key=lambda u: degree_score[u],
                           reverse=True)
    return ordered_nodes
