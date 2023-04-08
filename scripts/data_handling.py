import pandas as pd
import numpy as np
import networkx as nx
from itertools import combinations
from scipy.cluster.hierarchy import linkage, dendrogram

def create_graph_from_plot_data(filename, plot_number):
    sample_data = read_and_preprocess_data(filename, plot_number)
    adjacency_matrix = create_adjacency_matrix(sample_data)
    G = build_graph_from_adjacency_matrix(adjacency_matrix)
    return G

def read_and_preprocess_data(file_path, plot_number):
    df = pd.read_csv(file_path)
    df_plot = df[df['Plot'] == f'Plot {plot_number}'].drop(['Plot', 'Site', 'UTM_X', 'UTM_Y'], axis=1)
    df_plot = df_plot.drop_duplicates(subset=["SmpleID"])
    return df_plot

def get_unique_tree_connections(df):
    filtered_df = df[['GenetID', 'TreeID']]
    grouped = filtered_df.groupby('GenetID')

    fungus_connections = []
    for genet_id, group in grouped:
        connected_tree_genotypes = group['TreeID'].unique()
        connected_pairs = list(combinations(connected_tree_genotypes, 2))

        for pair in connected_pairs:
            fungus_connections.append((genet_id, pair[0], pair[1]))

    fungus_connections_df = pd.DataFrame(fungus_connections, columns=['GenetID', 'TreeID_1', 'TreeID_2'])
    fungus_connections_df['sorted_trees'] = fungus_connections_df[['TreeID_1', 'TreeID_2']].apply(sorted, axis=1).apply(tuple)
    unique_connections_df = fungus_connections_df.drop(['TreeID_1', 'TreeID_2'], axis=1).drop_duplicates()

    unique_pairs = set()
    for _, row in unique_connections_df.iterrows():
        tree_id_1 = row['sorted_trees'][0]
        tree_id_2 = row['sorted_trees'][1]
        pair = (tree_id_1, tree_id_2)
        unique_pairs.add(pair)

    unique_pairs_list = list(unique_pairs)

    return unique_pairs_list

def create_adjacency_matrix(plot_data):
    unique_tree_connections = get_unique_tree_connections(plot_data)
    unique_tree_genotypes = plot_data['TreeID'].unique()
    # Create a mapping of tree genotypes to indices for the adjacency matrix
    tree_genotype_to_index = {genotype: index for index, genotype in enumerate(unique_tree_genotypes)}

    # Create an empty adjacency matrix
    adjacency_matrix = np.zeros((len(unique_tree_genotypes), len(unique_tree_genotypes)))

    # Iterate through each row in the fungus connections dataframe
    for tree_genotype_1, tree_genotype_2 in unique_tree_connections:

        # Get the indices of the connected tree genotypes in the adjacency matrix
        index_1 = tree_genotype_to_index[tree_genotype_1]
        index_2 = tree_genotype_to_index[tree_genotype_2]

        # Increment the value at the corresponding row and column in the adjacency matrix
        adjacency_matrix[index_1, index_2] += 1
        adjacency_matrix[index_2, index_1] += 1

    # Convert the adjacency matrix to a pandas DataFrame for better readability
    adjacency_df = pd.DataFrame(adjacency_matrix, index=unique_tree_genotypes, columns=unique_tree_genotypes)
    
    return adjacency_df.values

def build_graph_from_adjacency_matrix(matrix):
    G = nx.Graph(matrix)
    return G

def hierachical_clustering(adjacency_matrix, method="single"):
    linkage_matrix = linkage(adjacency_matrix, method=method)
    order = np.argsort(dendrogram(linkage_matrix)['leaves'])
    return adjacency_matrix[:, order][order, :]

