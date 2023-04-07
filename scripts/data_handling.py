import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram

def read_and_preprocess_data(file_path, plot_number):
    df = pd.read_csv(file_path)
    df_plot = df[df['Plot'] == f'Plot {plot_number}'].drop(['Plot', 'Site', 'UTM_X', 'UTM_Y'], axis=1)
    df_plot = df_plot.drop_duplicates(subset=["SmpleID"])
    return df_plot

def hierachical_clustering(adjacency_matrix, method="single"):
    linkage_matrix = linkage(adjacency_matrix, method=method)
    order = np.argsort(dendrogram(linkage_matrix)['leaves'])
    return adjacency_matrix[:, order][order, :]

