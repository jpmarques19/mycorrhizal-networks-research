import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import data_handling as dh
import network_analysis as na
import visualization as vis

#%%
df_plot1 = dh.read_and_preprocess_data('../data/01_SampleData.csv', 1)
df_plot6 = dh.read_and_preprocess_data('../data/01_SampleData.csv', 6)

#%%
unique_tree_connections1 = na.get_unique_tree_connections(df_plot1)
unique_tree_connections6 = na.get_unique_tree_connections(df_plot6)

#%% Create adjancecy matrix
unique_tree_genotypes1 = df_plot1['TreeID'].unique()
adj_matrix1 = na.create_adjacency_matrix(unique_tree_connections1, unique_tree_genotypes1).values
unique_tree_genotypes6 = df_plot6['TreeID'].unique()
adj_matrix6 = na.create_adjacency_matrix(unique_tree_connections6, unique_tree_genotypes6).values
#%% plot adj matrix
vis.plot_adjacency_matrix(adj_matrix1, 'Plot 1')
vis.plot_adjacency_matrix(adj_matrix6, 'Plot 6')

#%% Create graph from adj matrix

# Create an empty graph
G1 = dh.build_graph_from_adjacency_matrix(adj_matrix1)
G6 = dh.build_graph_from_adjacency_matrix(adj_matrix6)

#%% Calculate Centralities

# Degree centrality
degree_centrality1 = na.degree_centrality(G1)
degree_centrality2 = na.degree_centrality(G6)

# Closeness centrality
closeness_centrality1 = na.closeness_centrality(G1)
closeness_centrality2 = na.closeness_centrality(G6)

# Betweenness centrality
betweenness_centrality1 = na.betweenness_centrality(G1)
betweenness_centrality2 = na.betweenness_centrality(G6)

# Eigenvector centrality
eigenvector_centrality1 = na.eigenvector_centrality(G1)
eigenvector_centrality2 = na.eigenvector_centrality(G6)


#%%
# Define the colors
bar_color = '#663399'  # Purple
background_color = '#FFFFFF'  # White

# Set the Seaborn context and style
sns.set(context='talk', style='white', font='sans-serif', font_scale=1, rc=None)

# Set the background color
sns.set_style("white", {'axes.facecolor': background_color, 'figure.facecolor': background_color})


#%%
# Convert dictionaries to dataframes
df_degree1 = pd.DataFrame.from_dict(degree_centrality1, orient='index', columns=['degree_centrality'])
df_degree2 = pd.DataFrame.from_dict(degree_centrality2, orient='index', columns=['degree_centrality'])

# Compare Every Centrality with bar plots, side by side
fig, (ax1, ax2) = plt.subplots(1, 2, dpi=150)
sns.barplot(x=df_degree1.index, y='degree_centrality', data=df_degree1, ax=ax1, color=bar_color)
sns.barplot(x=df_degree2.index, y='degree_centrality', data=df_degree2, ax=ax2, color=bar_color)
ax1.set_title('Plot 1', fontsize=8)
ax2.set_title('Plot 6', fontsize=8)
ax1.set_xlabel('Tree ID', fontsize=6)
ax2.set_xlabel('Tree ID', fontsize=6)
ax1.set_ylabel('Degree Centrality', fontsize=6)
ax2.set_ylabel('Degree Centrality', fontsize=6)
ax1.tick_params(axis='both', which='major', labelsize=4)
ax2.tick_params(axis='both', which='major', labelsize=4)
plt.show()
#%%
print("Degree Centrality for Network 1:")
print(df_degree1)

print("\nDegree Centrality for Network 2:")
print(df_degree2)



#%%
# Convert dictionaries to dataframes
df_closeness1 = pd.DataFrame.from_dict(closeness_centrality1, orient='index', columns=['closeness_centrality'])
df_closeness2 = pd.DataFrame.from_dict(closeness_centrality2, orient='index', columns=['closeness_centrality'])

