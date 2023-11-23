import json
import os
import sqlite3


# synonym dictionary
synonyms={
    "products": ["products"],
    "categories": ["categories"],
    "sub_categories": ["sub_categories"],
    "TVs": ["TVs"],
    "Laptops": ["Laptops"],
    "Home_Appliances": ["Home Appliances"],
    "Smartphones": ["Smartphones"],
    "Tables": ["Tables"],
    "Cabinets": ["Cabinets"],
    "Beds": ["Beds"],
    "Sofas": ["Sofas"],
    "Chairs": ["Chairs"],
    "building_materials": ["building_materials"],
    "safety_equipment": ["safety_equipment"],
    "electrical_supplies": ["electrical_supplies"],
    "tools": ["tools"],
    "power_tools":["power_tools"],
    "hand_tools": ["hand_tools"],
    "measuring_tools": ["measuring_tools"],
    "helmets": ["helmets"],
    "gloves": ["gloves"],
    "tiles": ["tiles"],
    "paint": ["paint"],
    "lumber": ["lumber"],
    "cement": ["cement"],
    "plumbing": ["plumbing"],
    "interior": ["interior"],
    "exterior": ["exterior"],
    "softwood": ["softwood"],
    "hardwood": ["hardwood"],
    "composite_wood": ["composite_wood"],
    "batteries": ["batteries"],
    "lighting": ["lighting"],
    "wires": ["wires"],
    "item_id":["id"],
    "item_type":["item_type","type"],
    "item_brand":["item_brand","brand"],
    "item_price":["item_price","price"],
    "item_size":["item_size","size"],
    "item_quantity": ["item_quantity","quantity"],
    "item_shape": ["item_shape","shape"],
    "item_details" : ["item_details","details"],
    "item_name" : ["item_name","name"]
}


product_attr = ""
categories_attr = ""
TVs_attr = ""
Laptops_attr = ""
Home_Appliances_attr = ""
Smartphones_attr = ""
item_id_attr = ""
item_type_attr = ""
item_brand_attr = ""
item_price_attr = ""
item_size_attr = ""
item_quantity_attr = ""
item_name_attr = ""

# Function to find the mapped attribute in a local database
def find_mapped_attribute(db_name, subfolder, synonyms, attribute_type):
    path=folder_path+subfolder+"/"+db_name+".json"
    print("attribute_type"+attribute_type)
    print(path)
    print(db_name)
    with open(path, 'r') as file:
        json_data = file.read()

    data = json.loads(json_data)
    data_dict=data[0]
    
    #print(data_dict)
    if attribute_type == "products":
        for synonym in synonyms[attribute_type]:
            for key in data_dict:
                if(key==synonym):
                    return key
    elif attribute_type in ["categories", "TVs", "Laptops", "Home_Appliances", "Smartphones"]:
        val=data_dict.get(product_attr)
        print(product_attr+"Hi")
        sub_dict=val[0]

        for synonym in synonyms[attribute_type]:
            for key in sub_dict:
                if(key==synonym):
                    return key      
                
    elif attribute_type in ["item_id", "item_type", "item_brand", "item_price", "item_size", "item_quantity"]:
        val=data_dict.get(product_attr)
        sub_dict=val[0]
        item_list=sub_dict.get(TVs_attr)
        item=item_list[0]

        for synonym in synonyms[attribute_type]:
            for key in item:
                if(key==synonym):
                    return key 
                
    elif attribute_type == "item_name":
        val=data_dict.get(product_attr)
        sub_dict=val[0]
        item_list=sub_dict.get(Laptops_attr)
        item=item_list[0]

        for synonym in synonyms[attribute_type]:
            for key in item:
                if(key==synonym):
                    return key 
    return None  # Return None if no matching attribute is found

#folder path
folder_path="../shop-items"
#subfolder
subfolders=["/electrical"]

#subfolders=["/electrical","/furniture","/general-hardware"]

# List all .db files in the folder
for subfolder in subfolders:

    
    path=folder_path+subfolder
    
    json_files = [file for file in os.listdir(path) if file.endswith('.json')]
    
    # Connect to the data_mapping.db database
    connection = sqlite3.connect('data_mapping.db')
    cursor = connection.cursor()

    # Get a list of existing database names in the mapping table
    cursor.execute("SELECT database_name FROM electrical_mapping")
    existing_json_names = [row[0] for row in cursor.fetchall()]

    # Iterate through the .db files
    for json_file in json_files:
        
        json_name = os.path.splitext(json_file)[0]
        
        # Check if the database is not already in the mapping table
        if json_name not in existing_json_names:
            # Find the mapped attributes using synonyms
            product_attr = find_mapped_attribute(json_name, subfolder, synonyms, "products")
            categories_attr = find_mapped_attribute(json_name, subfolder, synonyms, "categories")
            TVs_attr = find_mapped_attribute(json_name, subfolder, synonyms, "TVs")
            Laptops_attr = find_mapped_attribute(json_name, subfolder, synonyms, "Laptops")
            Home_Appliances_attr = find_mapped_attribute(json_name, subfolder, synonyms, "Home_Appliances")
            Smartphones_attr = find_mapped_attribute(json_name, subfolder, synonyms, "Smartphones")
            item_id_attr = find_mapped_attribute(json_name, subfolder, synonyms, "item_id")
            item_type_attr = find_mapped_attribute(json_name, subfolder, synonyms, "item_type")
            item_brand_attr = find_mapped_attribute(json_name, subfolder, synonyms, "item_brand")
            item_price_attr = find_mapped_attribute(json_name, subfolder, synonyms, "item_price")
            item_size_attr = find_mapped_attribute(json_name, subfolder, synonyms, "item_size")
            item_quantity_attr = find_mapped_attribute(json_name, subfolder, synonyms, "item_quantity")
            item_name_attr = find_mapped_attribute(json_name, subfolder, synonyms, "item_name")



            # Add the mapping entry to the mapping table
            
            cursor.execute("INSERT INTO electrical_mapping (database_name, categories, products, TVs, Laptops, Home_Appliances, Smartphones, item_id, item_type, item_brand, item_price, item_size, item_quantity, item_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (json_name, categories_attr, product_attr, TVs_attr, Laptops_attr, Home_Appliances_attr, Smartphones_attr, item_id_attr, item_type_attr, item_brand_attr, item_price_attr, item_size_attr, item_quantity_attr, item_name_attr))
            connection.commit()


    # Check and remove entries in the mapping table that correspond to deleted databases
    for existing_json_name in existing_json_names:
        if f"{existing_json_name}.json" not in json_files:
            cursor.execute("DELETE FROM electrical_mapping WHERE database_name = ?", (existing_json_name,))
            connection.commit()

    # Close the database connection
    connection.close()
