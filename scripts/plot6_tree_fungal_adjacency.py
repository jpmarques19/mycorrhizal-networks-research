import networkx as nx
import matplotlib.pyplot as plt

import data_handling as dh
import network_analysis as na
import visualization as vis
#%%
df_plot6 = dh.read_and_preprocess_data('../data/01_SampleData.csv', 6)

#%%
unique_tree_connections = na.get_unique_tree_connections(df_plot6)

#%% Create adjancecy matrix
unique_tree_genotypes = df_plot6['TreeID'].unique()
adj_matrix = na.create_adjacency_matrix(unique_tree_connections, unique_tree_genotypes).values
#%% plot adj matrix
vis.plot_adjacency_matrix(adj_matrix, 'Plot 6')

#%% Create graph from adj matrix

# Create an empty graph
G = dh.build_graph_from_adjacency_matrix(adj_matrix)


#%% generate circular layout  from  graph
# Create a figure and axes object
fig, ax = plt.subplots(dpi=300)

# Generate the circular layout of the graph
pos = nx.circular_layout(G)

# Set node properties
node_color = 'lightgreen'
node_edge_color = 'black'
node_size = 100
node_alpha = 0.8

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color=node_color, edgecolors=node_edge_color, node_size=node_size, alpha=node_alpha, ax=ax)

# Set edge properties
edge_color = 'black'
edge_width = 0.5

# Draw edges
nx.draw_networkx_edges(G, pos, edge_color=edge_color, width=edge_width, ax=ax)

# Set label properties
font_size = 6
font_color = 'black'
font_weight = 'bold'

# Remove the axes
ax.axis('off')

# Add a title
ax.set_title("Plot 6", fontsize=8)

# Show the plot
plt.show()


#move to new branch
#%% Calculate Centralities

# Calculate centrality measures
proximity_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
degree_centrality = nx.degree_centrality(G)

# Combine centrality measures into a single dictionary
combined_centrality = {}
for node in G.nodes():
    combined_centrality[node] = (proximity_centrality[node] + betweenness_centrality[node] + degree_centrality[node]) / 3

# Sort nodes by their combined centrality value in descending order
sorted_nodes = sorted(combined_centrality.items(), key=lambda x: x[1], reverse=True)

# Select the top N most central nodes
N = 8  # You can change this value based on your desired number of nodes to remove
top_nodes = [node for node, _ in sorted_nodes[:N]]

G_without_top_nodes = G.copy()
G_without_top_nodes.remove_nodes_from(top_nodes)


#%% count nodes compare

original_num_nodes = G.number_of_nodes()

# Assuming `subgraphs` contains the list of subgraphs after removing the top 8 nodes
total_subgraph_nodes = sum([subgraph.number_of_nodes() for subgraph in subgraphs])

print(f"Original number of nodes: {original_num_nodes}")
print(f"Total number of nodes in subgraphs: {total_subgraph_nodes}")



#%% plot subgraphs

def plot_subgraphs(G):
    connected_components = list(nx.connected_components(G))
    n_subgraphs = len(connected_components)
    fig, axes = plt.subplots(n_subgraphs, 1, figsize=(10, 5 * n_subgraphs))

    for i, component in enumerate(connected_components):
        subgraph = G.subgraph(component)

        if n_subgraphs == 1:
            ax = axes
        else:
            ax = axes[i]

        pos = nx.spring_layout(subgraph, seed=42)
        nx.draw(subgraph, pos, node_color='mediumseagreen', node_size=500, edge_color='black', with_labels=True, ax=ax)
        ax.set_title(f'Subgraph {i + 1}', fontsize=14)

    plt.tight_layout()
    plt.show()

# Call the function to plot the subgraphs
plot_subgraphs(G_without_top_nodes)


print(adj_matrix)
