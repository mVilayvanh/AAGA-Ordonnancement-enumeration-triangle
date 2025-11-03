import utils.directed_graph as DG
from functools import cmp_to_key
from collections import defaultdict, deque
from functools import lru_cache


def compute_homophily_order(g, tau=0.5, alpha=0.5):
    """
        Compute node order based on local homophily.

        Args:
            g: DirectedGraph
            tau: similarity threshold (between 0 and 1)
            alpha: homophily threshold to activate filtering

        Returns:
            ordered_nodes: list of nodes ordered by their homophily score
    """

    def similarity_fn(v, w):
        succ_v = set(g.successors_of_node(v))
        succ_w = set(g.successors_of_node(w))
        if not succ_v or not succ_w:
            return 0
        return len(succ_v & succ_w) / len(succ_v | succ_w)
    
    local_homophily = dict()

    # compute local homophily for each node
    for u in g.nodes:
        neighbors_out = list(g.successors_of_node(u))
        if len(neighbors_out) < 2:
            local_homophily[u] = 0
            continue

        sim_sum = 0
        pairs = 0
        for i in range(len(neighbors_out)):
            for j in range(i + 1, len(neighbors_out)):
                v, w = neighbors_out[i], neighbors_out[j]
                sim = similarity_fn(v, w)
                if sim >= tau:  # only consider pairs above threshold
                    sim_sum += sim
                    pairs += 1

        local_homophily[u] = (sim_sum / pairs) if pairs > 0 else 0

    # score-based ordering
    above = [u for u in g.nodes if local_homophily[u] >= alpha]
    below = [u for u in g.nodes if local_homophily[u] < alpha]

    above.sort(key=lambda u: local_homophily[u], reverse=True)
    below.sort(key=lambda u: local_homophily[u], reverse=True)

    ordered_nodes = above + below 
    return ordered_nodes
