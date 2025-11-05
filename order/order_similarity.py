import utils.directed_graph as DG
from functools import cmp_to_key
from collections import defaultdict, deque
from functools import lru_cache


def compute_similarity_order(g):
    """
        Compute node order based on local homophily.

        Args:
            g: DirectedGraph

        Returns:
            ordered_nodes: list of nodes ordered by their homophily score
    """

    
    def similarity(v, w):
        """
            Similarity of Jaccard

            Args :
                v : first node
                w : second node

            Returns : degree of similari
        """
        succ_v = set(g.successors_of_node(v))
        succ_w = set(g.successors_of_node(w))
        if not succ_v or not succ_w:
            return 0
        return len(succ_v & succ_w) / len(succ_v | succ_w)
    
    local_homophily = dict()

     # --- Compute similarity score for each node ---
    similarity_score = {}
    for u in g.nodes:
        neighbors = list(g.successors_of_node(u))
        if len(neighbors) < 2:
            similarity_score[u] = 0
            continue
        sim_sum = 0
        pairs = 0
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                sim_sum += similarity(neighbors[i], neighbors[j])
                pairs += 1
        similarity_score[u] = sim_sum / pairs if pairs > 0 else 0

    # --- Order nodes by similarity score ---
    ordered_nodes = sorted(similarity_score.keys(),
                           key=lambda u: similarity_score[u],
                           reverse=True)
    return ordered_nodes

def compute_degree_order(g):
    """
        Compute node order based on the sum of successor degrees.

        Args:
            g: DirectedGraph

        Returns:
            ordered_nodes: list of nodes ordered by their degrees score
    """

     # --- Compute similarity score for each node ---
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

    # --- Order nodes by similarity score ---
    ordered_nodes = sorted(degree_score.keys(),
                           key=lambda u: degree_score[u],
                           reverse=True)
    return ordered_nodes