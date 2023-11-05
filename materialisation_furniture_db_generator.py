# Column name is the same as column name of mapping db
# subcategory needs to be null if it is of not that subcategory
# 3 tables will be present in the db

import json
import pandas as pd
import sqlite3

# Iterate over all the values in database_name in electrical_mapping table
db_file = "data_mapping/data_mapping.db"
conn = sqlite3.connect(db_file)


# Add '.$oid' to each item_id
query = "UPDATE furniture_mapping SET item_id = (item_id || '.$oid');"
cursor = conn.cursor()
cursor.execute(query)
conn.commit()


query = 'SELECT * FROM furniture_mapping'
cursor = conn.cursor()
cursor.execute(query)
rows = cursor.fetchall()

sql_column_names = ["database_name", "categories", "products", "Tables", "Cabinets", "Beds",
                    "Sofas", "Chairs", "item_id", "item_type", "item_brand", "item_price", "item_size",
                    "item_quantity", "item_shape"]


items_df = pd.DataFrame()

for tup in rows:

    # KEY = Actual Column name, VALUE = current column name
    column_mapping = {tup[i]: sql_column_names[i] for i in range(len(tup))}

    # Opening JSON file
    json_file_name = tup[0]
    f = open(f'shop-items/furniture/{json_file_name}.json')
    json_data = json.load(f)
    Tables = tup[3]
    Cabinets = tup[4]
    Beds = tup[5]
    Sofas = tup[6]
    Chairs = tup[7]

    for product in json_data:
        for category, items in product.items():
            df_1 = pd.json_normalize(items[0][Tables])
            df_1[Tables] = 1
            df_1[Cabinets] = 0
            df_1[Beds] = 0
            df_1[Sofas] = 0
            df_1[Chairs] = 0

            df_2 = pd.json_normalize(items[0][Cabinets])
            df_2[Tables] = 0
            df_2[Cabinets] = 1
            df_2[Beds] = 0
            df_2[Sofas] = 0
            df_2[Chairs] = 0

            df_3 = pd.json_normalize(items[0][Beds])
            df_3[Tables] = 0
            df_3[Cabinets] = 0
            df_3[Beds] = 1
            df_3[Sofas] = 0
            df_3[Chairs] = 0

            df_4 = pd.json_normalize(items[0][Sofas])
            df_4[Tables] = 0
            df_4[Cabinets] = 0
            df_4[Beds] = 0
            df_4[Sofas] = 1
            df_4[Chairs] = 0

            df_5 = pd.json_normalize(items[0][Chairs])
            df_5[Tables] = 0
            df_5[Cabinets] = 0
            df_5[Beds] = 0
            df_5[Sofas] = 0
            df_5[Chairs] = 1

            df = pd.concat([df_1, df_2, df_3, df_4, df_5], ignore_index=True)
            df.rename(columns=column_mapping, inplace=True)
            df["db_name"] = tup[0]

            items_df = pd.concat([df, items_df], ignore_index=True)




# Add Shop Details
shops_df = pd.DataFrame(columns=[ "store_name", "store_id", "latitude", "longitude", "db_name"])

db_file = "shop-details/shopkeeper-details.db"
conn = sqlite3.connect(db_file)
query = 'SELECT * FROM shopkeepers'
cursor = conn.cursor()
cursor.execute(query)
rows = cursor.fetchall()

for tup in rows:
    shops_df = shops_df.append(pd.Series([tup[1], tup[0], tup[3], tup[4], tup[5]], index=shops_df.columns), ignore_index=True)



# Merge Items df and shops df
merged_df = pd.merge(shops_df, items_df, on='db_name', how='inner')
merged_df = merged_df.drop(columns=["db_name"])
merged_df.insert(0, 'id', range(1, len(merged_df) + 1))
# print(merged_df)



# Save the Dataframe as .db file
db_file = 'materialised_items_database/materialised_items.db'
conn = sqlite3.connect(db_file)
merged_df.to_sql('furniture_items', conn, if_exists='replace', index=False)
conn.commit()
conn.close()