import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import itertools

# Plot the barplot with green tones. Every bar same color intensity
def plot_barplot(df, title, y_label):
    # Create a figure and axes object
    fig, ax = plt.subplots(dpi=150)
    
    # Plot the barplot
    sns.barplot(x=df.index, y='degree_centrality', data=df, ax=ax, color='green')
    
    # Set the title and labels
    ax.set_title(title, fontsize=8)
    ax.set_xlabel('Tree ID', fontsize=6)
    ax.set_ylabel(y_label, fontsize=6)
    
    # Set the fontsize of the tick labels
    ax.tick_params(axis='both', which='major', labelsize=4)
    
    # Show the plot
    plt.show()

# Plot circular graphs  side by side
def plot_circular_graphs(G1, G2, title1, title2):
    # Generate the circular layouts
    pos1 = nx.circular_layout(G1)
    pos2 = nx.circular_layout(G2)

    # Set node properties
    node_color = 'lightgreen'
    node_edge_color = 'black'
    node_size = 100
    node_alpha = 0.8

    # Set edge properties
    edge_color = 'black'
    edge_width = 0.5

    # Set label properties
    font_size = 6
    font_color = 'black'
    font_weight = 'bold'

    # Create the figure and axes
    fig, axes = plt.subplots(dpi=150, ncols=2, figsize=(10, 5))

    # Plot the first ER random network
    nx.draw_networkx_nodes(G1, pos1, node_color=node_color, edgecolors=node_edge_color, node_size=node_size, alpha=node_alpha, ax=axes[0])
    nx.draw_networkx_edges(G1, pos1, edge_color=edge_color, width=edge_width, ax=axes[0])
    axes[0].axis('off')
    axes[0].set_title(title1, fontsize=8)

    # Plot the second ER random network
    nx.draw_networkx_nodes(G2, pos2, node_color=node_color, edgecolors=node_edge_color, node_size=node_size, alpha=node_alpha, ax=axes[1])
    nx.draw_networkx_edges(G2, pos2, edge_color=edge_color, width=edge_width, ax=axes[1])
    axes[1].axis('off')
    axes[1].set_title(title2, fontsize=8)

    # Show the plot
    plt.show()                                          

def plot_adjacency_matrix(adj_matrix, title):
    # Create a figure and axes object
    fig, ax = plt.subplots(dpi=150)
    
    # Plot the adjacency matrix
    im = ax.imshow(adj_matrix, cmap='binary')
    
    # Set the tick labels
    ax.set_xticks(np.arange(len(adj_matrix)))
    ax.set_yticks(np.arange(len(adj_matrix)))
    ax.set_xticklabels(np.arange(1, len(adj_matrix)+1))
    ax.set_yticklabels(np.arange(1, len(adj_matrix)+1))
    
    # Rotate the tick labels and set their alignment
    plt.setp(ax.get_xticklabels(), rotation=0, ha="center", va="center")
    plt.setp(ax.get_yticklabels(), rotation=0, ha="right", va="center")
    
    # Set the fontsize of the tick labels
    ax.tick_params(axis='both', which='major', labelsize=4)
    
    # Add a title
    ax.set_title(title, fontsize=8)
    
    # Show the plot
    plt.show()
    
def plot_degree_distribution(G, title):
    degrees = dict(G.degree())
    degree_values = sorted(set(degrees.values()))
    histogram = [list(degrees.values()).count(i) / float(nx.number_of_nodes(G)) for i in degree_values]
    return degree_values, histogram

def plot_degree_distributions(G_exp, G_rand, exp_label, rand_label):
    degree_values_exp, histogram_exp = plot_degree_distribution(G_exp, exp_label)
    degree_values_rand, histogram_rand = plot_degree_distribution(G_rand, rand_label)
    
    fig, ax = plt.subplots()
    ax.bar(degree_values_exp, histogram_exp, alpha=0.8, label=exp_label, width=0.4, align='center')
    ax.bar(degree_values_rand, histogram_rand, alpha=0.8, label=rand_label, width=0.4, align='edge')
    
    ax.set_xlabel("Degree")
    ax.set_ylabel("Fraction of Nodes")
    ax.set_title("Degree Distribution")
    ax.legend()
    plt.show()






