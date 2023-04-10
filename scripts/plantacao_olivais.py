import numpy as np

import data_handling as dh
import visualization as vis


matrix = np.genfromtxt('../data/olivais.csv', delimiter=',')


matrix_reordered = dh.hierachical_clustering(matrix, "single")

# Create a graph from the adjacency matrix
G = dh.build_graph_from_adjacency_matrix(matrix_reordered)

vis.plot_adjacency_matrix(matrix, "Plantação Olivais")