# Column name is the same as column name of mapping db
# subcategory needs to be null if it is of not that subcategory
# 3 tables will be present in the db

import json
import pandas as pd
import sqlite3

# Iterate over all the values in database_name in electrical_mapping table
db_file = "data_mapping/data_mapping.db"
conn = sqlite3.connect(db_file)

# query = "UPDATE electrical_mapping SET item_id = 'id.$oid';"
# cursor = conn.cursor()
# cursor.execute(query)
# conn.commit()

query = 'SELECT * FROM electrical_mapping'
cursor = conn.cursor()
cursor.execute(query)
rows = cursor.fetchall()

sql_column_names = ["database_name", "categories", "products", "TVs", "Laptops", "Home_Appliances",
                    "Smartphones", "item_id", "item_type", "item_brand", "item_price", "item_size",
                    "item_quantity", "item_name"]

items_df = pd.DataFrame()

for tup in rows:

    # KEY = Actual Column name, VALUE = current column name
    column_mapping = {tup[i]: sql_column_names[i] for i in range(len(tup))}

    # Opening JSON file
    json_file_name = tup[0]
    f = open(f'shop-items/electrical/{json_file_name}.json')
    json_data = json.load(f)
    category_1 = tup[3]
    category_2 = tup[4]
    category_3 = tup[5]
    category_4 = tup[6]

    for product in json_data:
        for category, items in product.items():
            df_1 = pd.json_normalize(items[0][category_1])
            df_1[category_1] = 1
            df_1[category_2] = 0
            df_1[category_3] = 0
            df_1[category_4] = 0

            df_2 = pd.json_normalize(items[0][category_2])
            df_2[category_1] = 0
            df_2[category_2] = 1
            df_2[category_3] = 0
            df_2[category_4] = 0

            df_3 = pd.json_normalize(items[0][category_3])
            df_3[category_1] = 0
            df_3[category_2] = 0
            df_3[category_3] = 1
            df_3[category_4] = 0

            df_4 = pd.json_normalize(items[0][category_4])
            df_4[category_1] = 0
            df_4[category_2] = 0
            df_4[category_3] = 0
            df_4[category_4] = 1

            df = pd.concat([df_1, df_2, df_3, df_4], ignore_index=True)
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

print(shops_df)



# Merge Items df and shops df
merged_df = pd.merge(shops_df, items_df, on='db_name', how='inner')
merged_df = merged_df.drop(columns=["db_name"])
merged_df.insert(0, 'id', range(1, len(merged_df) + 1))
# print(merged_df)



# Save the Dataframe as .db file
db_file = 'materialised_items_database/materialised_items.db'
conn = sqlite3.connect(db_file)
merged_df.to_sql('electrical_items', conn, if_exists='replace', index=False)
conn.commit()
conn.close()