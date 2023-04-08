import networkx as nx
import matplotlib.pyplot as plt

import data_handling as dh
import network_analysis as na
import visualization as vis
#%%
# Generate the two graphs
G1 = dh.create_graph_from_plot_data('../data/01_SampleData.csv', 1)
G6 = dh.create_graph_from_plot_data('../data/01_SampleData.csv', 6)

#%%
RG1 = dh.generate_random_network_from_graph(G1)
RG6 = dh.generate_random_network_from_graph(G6)

#%%

# Generate the circular layouts
pos1 = nx.circular_layout(RG1)
pos2 = nx.circular_layout(RG6)

# Set node properties
node_color = 'lightgreen'
node_edge_color = 'black'
node_size = 100
node_alpha = 0.8

# Set edge properties
edge_color = 'black'
edge_width = 0.5

# Set label properties
font_size = 6
font_color = 'black'
font_weight = 'bold'

# Create the figure and axes
fig, axes = plt.subplots(ncols=2, figsize=(10, 5))

# Plot the first ER random network
nx.draw_networkx_nodes(RG1, pos1, node_color=node_color, edgecolors=node_edge_color, node_size=node_size, alpha=node_alpha, ax=axes[0])
nx.draw_networkx_edges(RG1, pos1, edge_color=edge_color, width=edge_width, ax=axes[0])
axes[0].axis('off')
axes[0].set_title("ER Random Network 1", fontsize=8)

# Plot the second ER random network
nx.draw_networkx_nodes(RG6, pos2, node_color=node_color, edgecolors=node_edge_color, node_size=node_size, alpha=node_alpha, ax=axes[1])
nx.draw_networkx_edges(RG6, pos2, edge_color=edge_color, width=edge_width, ax=axes[1])
axes[1].axis('off')
axes[1].set_title("ER Random Network 2", fontsize=8)

# Show the plot
plt.show()