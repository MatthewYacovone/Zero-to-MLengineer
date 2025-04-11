import numpy as np
import pandas as pd

data_path = 'ml-1m/ratings.dat'
df = pd.read_csv(data_path, header=None, sep='::', engine='python')
df.columns = ['user_id', 'movie_id', 'rating', 'timestamp']
print(df)