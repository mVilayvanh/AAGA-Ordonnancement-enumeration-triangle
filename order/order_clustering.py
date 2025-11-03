def compute_clustering_order(g):
    """
    Compute node order based on the local out-clustering coefficient.

    The local out-clustering coefficient of a node u measures how many
    of its out-neighbors are also connected to each other (in any direction).

    Args:
        g: DirectedGraph

    Returns:
        ordered_nodes: list of nodes ordered by descending clustering coefficient
    """

    clustering = {}

    # Precompute adjacency sets for faster lookups
    adjacency = {u: set(g.successors_of_node(u)) for u in g.nodes}

    for u in g.nodes:
        neighbors = adjacency[u]
        deg = len(neighbors)

        # If less than 2 neighbors, clustering coefficient is 0
        if deg < 2:
            clustering[u] = 0.0
            continue

        # Count links among neighbors efficiently
        links = 0
        for v in neighbors:
            # Intersection between v's successors and u's neighbors
            links += len(adjacency.get(v, set()) & neighbors)

        # Each edge between neighbors is counted once per direction
        clustering[u] = links / (deg * (deg - 1))

    # Sort nodes by clustering coefficient descending
    ordered_nodes = sorted(g.nodes, key=lambda u: clustering[u], reverse=True)

    return ordered_nodes