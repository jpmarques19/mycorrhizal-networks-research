import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

# Read data
plot1_data = pd.read_csv("data/plot1_data.csv")
plot1_tree_data = pd.read_csv("data/Plot1_Tree_Data.csv")
adjacency_matrix = pd.read_csv("data/adjacency_matrix_plot1.csv", index_col=0)

# Prepare data
tree_coord = plot1_tree_data[['TreeID', 'Tree_X', 'Tree_Y']].set_index('TreeID')
tree_coord = tree_coord.rename(columns={'Tree_X': 'x', 'Tree_Y': 'y'})
pos = {k: (v['x'], v['y']) for k, v in tree_coord.to_dict('index').items()}
labels = plot1_tree_data['TreeID'].tolist()

# Create graph from DataFrame
g = nx.from_pandas_adjacency(adjacency_matrix)

# Add node positions and labels to graph
nx.set_node_attributes(g, pos, "pos")
nx.set_node_attributes(g, dict(zip(labels, labels)), "label")

# ORIGINAL NETWORK

nx.draw(g, pos, labels=dict(zip(labels, labels)))

g.remove_nodes_from(['P1-T080'])

degree_centrality_original = nx.degree_centrality(g)
closeness_centrality_original = nx.closeness_centrality(g)
betweenness_centrality_original = nx.betweenness_centrality(g)


# calculate the eccentricity of each node
eccentricity = nx.eccentricity(g)

# find the maximum eccentricity value in the graph
max_eccentricity = max(eccentricity.values())

# calculate the eccentricity centrality of each node
eccentricity_centrality = {}
for node in g.nodes():
    eccentricity_centrality[node] = 1.0 / eccentricity[node]

# convert the dictionary to a DataFrame
eccentricity_centrality_df = pd.DataFrame.from_dict(eccentricity_centrality, orient='index', columns=['Eccentricity Centrality'])

# add a column for the node IDs
eccentricity_centrality_df.index.name = 'Node'
# export the DataFrame to a CSV file
eccentricity_centrality_df.to_csv('eccentricity_centrality_original.csv')

# Convert the centrality measures to DataFrames
degree_centrality_df = pd.DataFrame(list(degree_centrality_original.items()), columns=["Node", "Degree Centrality"])
closeness_centrality_df = pd.DataFrame(list(closeness_centrality_original.items()), columns=["Node", "Closeness Centrality"])
betweenness_centrality_df = pd.DataFrame(list(betweenness_centrality_original.items()), columns=["Node", "Betweenness Centrality"])

# Export the DataFrames to CSV files
degree_centrality_df.to_csv("degree_centrality_original.csv", index=False)
closeness_centrality_df.to_csv("closeness_centrality_original.csv", index=False)
betweenness_centrality_df.to_csv("betweenness_centrality_original.csv", index=False)


# CHANGED NETWORK

# Remove nodes
g.remove_nodes_from(['P1-T041', 'P1-T026', 'P1-T080'])

# Calculate connected components
connected_components = list(nx.connected_components(g))
num_components = len(connected_components)

# Set node colors based on connected component
colors = {}
for i, component in enumerate(connected_components):
    for node in component:
        colors[node] = i

# Set node size and edge width
node_size = 80
edge_width = 2

# Set font size for node labels
font_size = 12

# Set color palette for connected components (pastel colors)
color_palette = sns.color_palette("pastel", num_components)

# Custom edge colors for components 1 and 3
edge_colors = ['#2a9d8f', '#e63946']

# Draw graph with customizations
plt.figure(figsize=(14, 10))

for i, component in enumerate(connected_components):
    color = color_palette[i]
    node_color = color
    edge_color = color
    if i in [0, 2]: # make the edges of components 1 and 3 more distinguishable
        edge_color = edge_colors[i // 2]
    nx.draw_networkx_nodes(g, pos, nodelist=component, node_color=node_color, node_size=node_size)
    nx.draw_networkx_edges(g, pos, edgelist=g.edges(component), edge_color=edge_color, width=edge_width, alpha=0.7)

# Add node labels
nx.draw_networkx_labels(g, pos, labels=dict(zip(labels, labels)), font_size=font_size)

# Add legend for connected components
legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color_palette[i], markersize=10) for i in range(num_components)]
plt.legend(legend_handles, [f"Component {i+1}" for i in range(num_components)], loc="upper right", prop={'size': 12})

