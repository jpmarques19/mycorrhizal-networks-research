import networkx as nx


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
