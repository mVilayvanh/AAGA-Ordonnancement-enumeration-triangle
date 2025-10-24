import order.order_deg as ODEG
import utils.file_parser as FP
import algo.triangle_algorithms as TA
import os

if __name__ == "__main__":
    # key: filepath, value: directed graph
    graph_dict = dict()
    ranks = list()
    
    for filepath in os.listdir("ressources/"):
        if filepath.endswith(".txt"):
            full_path = os.path.join("ressources/", filepath)
            graph_dict[full_path] = FP.parse_file_to_directed_graph(full_path)
    
    for graphName in graph_dict:
        g = graph_dict[graphName]
        ranked_nodes = ODEG.rank_nodes_by_degree(g, descending=True)
        ranks.append((graphName, ranked_nodes))
    
    print("Triangle enumeration for each graph:")
    for graphName, ranked_nodes in ranks:
        print(f"Graph: {graphName}")
        print("Using A++ algorithm with degree-based ranking")
        print("Number of triangle:", TA.A_plus_plus(graph_dict[graphName], ranklist=ranked_nodes))

        print("Using A+- algorithm with degree-based ranking")
        print("Number of triangle:", TA.A_plus_minus(graph_dict[graphName], ranklist=ranked_nodes))

        