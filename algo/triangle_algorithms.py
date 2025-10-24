import utils.directed_graph as DG

def A_plus_plus(g:DG.DirectedGraph, ranklist=[]) -> set:
    result = set()
    b = {u: False for u in g.nodes}
    nodes = ranklist if ranklist else g.nodes
    for w in nodes:
        for v in g.predecessors_of_node(w):
            b[v] = True
        for u in g.predecessors_of_node(w):
            for v in g.successors_of_node(u):
                if b[v]:
                    #print(f"Triangle found: ({u}, {v}, {w})")
                    result.add((u, v, w))
        for v in g.predecessors_of_node(w):
            b[v] = False
    return result

def A_plus_minus(g:DG.DirectedGraph, ranklist=[]) -> int:
    result = 0
    b = {u: False for u in g.nodes}
    nodes = ranklist if ranklist else g.nodes
    for u in nodes:
        for w in g.successors_of_node(u):
            b[w] = True
        for v in g.successors_of_node(u):
            for w in g.successors_of_node(v):
                if b[w]:
                    #print(f"Triangle found: ({u}, {v}, {w})")
                    result += 1
        for w in g.successors_of_node(u):
            b[w] = False
    return result
