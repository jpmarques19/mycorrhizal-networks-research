import matplotlib.pyplot as plt
import networkx as nx
import itertools
from data_handling import create_graph_from_plot_data
from network_analysis import k_clique_communities
from visualization import color_cliques, visualize_communities_with_k_cliques

# Create the graph from the plot data
filename = "../data/01_SampleData.csv"
plot_number = 6
G = create_graph_from_plot_data(filename, plot_number)
print(nx.number_of_nodes(G))
print(nx.number_of_edges(G))
print(nx.density(G))


#%%
# Get the k-clique communities
k = 6
community_k_cliques = k_clique_communities(G, k)

# Generate the node and edge colors based on the communities
node_colors, edge_colors = color_cliques(G, community_k_cliques)

# Plot the communities with their k-cliques
fig, axes = plt.subplots(nrows=1, ncols=len(community_k_cliques), figsize=(20, 8))
visualize_communities_with_k_cliques(G, community_k_cliques, edge_colors, node_colors, axes)
plt.show()
