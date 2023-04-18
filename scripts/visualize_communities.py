import matplotlib.pyplot as plt
import data_handling as dh
import network_analysis as na
import visualization as vis
import networkx as nx

# Create a networkx graph from your adjacency matrix
G = dh.create_graph_from_plot_data('../data/01_SampleData.csv', 5)

communities = na.find_communities_with_clique_percolation(G, 9)

# Assign colors to nodes
node_colors = []
for node in G.nodes():
    if len(communities) > 2 and node in communities[0] & communities[1] & communities[2]:
        node_colors.append('purple')  # Purple for overlapping nodes in all three communities
    elif node in communities[0]:
        node_colors.append('red')  # Red for community 1
    elif node in communities[1]:
        node_colors.append('blue')  # Blue for community 2
    elif len(communities) > 2 and node in communities[2]:
        node_colors.append('green')  # Green for community 3
    else:
        node_colors.append('gray')  # Gray for other nodes

# Assign colors to edges
edge_colors = []
for edge in G.edges():
    if edge[0] in communities[0] and edge[1] in communities[0]:
        edge_colors.append('red')  # Red for edges within community 1
    elif edge[0] in communities[1] and edge[1] in communities[1]:
        edge_colors.append('blue')  # Blue for edges within community 2
    elif len(communities) > 2 and edge[0] in communities[2] and edge[1] in communities[2]:
        edge_colors.append('green')  # Green for edges within community 3
    else:
        edge_colors.append('gray')  # Gray for other edges

# Draw the network
pos = nx.kamada_kawai_layout(G)

# If you need to update the positions of specific nodes, uncomment and modify the lines below
# pos['node_name_1'] = (x_coordinate_1, y_coordinate_1)
# pos['node_name_2'] = (x_coordinate_2, y_coordinate_2)

fig, ax = plt.subplots(dpi=150)
nx.draw(G, pos, node_color=node_colors, edge_color=edge_colors, with_labels=True, node_size=150, font_size=6)
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=150, linewidths=1, edgecolors='black')

plt.title('Community Structure of Network $\mathcal{M}_C$')
plt.show()
