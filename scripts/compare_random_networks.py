import networkx as nx
import matplotlib.pyplot as plt

# Generate the two graphs
G1 = nx.erdos_renyi_graph(10, 0.2)
G2 = nx.erdos_renyi_graph(10, 0.5)

# Create the figure and axes objects
fig, axes = plt.subplots(1, 2, figsize=(8, 4), dpi=100)

# Plot the first graph on the left axis
pos1 = nx.spring_layout(G1)
nx.draw(G1, pos1, ax=axes[0])
axes[0].set_title("Graph 1")

# Plot the second graph on the right axis
pos2 = nx.spring_layout(G2)
nx.draw(G2, pos2, ax=axes[1])
axes[1].set_title("Graph 2")

# Show the plot
plt.show()
