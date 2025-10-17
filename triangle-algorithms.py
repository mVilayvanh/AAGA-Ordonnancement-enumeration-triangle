import utils.directedGraph as dg

def triangle_listing(g:dg.DirectedGraph):
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

