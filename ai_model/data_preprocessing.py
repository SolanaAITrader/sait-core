import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(data_path):
    data = pd.read_csv(data_path)
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)
    return scaled_data
