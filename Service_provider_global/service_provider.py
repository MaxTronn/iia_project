import pandas as pd
import random
import string
import numpy as np
import sqlite3

df = pd.read_csv('service_provider.csv')


# Latitude : 28.38 --- 28.87
# Longitude : 76.5 ---- 77.2
df['latitude'] = np.random.uniform(low=28.38, high=28.87, size=len(df)).round(6)
df['longitude'] = np.random.uniform(low=76.5, high=77.2, size=len(df)).round(6)

db_file = "service_providers.db"
conn = sqlite3.connect(db_file)
df.to_sql("service_provers_table", con=conn, if_exists="replace", index=False)

print(df)
print(list(df.columns))