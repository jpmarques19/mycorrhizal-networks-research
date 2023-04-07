import pandas as pd

def read_and_preprocess_data(file_path, plot_number):
    df = pd.read_csv(file_path)

    df_plot = df[df['Plot'] == f'Plot {plot_number}'].drop(['Plot', 'Site', 'UTM_X', 'UTM_Y'], axis=1)
    df_plot = df_plot.drop_duplicates(subset=["SmpleID"])

    return df_plot