import utils.directedGraph as DG

def compare_degree_asc(d1:int, d2:int):
    return d1 - d2

def compare_degree_desc(d1:int, d2:int):
    return d2 - d1

def rank_nodes_by_degree(graph:DG.DirectedGraph, descending:bool=True):
    graph.compute_degrees()
    nodes = list(graph.nodes)
    if descending:
        nodes.sort(key=lambda n: graph.get_degree(n), reverse=True)
    else:
        nodes.sort(key=lambda n: graph.get_degree(n))
    return nodes

