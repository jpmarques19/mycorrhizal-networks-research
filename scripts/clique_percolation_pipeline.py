
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
G = dh.create_graph_from_plot_data('../data/01_SampleData.csv', 6)

#%%

k_values = [i for i in range(2,41)]  # You can test different k values based on your network properties

for k in k_values:
    print(f"Results for k={k}:")
    communities = find_communities_with_clique_percolation(G, k)
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

best_k = find_optimal_k(G, range(2,41))
print("\n")
print(f"Optimal k value: {best_k}")
print("\n")
communities = find_communities_with_clique_percolation(G, best_k)
print("\n")

#%%
from networkx.algorithms.community.quality import modularity

# Define the range of k values to test
k_values = range(2, G.number_of_nodes())

best_k = 2
best_modularity = -1
best_coverage = -1
best_communities = None


# Usage:



for k in k_values:
    communities = find_communities_with_clique_percolation(G, k) # Use your implementation of the clique percolation algorithm
    partition, valid_communities = na.create_partition(G, communities)
    curr_modularity = modularity(G, valid_communities)
    curr_coverage = na.coverage(G, communities)
    
    # You can use modularity, coverage, or a combination of both to choose the best k
    if curr_modularity > best_modularity:
    #if curr_coverage > best_coverage:
        best_k = k
        best_modularity = curr_modularity
        best_coverage = curr_coverage
        best_communities = communities

print(f"Best k: {best_k}")
print(f"Best modularity: {best_modularity}")
print(f"Best coverage: {best_coverage}")
print(f"Best communities: {best_communities}")

print("\n")
print(f"Optimal k value: {best_k}")
print("\n")
communities = find_communities_with_clique_percolation(G, best_k)
print("\n")