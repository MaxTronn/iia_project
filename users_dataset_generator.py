import pandas as pd
import random
import string
import numpy as np
import sqlite3

df = pd.read_csv('Indian_Names.csv')
df.rename(columns={'Name': 'name'}, inplace=True)
df.rename(columns={'Unnamed: 0': 'id'}, inplace=True)

df['email'] = df['name'] + '@gmail.com'
df['phone_number'] = df.apply(lambda _: '+91' + ''.join(random.choices('0123456789', k=10)), axis=1)
df['password'] = df.apply(lambda _: ''.join(random.choices(string.ascii_letters + string.digits, k=8)), axis=1)

# Latitude : 28.38 --- 28.87
# Longitude : 76.5 ---- 77.2
df['latitude'] = np.random.uniform(low=28.38, high=28.87, size=len(df)).round(6)
df['longitude'] = np.random.uniform(low=76.5, high=77.2, size=len(df)).round(6)

db_file = "users.db"
conn = sqlite3.connect(db_file)
df.to_sql("users_table", con=conn, if_exists="replace", index=False)

print(df)
print(list(df.columns))