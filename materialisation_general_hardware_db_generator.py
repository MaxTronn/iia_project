# Column name is the same as column name of mapping db
# subcategory needs to be null if it is of not that subcategory
# 3 tables will be present in the db

import json
import pandas as pd
import sqlite3

# Iterate over all the values in database_name in electrical_mapping table
db_file = "data_mapping/data_mapping.db"
conn = sqlite3.connect(db_file)



query = 'SELECT * FROM general_hardware_mapping'
cursor = conn.cursor()
cursor.execute(query)
rows = cursor.fetchall()

sql_column_names = ["database_name", "products", "categories", "sub_categories", "tools",
                    "electrical_supplies",  "building_materials", "safety_equipment", "hand_tools",
                    "measuring_tools", "power_tools", "helmets", "gloves",
                    "tiles", "paint", "lumber", "cement", "plumbing", "interior", "exterior",
                    "hardwood", "softwood", "composite_wood", "lighting", "wires", "batteries",
                    "item_id", "item_brand", "item_price", "item_size",
                    "item_quantity", "item_details", "item_name"]



items_df = pd.DataFrame()

general_hardware_df_list = []

for tup in rows:

    id_str = tup[-7] + ".$oid"
    tup_1 = tup[:-7] + (id_str,) + tup[-6:]
    tup = tup_1

    # KEY = Actual Column name, VALUE = current column name
    column_mapping = {tup[i]: sql_column_names[i] for i in range(len(tup))}

    # Opening JSON file
    json_file_name = tup[0]
    f = open(f'shop-items/general-hardware/{json_file_name}.json')
    json_data = json.load(f)
    category_1 = tup[4]
    category_2 = tup[4]
    category_3 = tup[5]
    category_4 = tup[6]

    # Iterate over subcategories
    # create a df for each subcategory
    # insert df[category] = 1
    # combine all dfs for that subcategory

    for product in json_data:
        for key, items in product.items():

            categories_df_list = []

            for category in items[0]["categories"]:



                for dict in items[0][category]:

                    sub_categories_df_list = []


                    for sub_category in dict["sub_categories"]:

                        # Check for sub_sub_category
                        if(len(dict[sub_category]) == 1):
                            sub_sub_categories_df_list = []


                            for sub_sub_category in dict[sub_category][0]["sub_categories"]:
                                sub_df = pd.json_normalize(dict[sub_category][0][sub_sub_category])
                                sub_df[sub_sub_category] = 1
                                sub_sub_categories_df_list.append(sub_df)

                            sub_categories_merged_df = pd.concat(sub_sub_categories_df_list, ignore_index=True)
                            sub_categories_merged_df[sub_category] = 1
                            sub_categories_df_list.append(sub_categories_merged_df)

                        else:
                            df = pd.json_normalize(dict[sub_category])
                            df[sub_category] = 1
                            sub_categories_df_list.append(df)

                    sub_categories_merged_df = pd.concat(sub_categories_df_list, ignore_index=True)
                    sub_categories_merged_df[category] = 1
                    categories_df_list.append(sub_categories_merged_df)

            merged_categories_df = pd.concat(categories_df_list, ignore_index=True)
            merged_categories_df["db_name"] = tup[0]

            general_hardware_df_list.append(merged_categories_df)

items_df = pd.concat(general_hardware_df_list, ignore_index=True)
items_df.rename(columns=column_mapping, inplace=True)




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

# data_type = merged_df.at[15, "item_size"]
# print(data_type)
# print(type(data_type))


# Function to convert lists to strings
def convert_to_string(value):
    if isinstance(value, list):
        return ', '.join(map(str, value))
    else:
        return str(value)

# Apply the function to the DataFrame
merged_df = merged_df.applymap(convert_to_string)

# Save the Dataframe as .db file
db_file = 'materialised_items_database/materialised_items.db'
conn = sqlite3.connect(db_file)
merged_df.to_sql('general_hardware_items', conn, if_exists='replace', index=False)
conn.commit()
conn.close()

