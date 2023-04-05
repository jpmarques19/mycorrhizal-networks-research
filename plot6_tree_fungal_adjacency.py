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
# Create a new empty graph object
G = nx.Graph()

# Get the unique tree genotypes
unique_tree_genotypes = df['TreeID'].unique()

# Add the nodes to the graph
for tree_genotype in unique_tree_genotypes:
    G.add_node(tree_genotype)

# Preview the nodes in the graph
print(G.nodes())

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