# Show the plot
plt.axis("off")
plt.show()


#g.remove_nodes_from(['P1-T057', 'P1-T033', 'P1-T048'])

degree_centrality = nx.degree_centrality(g)
closeness_centrality = nx.closeness_centrality(g)
betweenness_centrality = nx.betweenness_centrality(g)



# Convert the centrality measures to DataFrames
degree_centrality_df = pd.DataFrame(list(degree_centrality.items()), columns=["Node", "Degree Centrality"])
closeness_centrality_df = pd.DataFrame(list(closeness_centrality.items()), columns=["Node", "Closeness Centrality"])
betweenness_centrality_df = pd.DataFrame(list(betweenness_centrality.items()), columns=["Node", "Betweenness Centrality"])

# Export the DataFrames to CSV files
degree_centrality_df.to_csv("degree_centrality_modified.csv", index=False)
closeness_centrality_df.to_csv("closeness_centrality_modified.csv", index=False)
betweenness_centrality_df.to_csv("betweenness_centrality_modified.csv", index=False)

# calculate the eccentricity of each node
eccentricity = nx.eccentricity(g)

# find the maximum eccentricity value in the graph
max_eccentricity = max(eccentricity.values())

# calculate the eccentricity centrality of each node
eccentricity_centrality = {}
for node in g.nodes():
    eccentricity_centrality[node] = 1.0 / eccentricity[node]

# convert the dictionary to a DataFrame
eccentricity_centrality_df = pd.DataFrame.from_dict(eccentricity_centrality, orient='index', columns=['Eccentricity Centrality'])

# add a column for the node IDs
eccentricity_centrality_df.index.name = 'Node'
# export the DataFrame to a CSV file
eccentricity_centrality_df.to_csv('eccentricity_centrality.csv')


# Read the centrality CSV files for both original and modified networks
degree_original = pd.read_csv("degree_centrality_original.csv")
degree_modified = pd.read_csv("degree_centrality.csv")
closeness_original = pd.read_csv("closeness_centrality_original.csv")
closeness_modified = pd.read_csv("closeness_centrality.csv")
betweenness_original = pd.read_csv("betweenness_centrality_original.csv")
betweenness_modified = pd.read_csv("betweenness_centrality.csv")

# Merge the DataFrames for each centrality measure
degree_merged = degree_original.merge(degree_modified, on="Node", suffixes=("_original", "_modified"))
closeness_merged = closeness_original.merge(closeness_modified, on="Node", suffixes=("_original", "_modified"))
betweenness_merged = betweenness_original.merge(betweenness_modified, on="Node", suffixes=("_original", "_modified"))

# Calculate the difference in centrality values
degree_merged["degree_difference"] = degree_merged["Degree Centrality_modified"] - degree_merged["Degree Centrality_original"]
closeness_merged["closeness_difference"] = closeness_merged["Closeness Centrality_modified"] - closeness_merged["Closeness Centrality_original"]
betweenness_merged["betweenness_difference"] = betweenness_merged["Betweenness Centrality_modified"] - betweenness_merged["Betweenness Centrality_original"]

# Visualize the differences using bar plots
degree_merged.plot(x="Node", y="degree_difference", kind="bar", figsize=(15, 6), title="Difference in Degree Centrality")
closeness_merged.plot(x="Node", y="closeness_difference", kind="bar", figsize=(15, 6), title="Difference in Closeness Centrality")
betweenness_merged.plot(x="Node", y="betweenness_difference", kind="bar", figsize=(15, 6), title="Difference in Betweenness Centrality")

plt.show()
