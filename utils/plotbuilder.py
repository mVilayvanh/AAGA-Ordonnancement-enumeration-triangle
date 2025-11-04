import matplotlib.pyplot as plt
import numpy as np

class PlotBuilder:
    def __init__(self):
        self.data = {}

    def add_dataset(self, dataset: str) -> None:
        """Ajoute un dataset à la structure de données."""
        if dataset not in self.data:
            self.data[dataset] = {}

    def add_order(self, dataset: str, order: str) -> None:
        """Ajoute un ordonnancement pour un dataset donné."""
        if dataset not in self.data:
            self.add_dataset(dataset)
        if order not in self.data[dataset]:
            self.data[dataset][order] = None

    def add_time(self, dataset: str, order: str, time: float) -> None:
        """Ajoute un temps d'exécution pour un dataset et un ordonnancement donnés."""
        if dataset not in self.data:
            self.add_dataset(dataset)
        if order not in self.data[dataset]:
            self.add_order(dataset, order)
        self.data[dataset][order] = time

    def build_durations(self, title="Temps d'exécution par dataset et ordonnancement", ylabel="Temps (s)"):
        """Affiche un graphique en barres des temps d'exécution."""
        if not self.data:
            return
        datasets = list(self.data.keys())
        ordonnancements = sorted({o for d in self.data.values() for o in d.keys()})
        values = np.array([
            [self.data[d].get(o, 0) or 0 for o in ordonnancements] for d in datasets
        ])
        x = np.arange(len(datasets))
        width = 0.8 / len(ordonnancements)
        plt.figure(figsize=(10, 6))
        for i, o in enumerate(ordonnancements):
            plt.bar(
                x + i * width,
                values[:, i],
                width,
                label=o)
        plt.xticks(x + width * (len(ordonnancements) - 1) / 2, datasets)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.legend(title="Ordonnancement")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()

    def build_speedups(self, baseline_order: str, title="Speedup par dataset et ordonnancement", ylabel="Speedup"):
        """Fabrique les graphique en barres des speedups par rapport à un ordonnancement de référence."""
        if not self.data:
            return
        datasets = list(self.data.keys())
        ordonnancements = sorted({o for d in self.data.values() for o in d.keys() if o != baseline_order})
        values = np.array([
            [
                (self.data[d][baseline_order] / self.data[d][o]) if self.data[d].get(baseline_order) and self.data[d].get(o) else 0
                for o in ordonnancements
            ]
            for d in datasets
        ])
        x = np.arange(len(datasets))
        width = 0.8 / len(ordonnancements)
        plt.figure(figsize=(10, 6))
        for i, o in enumerate(ordonnancements):
            plt.bar(
                x + i * width,
                values[:, i],
                width,
                label=o)
        plt.axhline(y=1, color='r', linestyle='--', linewidth=1, label=baseline_order)
        plt.xticks(x + width * (len(ordonnancements) - 1) / 2, datasets)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.legend(title="Ordonnancement")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()

    def show(self):
        plt.show()

    def __repr__(self):
        return f"PlotBuilder(data={self.data})"

if __name__ == "__main__":
    pb = PlotBuilder()
    pb.add_time("Dataset1", "OrderA", 2.5)
    pb.add_time("Dataset1", "OrderB", 3.0)
    pb.add_time("Dataset2", "OrderA", 1.5)
    pb.add_time("Dataset2", "OrderB", 2.0)
    pb.add_time("Dataset3", "OrderA", 4.0)
    pb.add_time("Dataset3", "OrderB", 3.5)
    pb.show()