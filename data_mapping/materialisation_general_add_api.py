
import materialisation_general_hardware_mapping as mem
from flask import Flask, jsonify, request
import sqlite3
import os


app = Flask(__name__)

def map_schema():

    synonyms= mem.synonyms
        #folder path
        #folder path
    folder_path="../shop-items"
    #subfolder
    subfolders=["/general-hardware"]

    #subfolders=["/electrical","/furniture","/general-hardware"]

    # List all .db files in the folder
    for subfolder in subfolders:

        
        path=folder_path+subfolder
        
        json_files = [file for file in os.listdir(path) if file.endswith('.json')]
        
        # Connect to the data_mapping.db database
        connection = sqlite3.connect('data_mapping.db')
        cursor = connection.cursor()

        # Get a list of existing database names in the mapping table
        cursor.execute("SELECT database_name FROM general_hardware_mapping")
        existing_json_names = [row[0] for row in cursor.fetchall()]

        # Iterate through the .db files
        for json_file in json_files:
            
            json_name = os.path.splitext(json_file)[0]
            
            # Check if the database is not already in the mapping table
            if json_name not in existing_json_names:
                # Find the mapped attributes using synonyms
                product_attr = mem.find_mapped_attribute(json_name, subfolder, synonyms, "products")
                categories_attr = mem.find_mapped_attribute(json_name, subfolder, synonyms, "categories")
                tools_attr = mem.find_mapped_attribute(json_name, subfolder, synonyms, "tools")
                sub_category_attr = mem.find_mapped_attribute(json_name, subfolder, synonyms, "sub_categories")
                electrical_supplies_attr= mem.find_mapped_attribute(json_name, subfolder, synonyms,"electrical_supplies")
                building_materials_attr= mem.find_mapped_attribute(json_name, subfolder, synonyms, "building_materials")
                safety_equipment_attr= mem.find_mapped_attribute(json_name, subfolder,synonyms, "safety_equipment")
                hand_tools_attr= mem.find_mapped_attribute(json_name, subfolder,synonyms, "hand_tools")
                measuring_tools_attr= mem.find_mapped_attribute(json_name, subfolder,synonyms, "measuring_tools")
                power_tools_attr =mem.find_mapped_attribute(json_name, subfolder,synonyms, "power_tools")
                helmets_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "helmets")
                gloves_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "gloves")
                tiles_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "tiles")
                paint_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "paint")
                lumber_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "lumber")
                cement_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "cement")
                plumbing_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "plumbing")
                interior_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "interior")
                exterior_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "exterior")
                hardwood_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "hardwood")
                softwood_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "softwood")
                composite_wood_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "composite_wood")
                lighting_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "lighting")
                wires_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "wires")
                batteries_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "batteries")
                item_id_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "item_id")
                item_brand_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "item_brand")
                item_price_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "item_price")
                item_size_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "item_size")
                item_quantity_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "item_quantity")
                item_details_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "item_details")
                item_name_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "item_name")
                # Add the mapping entry to the mapping table
                
                cursor.execute("INSERT INTO general_hardware_mapping (database_name, products, categories, sub_categories, tools, electrical_supplies, building_materials, safety_equipment, hand_tools, measuring_tools, power_tools, helmets, gloves, tiles, paint, lumber, cement, plumbing, interior, exterior, hardwood, softwood, composite_wood, lighting, wires, batteries, item_id, item_brand, item_price, item_size, item_quantity, item_details, item_name ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (json_name, product_attr, categories_attr, sub_category_attr, tools_attr, electrical_supplies_attr, building_materials_attr, safety_equipment_attr, hand_tools_attr, measuring_tools_attr, power_tools_attr, helmets_attr, gloves_attr, tiles_attr, paint_attr, lumber_attr, cement_attr, plumbing_attr, interior_attr, exterior_attr, hardwood_attr, softwood_attr, composite_wood_attr, lighting_attr, wires_attr, batteries_attr, item_id_attr, item_brand_attr, item_price_attr, item_size_attr, item_quantity_attr, item_details_attr, item_name_attr))
                connection.commit()


    # Check and remove entries in the mapping table that correspond to deleted databases
        for existing_json_name in existing_json_names:
            if f"{existing_json_name}.json" not in json_files:
                cursor.execute("DELETE FROM general_hardware_mapping WHERE database_name = ?", (existing_json_name,))
                connection.commit()

        # Close the database connection
        connection.close()

    
    return "Schema mapped successfully"


@app.route('/add-general-db', methods=['POST'])
def upload_file():

    file = request.files['file']
    id = request.form['id']
    file.save(os.path.join(mem.folder_path+"/general-hardware", file.filename))

    conn = sqlite3.connect('../shop-details/shopkeeper-details.db')
    # change db name where id = id
    query = "UPDATE shopkeepers SET db_name = ? WHERE id = ?"
    conn.execute(query, (file.filename, id))

    conn.commit()
    conn.close()

    map_schema()
    

    return 'File uploaded successfully'


if __name__ == '__main__':
    app.run()