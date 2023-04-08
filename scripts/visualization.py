import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
