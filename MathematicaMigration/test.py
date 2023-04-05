import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge(1,2)
G.add_edge(2,3)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()
