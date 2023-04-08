import networkx as nx

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
