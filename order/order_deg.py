import utils.directed_graph as DG
from functools import cmp_to_key

def compare_degree_asc(d1:int, d2:int):
    return d1 - d2

def compare_degree_desc(d1:int, d2:int):
    return d2 - d1

def rank_nodes_by_degree(graph:DG.DirectedGraph, descending:bool=True):
    graph.compute_degrees()
    nodes = list(graph.nodes)
    if descending:
        nodes.sort(key=cmp_to_key(compare_degree_desc))
    else:
        nodes.sort(key=cmp_to_key(compare_degree_asc))
    return nodes

