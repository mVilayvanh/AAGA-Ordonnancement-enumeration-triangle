import utils.directed_graph as DG

def A_plus_plus(g:DG.DirectedGraph, ranklist=[]) -> int:
    result = 0
    b = {u: False for u in g.nodes}
    nodes = ranklist if ranklist else g.nodes
    for w in nodes:
        for v in g.predecessors(w):
            b[v] = True
        for u in g.predecessors(w):
            for v in g.successors(u):
                if b[v]:
                    #print(f"Triangle found: ({u}, {v}, {w})")
                    result += 1
        for v in g.predecessors(w):
            b[v] = False
    return result

def A_plus_minus(g:DG.DirectedGraph, ranklist=[]) -> int:
    result = 0
    b = {u: False for u in g.nodes}
    nodes = ranklist if ranklist else g.nodes
    for u in nodes:
        for w in g.successors(u):
            b[w] = True
        for v in g.successors(u):
            for w in g.successors(v):
                if b[w]:
                    #print(f"Triangle found: ({u}, {v}, {w})")
                    result += 1
        for w in g.successors(u):
            b[w] = False
    return result
