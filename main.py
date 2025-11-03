import order.order_deg as ODEG
import order.order_degene as ODEGNE
import order.order_similarity as ODSIM
import order.order_louvain as ODLOUV
import order.order_clustering as ODCLU
import utils.file_parser as FP
import utils.clock as CL
import algo.triangle_algorithms as TA
import os

if __name__ == "__main__":
    graph_dict = dict()

    # Création du dossier de résultats
    os.makedirs("results", exist_ok=True)
    result_path_mere = "results/results_mereListing.txt"
    result_path_full = "results/results_fullListing.txt"

    # Charger les graphes
    for filepath in os.listdir("ressources/"):
        if filepath.endswith(".txt"):
            full_path = os.path.join("ressources/", filepath)
            graph_dict[full_path] = FP.parse_file_to_directed_graph(full_path)

    print("Triangle enumeration for each graph:")
    for graph_name, g in graph_dict.items():
        print(f"\nGraph: {graph_name}")

        # --- degre order ---
        # --- mere listing ---
        ranked_degree = ODEG.rank_nodes_by_degree(g, descending=True)

        # A++
        clock = CL.Clock()
        clock.start()
        ntri_degree_a1_m = len(TA.A_plus_plus(g, ranklist=ranked_degree))
        clock.stop()
        t_degree_a1_m = clock.elapsed()

        clock.reset()

        # A+-
        clock.start()
        ntri_degree_a2_m = TA.A_plus_minus(g, ranklist=ranked_degree)
        clock.stop()
        t_degree_a2_m = clock.elapsed()

        clock.reset()

        # --- full listing ---

        # A++
        clock = CL.Clock()
        clock.start()
        ranked_degree_a1 = ODEG.rank_nodes_by_degree(g, descending=True)
        ntri_degree_a1_f = len(TA.A_plus_plus(g, ranklist=ranked_degree_a1))
        clock.stop()
        t_degree_a1_f = clock.elapsed()

        clock.reset()

        # A+-
        clock.start()
        ranked_degree_a2 = ODEG.rank_nodes_by_degree(g, descending=True)
        ntri_degree_a2_f = TA.A_plus_minus(g, ranklist=ranked_degree_a2)
        clock.stop()
        t_degree_a2_f = clock.elapsed()

        clock.reset()

        print(f"Degree Order - A++: {t_degree_a1_m}s (mere), {t_degree_a1_f}s (full)")
        print(f"Degree Order - A+-: {t_degree_a2_m}s (mere), {t_degree_a2_f}s (full)")
        print(f"Number of triangles found: {ntri_degree_a1_m}")
        print(f"Number of tringles found: {ntri_degree_a2_m}")

        # --- degeneracy order ---
        # --- mere listing ---
        ranked_degen = ODEGNE.compute_degeneracy_order(g)
        ranked_degen.reverse()

        # A++
        clock.start()
        ntri_degen_a1_m = len(TA.A_plus_plus(g, ranklist=ranked_degen))
        clock.stop()
        t_degen_a1_m = clock.elapsed()

        clock.reset()

        # A+-
        clock.start()
        ntri_degen_a2_m = TA.A_plus_minus(g, ranklist=ranked_degen)
        clock.stop()
        t_degen_a2_m = clock.elapsed()

        clock.reset()

        # --- full listing ---
        # A++
        clock.start()
        ranked_degen_a1 = ODEGNE.compute_degeneracy_order(g)
        ranked_degen_a1.reverse()
        ntri_degen_a1_f = len(TA.A_plus_plus(g, ranklist=ranked_degen_a1))
        clock.stop()
        t_degen_a1_f = clock.elapsed()

        clock.reset()

        # A+-
        clock.start()
        ranked_degen_a2 = ODEGNE.compute_degeneracy_order(g)
        ranked_degen_a2.reverse()
        ntri_degen_a2_f = TA.A_plus_minus(g, ranklist=ranked_degen_a2)
        clock.stop()
        t_degen_a2_f = clock.elapsed()

        clock.reset()

        print(f"Degen Order - A++: {t_degen_a1_m}s (mere), {t_degen_a1_f}s (full)")
        print(f"Degen Order - A+-: {t_degen_a2_m}s (mere), {t_degen_a2_f}s (full)")
        print(f"Number of triangles found: {ntri_degen_a1_m}")
        print(f"Number of tringles found: {ntri_degen_a2_m}")

        # --- Similarity order ---
        # --- mere listing ---
        ranked_sim = ODSIM.compute_similarity_order(g)

        # A++
        clock.start()
        ntri_sim_a1_m = len(TA.A_plus_plus(g, ranklist=ranked_sim))
        clock.stop()
        t_sim_a1_m = clock.elapsed()

        clock.reset()

        # A+-
        clock.start()
        ntri_homo_a2_m = TA.A_plus_minus(g, ranklist=ranked_sim)
        clock.stop()
        t_homo_a2_m = clock.elapsed()

        clock.reset()

        # --- full listing ---

        # A++
        clock.start()
        ranked_sim_a1 = ODSIM.compute_similarity_order(g)
        ntri_sim_a1_f = len(TA.A_plus_plus(g, ranklist=ranked_sim_a1))
        clock.stop()
        t_sim_a1_f = clock.elapsed()

        clock.reset()

        # A+-
        clock.start()
        ranked_sim_a2 = ODSIM.compute_similarity_order(g)
        ntri_sim_a2_f = TA.A_plus_minus(g, ranklist=ranked_sim_a2)
        clock.stop()
        t_sim_a2_f = clock.elapsed()

        clock.reset()

        print(f"Homophily Order - A++: {t_sim_a1_m}s (mere), {t_sim_a1_f}s (full)")
        print(f"Homophily Order - A+-: {t_homo_a2_m}s (mere), {t_sim_a2_f}s (full)")
        print(f"Number of triangles found: {ntri_sim_a1_m}")
        print(f"Number of tringles found: {ntri_homo_a2_m}")

        # --- louvain order ---
        # --- mere listing ---
        ranked_louv = ODLOUV.compute_louvain_order(g)

        # A++
        clock.start()
        ntri_louv_a1_m = len(TA.A_plus_plus(g, ranklist=ranked_louv))
        clock.stop()
        t_louv_a1_m = clock.elapsed()

        clock.reset()

        # A+-
        clock.start()
        ntri_louv_a2_m = TA.A_plus_minus(g, ranklist=ranked_louv)
        clock.stop()
        t_louv_a2_m = clock.elapsed()

        clock.reset()

        # --- full listing ---

        # A++
        clock.start()
        ranked_louv_a1 = ODLOUV.compute_louvain_order(g)
        ntri_louv_a1_f = len(TA.A_plus_plus(g, ranklist=ranked_louv_a1))
        clock.stop()
        t_louv_a1_f = clock.elapsed()

        clock.reset()

        # A+-
        clock.start()
        ranked_louv_a2 = ODLOUV.compute_louvain_order(g)
        ntri_louv_a2_f = TA.A_plus_minus(g, ranklist=ranked_louv_a2)
        clock.stop()
        t_louv_a2_f = clock.elapsed()

        clock.reset()

        print(f"Louvain Order - A++: {t_louv_a1_m}s (mere), {t_louv_a1_f}s (full)")
        print(f"Louvain Order - A+-: {t_louv_a2_m}s (mere), {t_louv_a2_f}s (full)")
        print(f"Number of triangles found: {ntri_louv_a1_m}")
        print(f"Number of tringles found: {ntri_louv_a2_m}")

        # --- clustering order ---
        # --- mere listing ---
        ranked_clus = ODCLU.compute_clustering_order(g)

        # A++
        clock.start()
        ntri_clus_a1_m = len(TA.A_plus_plus(g, ranklist=ranked_clus))
        clock.stop()
        t_clus_a1_m = clock.elapsed()

        clock.reset()

        # A+-
        clock.start()
        ntri_clus_a2_m = TA.A_plus_minus(g, ranklist=ranked_clus)
        clock.stop()
        t_clus_a2_m = clock.elapsed()

        clock.reset()

        # --- full listing ---

        # A++
        clock.start()
        ranked_clus_a1 = ODCLU.compute_clustering_order(g)
        ntri_clus_a1_f = len(TA.A_plus_plus(g, ranklist=ranked_clus_a1))
        clock.stop()
        t_clus_a1_f = clock.elapsed()

        clock.reset()

        # A+-
        clock.start()
        ranked_clus_a2 = ODCLU.compute_clustering_order(g)
        ntri_clus_a2_f = TA.A_plus_minus(g, ranklist=ranked_clus_a2)
        clock.stop()
        t_clus_a2_f = clock.elapsed()

        clock.reset()

        print(f"Clustering Order - A++: {t_clus_a1_m}s (mere), {t_clus_a1_f}s (full)")
        print(f"Clustering Order - A+-: {t_clus_a2_m}s (mere), {t_clus_a2_f}s (full)")
        print(f"Number of triangles found: {ntri_clus_a1_m}")
        print(f"Number of tringles found: {ntri_clus_a2_m}")


        with open(result_path_mere, "a") as f:
            f.write(f"{graph_name} : {t_degree_a1_m}; {t_degree_a2_m}; {t_degen_a1_m}; {t_degen_a2_m}; {t_sim_a1_m}; {t_homo_a2_m}; {t_louv_a1_m}; {t_louv_a2_m}; {t_clus_a1_m}; {t_clus_a2_m}\n")
        with open(result_path_full, "a") as f:
            f.write(f"{graph_name} : {t_degree_a1_f}; {t_degree_a2_f}; {t_degen_a1_f}; {t_degen_a2_f}; {t_sim_a1_f}; {t_sim_a2_f}; {t_louv_a1_f}; {t_louv_a2_f}; {t_clus_a1_f}; {t_clus_a2_f}\n")
        assert ntri_degree_a1_m == ntri_degree_a2_m == ntri_degree_a1_f == ntri_degree_a2_f == \
                ntri_degen_a1_m == ntri_degen_a2_m == ntri_degen_a1_f == ntri_degen_a2_f == \
                ntri_sim_a1_m == ntri_homo_a2_m == ntri_sim_a1_f == ntri_sim_a2_f == \
                ntri_louv_a1_m == ntri_louv_a2_m == ntri_louv_a1_f == ntri_louv_a2_f  == \
                ntri_clus_a1_m == ntri_clus_a2_m == ntri_clus_a1_f == ntri_clus_a2_f, \
                "Triangle counts are not all equal!"


        