import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
#%%
df = pd.read_csv("01_SampleData.csv")

df_plot6 = df[df['Plot'] == 'Plot 6'].drop(['Plot', 'Site', 'UTM_X', 'UTM_Y'], axis=1)

df_plot6.head()

df_plot6 = df_plot6.drop_duplicates(subset=["SmpleID"])


#%%
# Filter the dataframe to keep only relevant columns
filtered_df = df_plot6[['GenetID', 'TreeID']]

# Group the filtered dataframe by 'GenetID'
grouped = filtered_df.groupby('GenetID')

# Initialize an empty list to store fungus connections
fungus_connections = []

# Iterate through the groups
for genet_id, group in grouped:
    # Get the tree genotypes connected by the same fungus genotype (GenetID)
    connected_tree_genotypes = group['TreeID'].unique()

    # Find all pairs of connected tree genotypes using itertools.combinations
    connected_pairs = list(combinations(connected_tree_genotypes, 2))

    # Add the connected pairs to the fungus_connections list along with the GenetID
    for pair in connected_pairs:
        fungus_connections.append((genet_id, pair[0], pair[1]))

# Create the fungus_connections_df using the fungus_connections list
fungus_connections_df = pd.DataFrame(fungus_connections, columns=['GenetID', 'TreeID_1', 'TreeID_2'])

# First, create a new column with sorted tree IDs
fungus_connections_df['sorted_trees'] = fungus_connections_df[['TreeID_1', 'TreeID_2']].apply(sorted, axis=1).apply(tuple)

# Then, drop the original columns and drop duplicates
unique_connections_df = fungus_connections_df.drop(['TreeID_1', 'TreeID_2'], axis=1).drop_duplicates()

# Initialize an empty set to store unique pairs
unique_pairs = set()

# Iterate over the rows of fungus_connections_df
for _, row in unique_connections_df.iterrows():
    # Get the tree genotypes connected by the current fungus genotype
    tree_id_1 = row['sorted_trees'][0]
    tree_id_2 = row['sorted_trees'][1]    
    # Create a pair of connected tree genotypes
    pair = (tree_id_1, tree_id_2)
    
    # Add the pair to the unique_pairs set
    unique_pairs.add(pair)

# Convert the set of unique_pairs back to a list
unique_pairs_list = list(unique_pairs)

#%%
# Get the unique tree genotypes
unique_tree_genotypes = df_plot6['TreeID'].unique()

# Create a mapping of tree genotypes to indices for the adjacency matrix
tree_genotype_to_index = {genotype: index for index, genotype in enumerate(unique_tree_genotypes)}

# Create an empty adjacency matrix
adjacency_matrix = np.zeros((len(unique_tree_genotypes), len(unique_tree_genotypes)))

# Iterate through each row in the fungus connections dataframe
for tree_genotype_1, tree_genotype_2 in unique_pairs_list:

    # Get the indices of the connected tree genotypes in the adjacency matrix
    index_1 = tree_genotype_to_index[tree_genotype_1]
    index_2 = tree_genotype_to_index[tree_genotype_2]

    # Increment the value at the corresponding row and column in the adjacency matrix
    adjacency_matrix[index_1, index_2] += 1
    adjacency_matrix[index_2, index_1] += 1

# Convert the adjacency matrix to a pandas DataFrame for better readability
adjacency_df = pd.DataFrame(adjacency_matrix, index=unique_tree_genotypes, columns=unique_tree_genotypes)

#%%

adj_matrix = adjacency_df.values

# Create a figure and axes object
fig, ax = plt.subplots(dpi=300)

# Plot the adjacency matrix
im = ax.imshow(adj_matrix, cmap='binary')

# Set the tick labels
ax.set_xticks(np.arange(len(adj_matrix)))
ax.set_yticks(np.arange(len(adj_matrix)))
ax.set_xticklabels(np.arange(1, len(adj_matrix)+1))
ax.set_yticklabels(np.arange(1, len(adj_matrix)+1))

# Rotate the tick labels and set their alignment
plt.setp(ax.get_xticklabels(), rotation=0, ha="center", va="center")
plt.setp(ax.get_yticklabels(), rotation=0, ha="right", va="center")

# Set the fontsize of the tick labels
ax.tick_params(axis='both', which='major', labelsize=4)

# Add a title
ax.set_title("Adjacency Matrix - Plot 6", fontsize=8)

# Show the plot
plt.show()

#%%

# Create an empty graph
G = nx.Graph()

# Add the edges to the graph
for i in range(adj_matrix.shape[0]):
    for j in range(adj_matrix.shape[1]):
        if adj_matrix[i, j] == 1:
            G.add_edge(i, j)

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


