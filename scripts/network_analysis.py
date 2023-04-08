import networkx as nx

def generate_random_network_from_graph(G):
    """
    Generates an Erdos-Renyi random graph with the same number of nodes and edge probability as a given graph.

    Parameters:
        G (networkx.Graph): The input graph for which an Erdos-Renyi random graph will be generated.

    Returns:
        random_graph (networkx.Graph): An Erdos-Renyi random graph with the same number of nodes and edge probability as the input graph.
    """

    # Get the number of nodes and edges in the input graph
    n = G.number_of_nodes()
    m = G.number_of_edges()

    # Calculate the edge probability for the random graph
    p = (2 * m) / (n * (n - 1))

    # Generate the random graph using the calculated edge probability
    random_graph = nx.erdos_renyi_graph(n, p, seed=None, directed=False)

    return random_graph


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
