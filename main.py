import order.order_deg as ODEG
import order.order_degene as ODEGNE
import order.order_similarity as ODSIM
import order.order_clustering as ODCLU
import order.order_succ_degree as ODSUCD
import utils.file_parser as FP
import utils.plotbuilder as PB
import utils.clock as CL
import algo.triangle_algorithms as TA
import os

if __name__ == "__main__":
    graph_dict = dict()
    orders = ["Degenerancy", "Degree", "Similarity", "Clustering", "Succ_Degree"]
    rank_functions = [ODEGNE.compute_degeneracy_order, 
                 ODEG.rank_nodes_by_degree_desc,
                 ODSIM.compute_similarity_order,
                 ODCLU.rank_nodes_by_local_clustering_order,
                 ODSUCD.rank_nodes_by_sum_successors_degree]
    pb_full = PB.PlotBuilder()
    pb_mere = PB.PlotBuilder()
    clock = CL.Clock()
    n = 1
    # Charger les graphes
    for filepath in os.listdir("ressources/"):
        if filepath.endswith(".txt"):
            full_path = os.path.join("ressources/", filepath)
            graph_dict[full_path] = FP.parse_file_to_directed_graph(full_path)
    print(f"Ordonnacements à tester: {orders}")
    for graph_name, g in graph_dict.items():
        print(f"Dataset: {graph_name}")
        print(f"Statistics:\n" + g.stats())
        for i in range(len(orders)):
            times = list()
            print(f"  Order: {orders[i]}")
            for j in range(n):
                clock.start()
                rank_list = rank_functions[i](g)
                clock.stop()
                rank_time = clock.elapsed()
                clock.reset()

                clock.start()
                TA.A_plus_minus(g, ranklist=rank_list)
                a_plus_minus_time = clock.elapsed()
                clock.reset()
                times.append((rank_time, a_plus_minus_time))
            average_rank_time = sum(t[0] for t in times) / n
            average_enum_time = sum(t[1] for t in times) / n
            pb_full.add_time(graph_name, f"{orders[i]}", average_rank_time + average_enum_time)
            pb_mere.add_time(graph_name, f"{orders[i]}", average_enum_time)

    pb_full.build_durations(title="Durées d'exécution (full-listing) par dataset et ordonnancement")
    pb_full.build_speedups(baseline_order="Degenerancy", title="Speedups (full-listing) par dataset et ordonnancement")
    pb_mere.build_durations(title="Durées d'exécution (mere-listing) par dataset et ordonnancement")
    pb_mere.build_speedups(baseline_order="Degenerancy", title="Speedups (mere-listing) par dataset et ordonnancement")
    pb_full.show()
