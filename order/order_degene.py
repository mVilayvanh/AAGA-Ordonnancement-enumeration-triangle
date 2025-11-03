import utils.directed_graph as DG
from functools import cmp_to_key
from collections import defaultdict, deque

def compute_degeneracy_order(g):
    # Calculate each node's degree
    g.compute_degrees()

    # Initialize degrees dictionary {node : degree}
    degrees = {u: g.get_degree(u) for u in g.nodes}

    order_list = []

    buckets = [[] for _ in range(max(degrees.values()) + 1)] 
    for u , d in degrees.items():
        buckets[d].append(u)

    k = 0

    for n in range (len(g.nodes)):
        i = 0
        while i < len(buckets) and len(buckets[i]) == 0:
            i += 1
        
        k = max (k, i)

        v = buckets[i].pop()
        order_list.append(v)

        for w in g.successors_of_node(v) | g.predecessors_of_node(v):
            if(w not in order_list):
                d_w = degrees[w]
                buckets[d_w].remove(w)
                degrees[w] -= 1
                buckets[d_w - 1].append(w)

    return order_list