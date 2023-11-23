
import materialisation_furniture_mapping as mem
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
    subfolders=["/furniture"]

    #subfolders=["/electrical","/furniture","/general-hardware"]

    # List all .db files in the folder
    for subfolder in subfolders:

        
        path=folder_path+subfolder
        
        json_files = [file for file in os.listdir(path) if file.endswith('.json')]
        
        # Connect to the data_mapping.db database
        connection = sqlite3.connect('data_mapping.db')
        cursor = connection.cursor()

        # Get a list of existing database names in the mapping table
        cursor.execute("SELECT database_name FROM furniture_mapping")
        existing_json_names = [row[0] for row in cursor.fetchall()]

        # Iterate through the .db files
        for json_file in json_files:
            
            json_name = os.path.splitext(json_file)[0]
            
            # Check if the database is not already in the mapping table
            if json_name not in existing_json_names:
                # Find the mapped attributes using synonyms
                product_attr = mem.find_mapped_attribute(json_name, subfolder, synonyms, "products")
                mem.product_attr = product_attr
                categories_attr = mem.find_mapped_attribute(json_name, subfolder, synonyms, "categories")
                mem.categories_attr = categories_attr
                Tables_attr = mem.find_mapped_attribute(json_name, subfolder, synonyms, "Tables")
                mem.Tables_attr=Tables_attr
                Cabinets_attr = mem.find_mapped_attribute(json_name, subfolder, synonyms, "Cabinets")
                mem.Cabinets_attr=Cabinets_attr
                Beds_attr = mem.find_mapped_attribute(json_name, subfolder, synonyms, "Beds")
                mem.Beds_attr=Beds_attr
                Sofas_attr = mem.find_mapped_attribute(json_name, subfolder, synonyms, "Sofas")
                mem.Sofas_attr=Sofas_attr
                #print(Sofas_attr)
                Chairs_attr = mem.find_mapped_attribute(json_name, subfolder, synonyms, "Chairs")
                mem.Chairs_attr=Chairs_attr
                #print(Chairs_attr)
                item_id_attr = mem.find_mapped_attribute(json_name, subfolder, synonyms, "item_id")
                mem.item_id_attr=item_id_attr
                item_type_attr = mem.find_mapped_attribute(json_name, subfolder, synonyms, "item_type")
                mem.item_type_attr=item_type_attr
                item_brand_attr = mem.find_mapped_attribute(json_name, subfolder, synonyms, "item_brand")
                mem.item_brand_attr=item_brand_attr
                item_price_attr = mem.find_mapped_attribute(json_name, subfolder, synonyms, "item_price")
                mem.item_price_attr=item_price_attr
                item_size_attr = mem.find_mapped_attribute(json_name, subfolder, synonyms, "item_size")
                mem.item_size_attr=item_size_attr
                #print(item_size_attr)
                item_quantity_attr = mem.find_mapped_attribute(json_name, subfolder, synonyms, "item_quantity")
                mem.item_quantity_attr=item_quantity_attr
                item_shape_attr = mem.find_mapped_attribute(json_name, subfolder,synonyms, "item_shape")
                mem.item_shape_attr=item_shape_attr

                # Add the mapping entry to the mapping table
                
                cursor.execute("INSERT INTO furniture_mapping (database_name, categories, products, Tables, Cabinets, Beds, Sofas, Chairs, item_id, item_type, item_brand, item_price, item_size, item_quantity, item_shape) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (json_name, categories_attr, product_attr, Tables_attr, Cabinets_attr, Beds_attr, Sofas_attr, Chairs_attr, item_id_attr, item_type_attr, item_brand_attr, item_price_attr, item_size_attr, item_quantity_attr, item_shape_attr))
                connection.commit()


        # Check and remove entries in the mapping table that correspond to deleted databases
        for existing_json_name in existing_json_names:
            if f"{existing_json_name}.json" not in json_files:
                cursor.execute("DELETE FROM furniture_mapping WHERE database_name = ?", (existing_json_name,))
                connection.commit()

    
    return "Schema mapped successfully"


@app.route('/add-furniture-db', methods=['POST'])
def upload_file():

    file = request.files['file']
    id = request.form['id']
    file.save(os.path.join(mem.folder_path+"/furniture", file.filename))

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