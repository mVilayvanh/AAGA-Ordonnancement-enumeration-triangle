def compute_louvain_order(g, max_iter=10):
    """
    Simplified Louvain community detection to derive a node ordering.
    Works without any external libraries.

    Args:
        g: DirectedGraph
        max_iter: number of iterations for local optimization

    Returns:
        ordered_nodes: list of nodes ordered by community density (descending)
    """

    # --- Initialization ---
    community = {u: u for u in g.nodes}  # each node = its own community
    changed = True
    iteration = 0

    def neighbors(u):
        # Combine successors and predecessors for community detection
        return set(g.successors_of_node(u)) | set(g.predecessors_of_node(u))

    # --- Phase 1: local optimization ---
    while changed and iteration < max_iter:
        changed = False
        iteration += 1

        for u in g.nodes:
            # Current community of u
            current_c = community[u]

            # Compute connections per community
            neighbor_comms = {}
            for v in neighbors(u):
                c = community[v]
                neighbor_comms[c] = neighbor_comms.get(c, 0) + 1

            if not neighbor_comms:
                continue

            # Find community with maximum link count
            best_c = max(neighbor_comms, key=neighbor_comms.get)

            # Move u if the new community is better
            if neighbor_comms[best_c] > neighbor_comms.get(current_c, 0):
                community[u] = best_c
                changed = True

    # --- Phase 2: compute community densities ---
    comm_nodes = {}
    for node, comm_id in community.items():
        comm_nodes.setdefault(comm_id, []).append(node)

    density = {}
    for comm_id, nodes in comm_nodes.items():
        internal_edges = sum(
            1 for u in nodes for v in g.successors_of_node(u) if v in nodes
        )
        possible = len(nodes) * (len(nodes) - 1)
        density[comm_id] = internal_edges / possible if possible > 0 else 0

    # --- Build final ordering ---
    ordered_comms = sorted(comm_nodes.keys(), key=lambda c: density[c], reverse=True)

    ordered_nodes = []
    for comm_id in ordered_comms:
        nodes_sorted = sorted(comm_nodes[comm_id], key=lambda n: g.get_out_degree(n), reverse=True)
        ordered_nodes.extend(nodes_sorted)

    return ordered_nodes