#%%
print("Closeness Centrality for Network 1:")
print(df_closeness1)

print("\nCloseness Centrality for Network 2:")
print(df_closeness2)
#%%
# Compare Every Centrality with bar plots, side by side
fig, (ax1, ax2) = plt.subplots(1, 2, dpi=150)
sns.barplot(x=df_closeness1.index, y='closeness_centrality', data=df_closeness1, ax=ax1, color=bar_color)
sns.barplot(x=df_closeness2.index, y='closeness_centrality', data=df_closeness2, ax=ax2, color=bar_color)
ax1.set_title('Plot 1', fontsize=8)
ax2.set_title('Plot 6', fontsize=8)
ax1.set_xlabel('Tree ID', fontsize=6)
ax2.set_xlabel('Tree ID', fontsize=6)
ax1.set_ylabel('Closeness Centrality', fontsize=6)
ax2.set_ylabel('Closeness Centrality', fontsize=6)
ax1.tick_params(axis='both', which='major', labelsize=4)
ax2.tick_params(axis='both', which='major', labelsize=4)
plt.show()

#%%
# Convert dictionaries to dataframes
df_betweenness1 = pd.DataFrame.from_dict(betweenness_centrality1, orient='index', columns=['betweenness_centrality'])
df_betweenness2 = pd.DataFrame.from_dict(betweenness_centrality2, orient='index', columns=['betweenness_centrality'])
#%%
print("Betweennees Centrality for Network 1:")
print(df_betweenness1)

print("\nBetweennees Centrality for Network 2:")
print(df_betweenness2)
#%%
# Compare Every Centrality with bar plots, side by side
fig, (ax1, ax2) = plt.subplots(1, 2, dpi=150)
sns.barplot(x=df_betweenness1.index, y='betweenness_centrality', data=df_betweenness1, ax=ax1, color=bar_color)
sns.barplot(x=df_betweenness2.index, y='betweenness_centrality', data=df_betweenness2, ax=ax2, color=bar_color)

ax1.set_title('Plot 1', fontsize=8)
ax2.set_title('Plot 6', fontsize=8)
ax1.set_xlabel('Tree ID', fontsize=6)
ax2.set_xlabel('Tree ID', fontsize=6)
ax1.set_ylabel('Betweenness Centrality', fontsize=6)
ax2.set_ylabel('Betweenness Centrality', fontsize=6)
ax1.tick_params(axis='both', which='major', labelsize=4)
ax2.tick_params(axis='both', which='major', labelsize=4)
plt.show()

#%%
# Convert dictionaries to dataframes
df_eigenvector1 = pd.DataFrame.from_dict(eigenvector_centrality1, orient='index', columns=['eigenvector_centrality'])
df_eigenvector2 = pd.DataFrame.from_dict(eigenvector_centrality2, orient='index', columns=['eigenvector_centrality'])

#%%
print("Eigenvector Centrality for Network 1:")
print(df_eigenvector1)

print("\nEigenvector Centrality for Network 2:")
print(df_eigenvector2)
#%%

# Compare Every Centrality with bar plots, side by side
fig, (ax1, ax2) = plt.subplots(1, 2, dpi=150)
sns.barplot(x=df_eigenvector1.index, y='eigenvector_centrality', data=df_eigenvector1, ax=ax1, color=bar_color)
sns.barplot(x=df_eigenvector2.index, y='eigenvector_centrality', data=df_eigenvector2, ax=ax2, color=bar_color)
ax1.set_title('Plot 1', fontsize=8)
ax2.set_title('Plot 6', fontsize=8)
ax1.set_xlabel('Tree ID', fontsize=6)
ax2.set_xlabel('Tree ID', fontsize=6)
ax1.set_ylabel('Eigenvector Centrality', fontsize=6)
ax2.set_ylabel('Eigenvector Centrality', fontsize=6)
ax1.tick_params(axis='both', which='major', labelsize=4)
ax2.tick_params(axis='both', which='major', labelsize=4)
plt.show()
