import numpy as np
import networkx as nx
import math
from networkx.algorithms.community import k_clique_communities

def network_properties(G):
    """
    Calculates various network properties for a given graph.

    Parameters:
    - G (networkx.Graph): Graph to analyze

    Returns:
    - avg_degree (float): Average degree of the graph
    - deg_dist (dict): Degree distribution of the graph
    - net_diameter (int): Diameter of the graph
    - clus_coeff (float): Clustering coefficient of the graph
    - conn_comps (int): Number of connected components in the graph
    - net_density (float): Density of the graph
    """
    avg_degree = average_degree(G)
    deg_dist = degree_distribution(G)
    net_diameter = network_diameter(G)
    clus_coeff = clustering_coefficient(G)
    conn_comps = len(list(nx.connected_components(G)))
    net_density = network_density(G)

    return avg_degree, deg_dist, net_diameter, clus_coeff, conn_comps, net_density


def average_degree(G):
    return sum(dict(G.degree()).values()) / len(G)

def degree_distribution(G):
    degrees = dict(G.degree())
    degree_counts = {}
    for degree in degrees.values():
        if degree not in degree_counts:
            degree_counts[degree] = 1
        else:
            degree_counts[degree] += 1
    for degree in degree_counts:
        degree_counts[degree] /= len(G)
    return degree_counts

def network_diameter(G):
    return nx.diameter(G)

def clustering_coefficient(G):
    return nx.average_clustering(G)

def connected_components(G):
    return list(nx.connected_components(G))

def network_density(G):
    return nx.density(G)



def degree_centrality(G):
    return nx.degree_centrality(G)

def closeness_centrality(G):
    return nx.closeness_centrality(G)

def betweenness_centrality(G):
    return nx.betweenness_centrality(G, normalized=True, endpoints=False)

def eigenvector_centrality(G):
    return nx.eigenvector_centrality(G)


#%% community analysis

def entropy(community_sizes, total_nodes):
    # Account for isolated nodes
    isolated_nodes = total_nodes - sum(community_sizes)
    community_sizes += [1] * isolated_nodes

    # Calculate proportions
    proportions = np.array(community_sizes) / total_nodes
    
    # Calculate entropy
    entropy = -np.sum(proportions * np.log(proportions))
    return entropy

def entropy_shared_nodes(community_sizes, total_nodes, communities):
    # Create a dictionary to store the count of shared nodes
    shared_node_count = {}

    # Iterate through each community and count the shared nodes
    for community in communities:
        for node in community:
            shared_node_count[node] = shared_node_count.get(node, 0) + 1

    # Adjust community_sizes to account for shared nodes
    adjusted_community_sizes = []
    for community in communities:
        adjusted_size = sum(1 / shared_node_count[node] for node in community)
        adjusted_community_sizes.append(adjusted_size)

    # Account for isolated nodes
    isolated_nodes = total_nodes - sum(adjusted_community_sizes)
    adjusted_community_sizes += [1] * int(isolated_nodes)

    # Calculate proportions
    proportions = np.array(adjusted_community_sizes) / total_nodes

    # Calculate entropy
    entropy = -np.sum(proportions * np.log(proportions))
    return entropy


def community_sizes_with_shared_nodes(community_list):
    node_counts = {}
    for community in community_list:
        for node in community:
            node_counts[node] = node_counts.get(node, 0) + 1
    
    community_sizes = []
    for community in community_list:
        size = sum(1 / node_counts[node] for node in community)
        community_sizes.append(size)

    return community_sizes

def count_isolated_nodes(community_list, total_nodes):
    all_nodes = set(range(total_nodes))
    connected_nodes = set()
    for community in community_list:
        connected_nodes.update(community)
    return len(all_nodes - connected_nodes)


def coverage(G, communities):
    intra_edges = sum(G.subgraph(c).number_of_edges() for c in communities)
    total_edges = G.number_of_edges()
    return intra_edges / total_edges

def create_partition(G, communities):
    partition = {}
    for i, community in enumerate(communities):
        for node in community:
            partition[node] = i

    # Handle isolated nodes
    for node in G.nodes:
        if node not in partition:
            partition[node] = len(communities)
            communities.append({node})

    # Convert communities to a list of sets for compatibility with modularity function
    communities = [set(community) for community in communities]
    
    return partition, communities

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

def get_k_cliques_in_communities(G, communities, k):
    k_cliques = nx.find_cliques(G)
    k_cliques = [clique for clique in k_cliques if len(clique) == k]
    
    community_k_cliques = []
    for community in communities:
        community_cliques = []
        for clique in k_cliques:
            if set(clique).issubset(community):
                community_cliques.append(clique)
        community_k_cliques.append(community_cliques)
    
    return community_k_cliques


def find_optimal_k(network, k_range):
    max_entropy = -np.inf
    optimal_k = None

    for k in k_range:
        communities = find_communities_with_clique_percolation(network, k)
        community_sizes = [len(community) for community in communities]
        total_nodes = sum(community_sizes)
        entropy = entropy_shared_nodes(community_sizes, total_nodes, communities)

        if entropy > max_entropy:
            max_entropy = entropy
            optimal_k = k

    return optimal_k
