import matplotlib.pyplot as plt
import numpy as np

class PlotBuilder:
    def __init__(self, size=(10, 6), ndataset=1):
        self.fig, self.ax = plt.subplots(2, 2, figsize=size)
        self.x = np.arange(ndataset)
        self.width = 1 / ndataset
        self.ndataset = ndataset

    def set_title(self, title, subplot=(0, 0)):
        i, j = subplot
        self.ax[i][j].set_title(title)

    def plot_clustered_bar(self, data, xlabel, subplot=(0, 0)):
        i, j = subplot
        ax = self.ax[i][j]
        ax.bar([self.x - self.width], data[0], width=self.width)
        ax.set_xticks(self.x)
        ax.set_xticklabels(xlabel)

    def show(self):
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    # pb = PlotBuilder(nmethods=5)
    # pb.set_title("Test Plot", subplot=(0, 0))
    # pb.plot_clustered_bar([[1, 2, 3, 6, 7], [2, 3, 4, 1, 0], [3, 4, 5, 2, 2]], xlabel=["A"], subplot=(0, 0))
    # pb.show()
    # [[Donnée1] [Donnée2] ...]
    # [[valeur 1= methode1, valeur 2= méthode2, ...], [valeur 1= méthode1, valeur 2= méthode2, ...], ...]
    data = [[4, 5, 6, 5], [5, 1, 3, 6]]
    for i in range(len(data)):
        plt.bar(np.arange(len(data[i])) + i * 0.2, data[i], width=0.2)
    plt.xticks(np.arange(len(data[0])) + 0.2, ['A', 'B', 'C', 'D'])
    plt.show()