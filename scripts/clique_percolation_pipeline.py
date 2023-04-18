
import networkx as nx
from networkx.algorithms.community import k_clique_communities

import data_handling as dh
import network_analysis as na
import visualization as vis

#%%
def find_communities_with_clique_percolation(G, k):
    communities = list(k_clique_communities(G, k))
    num_communities = len(communities)
    print(f"Number of communities for k={k}: {num_communities}")
    
    for i, community in enumerate(communities):
        print(f"Community {i + 1}: {community}")
        subgraph = G.subgraph(community)
        size = len(subgraph.nodes())
        density = nx.density(subgraph)
        print(f"Community {i+1}: size={size}, density={density}")
        
    return communities

#%%
G = dh.create_graph_from_plot_data('../data/01_SampleData.csv', 5)

#%%

k_values = [i for i in range(2,28)]  # You can test different k values based on your network properties

for k in k_values:
    print(f"Results for k={k}:")
    print("\n")
    communities = find_communities_with_clique_percolation(G, k)
    community_sizes = [len(community) for community in communities]
    total_nodes = sum(community_sizes)
    print(na.entropy_shared_nodes(community_sizes, total_nodes, communities))
    print("\n")


#%%
import math
import numpy as np

def find_optimal_k(network, k_range):
    max_entropy = -np.inf
    optimal_k = None

    for k in k_range:
        communities = find_communities_with_clique_percolation(network, k)
        community_sizes = [len(community) for community in communities]
        total_nodes = sum(community_sizes)
        entropy = na.entropy(community_sizes, total_nodes)
        entropy = na.entropy_shared_nodes(community_sizes, total_nodes, communities)

        if entropy > max_entropy:
            max_entropy = entropy
            optimal_k = k

    return optimal_k

best_k = find_optimal_k(G, range(2,28))
print("\n")
print(f"Optimal k value: {best_k}")
print("\n")
communities = find_communities_with_clique_percolation(G, best_k)
print("\n")

#%%
import math
import numpy as np
import csv

def find_shared_nodes(communities):
    shared_nodes = 0
    for i in range(len(communities)):
        for j in range(i + 1, len(communities)):
            shared_nodes += len(set(communities[i]).intersection(set(communities[j])))
    return shared_nodes

def find_optimal_k(network, k_range):
    max_entropy = -np.inf
    optimal_k = None

    for k in k_range:
        communities = find_communities_with_clique_percolation(network, k)
        community_sizes = [len(community) for community in communities]
        total_nodes = sum(community_sizes)
        entropy = na.entropy(community_sizes, total_nodes)
        entropy = na.entropy_shared_nodes(community_sizes, total_nodes, communities)

        if entropy > max_entropy:
            max_entropy = entropy
            optimal_k = k

    return optimal_k

best_k = find_optimal_k(G, range(2,14))
print("\n")
print(f"Optimal k value: {best_k}")
print("\n")
communities = find_communities_with_clique_percolation(G, best_k)
print("\n")

# Export to CSV
with open('community_stats_a.csv', mode='w', newline='') as csv_file:
    fieldnames = ['k', 'N', 'Size of communities', 'Density of communities', 'Shared nodes', 'Entropy']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for k in range(2, 14):
        communities = find_communities_with_clique_percolation(G, k)
        community_sizes = [len(community) for community in communities]
        density_values = [nx.density(G.subgraph(community)) for community in communities]
        shared_nodes = find_shared_nodes(communities)
        entropy = na.entropy_shared_nodes(community_sizes, sum(community_sizes), communities)
        writer.writerow({'k': k, 'N': len(communities), 'Size of communities': community_sizes, 'Density of communities': density_values, 'Shared nodes': shared_nodes, 'Entropy': entropy})
