import networkx as nx
import matplotlib.pyplot as plt

import data_handling as dh
import network_analysis as na
import visualization as vis
#%%
# Generate the two graphs
G1 = dh.create_graph_from_plot_data('../data/01_SampleData.csv', 1)
G6 = dh.create_graph_from_plot_data('../data/01_SampleData.csv', 6)

#%%
RG1 = dh.generate_random_network_from_graph(G1)
RG6 = dh.generate_random_network_from_graph(G6)

#%% remove isolated nodes
G1.remove_nodes_from(list(nx.isolates(G1)))
G6.remove_nodes_from(list(nx.isolates(G6)))
RG1.remove_nodes_from(list(nx.isolates(RG1)))
RG6.remove_nodes_from(list(nx.isolates(RG6)))

#%%
vis.plot_circular_graphs(G6, RG6, "Mycorrhizal Network $\mathcal{M}_B$", "Random E-R Network ")
vis.plot_circular_graphs(RG1, RG6, "RG1", "RG6")


#%%
# Calculate additional network parameters
G1_properties = na.network_properties(G1)
G6_properties = na.network_properties(G6)
RG1_properties = na.network_properties(RG1)
RG6_properties = na.network_properties(RG6)

#%% compare network properties
print("G1")
print(G1_properties)
print("G6")
print(G6_properties)
print("RG1")
print(RG1_properties)
print("RG6")
print(RG6_properties)

#%%

# Assuming you have already created the graphs G1, RG1, G6, and RG6
vis.plot_degree_distributions(G1, RG1, 'G1', 'RG1')
vis.plot_degree_distributions(G6, RG6, 'G6', 'RG6')
