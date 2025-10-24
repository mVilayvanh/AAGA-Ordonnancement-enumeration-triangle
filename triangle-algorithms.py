import utils.directed_graph as dg

def A_plus_plus(g:dg.DirectedGraph):
    b = {u: False for u in g.nodes}
    # ici il faudra modifier g.nodes pour changer l'ordre de parcours
    for w in g.nodes:
        for v in g.predecessors(w):
            b[v] = True
        for u in g.predecessors(w):
            for v in g.successors(u):
                if b[v]:
                    print(f"Triangle found: ({u}, {v}, {w})")
        for v in g.predecessors(w):
            b[v] = False

def A_plus_minus(g:dg.DirectedGraph):
    b = {u: False for u in g.nodes}
    for u in g.nodes:
        for w in g.successors(u):
            b[w] = True
        for v in g.successors(u):
            for w in g.successors(v):
                if b[w]:
                    print(f"Triangle found: ({u}, {v}, {w})")
        for w in g.successors(u):
            b[w] = False

