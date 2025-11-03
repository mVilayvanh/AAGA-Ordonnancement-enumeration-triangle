import utils.directed_graph as DG
from functools import cmp_to_key

def compare_degree_asc(d1:int, d2:int) -> int:
    return d1 - d2

def compare_degree_desc(d1:int, d2:int) -> int:
    return d2 - d1

def rank_nodes_by_degree(graph:DG.DirectedGraph, descending:bool=True) -> list:
    graph.compute_degrees()
    nodes = list(graph.nodes)
    if descending:
        nodes.sort(key=cmp_to_key(lambda u, v: compare_degree_desc(graph.get_degree(u), graph.get_degree(v))))
    else:
        nodes.sort(key=cmp_to_key(lambda u, v: compare_degree_asc(graph.get_degree(u), graph.get_degree(v))))
    return nodes

def rank_nodes_by_degree_desc(graph:DG.DirectedGraph) -> list:
    return rank_nodes_by_degree(graph, descending=True)

def rank_nodes_by_degree_asc(graph:DG.DirectedGraph) -> list:
    return rank_nodes_by_degree(graph, descending=False)
