import utils.directed_graph as DG
from functools import cmp_to_key
from collections import defaultdict, deque
import heapq

def compute_degeneracy_order(g):
    """
    Compute degeneracy ordering for a directed graph (based on in-degree).
    Equivalent to the C++ algo_kcore version, adapted to DirectedGraph.
    """

    g.compute_degrees()

    # Compute in-degrees (since graph is directed)
    in_degrees = {u: g.get_in_degree(u) for u in g.nodes}

    # Initialize min-heap (degree, node)
    heap = [(deg, u) for u, deg in in_degrees.items()]
    heapq.heapify(heap)

    visited = set()
    order_list = []
    degeneracy = 0

    # Main loop
    while heap:
        deg, u = heapq.heappop(heap)

        # Skip if node already processed
        if u in visited:
            continue

        visited.add(u)
        order_list.append(u)
        degeneracy = max(degeneracy, deg)

        # Decrease degree of neighbors still in heap
        for v in g.successors_of_node(u):
            if v not in visited:
                in_degrees[v] -= 1
                heapq.heappush(heap, (in_degrees[v], v))

    return order_list