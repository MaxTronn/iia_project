import pandas as pd
import random
import numpy as np

# Read the first name and last name lists from text files
with open('data/first_name.txt', 'r') as f:
    first_names = f.read().splitlines()

with open('data/last_name.txt', 'r') as f:
    last_names = f.read().splitlines()


df = pd.DataFrame(columns=['id','name', 'service_id', 'charge'])
id = 1

# Generate random names and add them to the DataFrame
for _ in range(500):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    full_name = f'{first_name} {last_name}'
    service_id = random.randint(1,16)
    charge = random.randint(10, 24) * 50
    df = df.append({'id' : id,'name': full_name, 'service_id': service_id, 'charge': charge}, ignore_index=True)
    id+=1

df['phone_number'] = df.apply(lambda _: '+91' + ''.join(random.choices('0123456789', k=10)), axis=1)
df['available'] = 1

# Latitude : 28.38 --- 28.87
# Longitude : 76.5 ---- 77.2
df['latitude'] = np.random.uniform(low=28.38, high=28.87, size=len(df)).round(6)
df['longitude'] = np.random.uniform(low=76.5, high=77.2, size=len(df)).round(6)


# Generating a table to assign service id to each type of service
service_type_df = pd.DataFrame(columns=['id','service_type'])

service_type_df = service_type_df.append({'id' : 1, 'service_type': "electrician"}, ignore_index=True)
service_type_df = service_type_df.append({'id' : 2, 'service_type': "plumber"}, ignore_index=True)
service_type_df = service_type_df.append({'id' : 3, 'service_type': "mechanic"}, ignore_index=True)
service_type_df = service_type_df.append({'id' : 4, 'service_type': "welder"}, ignore_index=True)

service_type_df = service_type_df.append({'id' : 5, 'service_type': "painter"}, ignore_index=True)
service_type_df = service_type_df.append({'id' : 6, 'service_type': "carpenter"}, ignore_index=True)
service_type_df = service_type_df.append({'id' : 7, 'service_type': "barber"}, ignore_index=True)
service_type_df = service_type_df.append({'id' : 8, 'service_type': "tailor"}, ignore_index=True)

service_type_df = service_type_df.append({'id' : 9, 'service_type': "housekeeper"}, ignore_index=True)
service_type_df = service_type_df.append({'id' : 10, 'service_type': "cook"}, ignore_index=True)
service_type_df = service_type_df.append({'id' : 11, 'service_type': "makeup artist"}, ignore_index=True)
service_type_df = service_type_df.append({'id' : 12, 'service_type': "cobbler"}, ignore_index=True)

service_type_df = service_type_df.append({'id' : 13, 'service_type': "mason"}, ignore_index=True)
service_type_df = service_type_df.append({'id' : 14, 'service_type': "cobbler"}, ignore_index=True)
service_type_df = service_type_df.append({'id' : 15, 'service_type': "pest control"}, ignore_index=True)
service_type_df = service_type_df.append({'id' : 16, 'service_type': "appliance repair"}, ignore_index=True)


# print(df)
# print(service_type_df)

df.to_json('data/servicemen_global.json', orient='records')
service_type_df.to_json('data/service_type_global.json', orient='records')

