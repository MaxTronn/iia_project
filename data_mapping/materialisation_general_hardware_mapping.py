import json
import os
import sqlite3

# synonym dictionary
synonyms={
    "products": ["products","product","thing","goods"],
    "categories": ["categories","category","division"],
    "sub_categories": ["sub_categories","sub_category"],
    "TVs": ["TVs","tv","TV"],
    "Laptops": ["Laptops","Laptop","Personal_PC"],
    "Home_Appliances": ["Home Appliances","Home Appliance"],
    "Smartphones": ["Smartphones","Smartphone","Mobile phone","mobile"],
    "Tables": ["Tables","Table"],
    "Cabinets": ["Cabinets","cabinet","cabinets"],
    "Beds": ["Beds","beds","bed"],
    "Sofas": ["Sofas","sofa","sofas"],
    "Chairs": ["Chairs","chair","seat","stool"],
    "building_materials": ["building_materials","building items"],
    "safety_equipment": ["safety_equipment","safety","safety_equipments"],
    "electrical_supplies": ["electrical_supplies","electrical_supply","electric supply","electric goods","electrical goods"],
    "tools": ["tools","tool","instrument"],
    "power_tools":["power_tools","power tool"],
    "hand_tools": ["hand_tools"," hand tool"],
    "measuring_tools": ["measuring_tools","scaling tools", "measure tools"],
    "helmets": ["helmets","helmet"],
    "gloves": ["gloves","glove"],
    "tiles": ["tiles","tile","tiling"],
    "paint": ["paint","paints","wall colours"],
    "lumber": ["lumber"],
    "cement": ["cement"],
    "plumbing": ["plumbing","plumbing tools"],
    "interior": ["interior","interiors"],
    "exterior": ["exterior","exteriors"],
    "softwood": ["softwood"],
    "hardwood": ["hardwood"],
    "composite_wood": ["composite_wood"],
    "batteries": ["batteries", "battery"],
    "lighting": ["lighting", "light"],
    "wires": ["wires", "wire", "cable"],
    "item_id":["id", "ID","Identity card"],
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
tools_attr= ""
electrical_supplies_attr= ""
building_materials_attr= ""
safety_equipment_attr= ""
sub_category_attr= ""
hand_tools_attr= ""
measuring_tools_attr= ""
power_tools_attr = ""
helmets_attr = ""
gloves_attr = ""
tiles_attr = ""
paint_attr = ""
lumber_attr = ""
cement_attr = ""
plumbing_attr = ""
interior_attr = ""
exterior_attr = ""
hardwood_attr = ""
softwood_attr = ""
composite_wood_attr = ""
lighting_attr = ""
wires_attr = ""
batteries_attr = ""

item_id_attr = ""
item_brand_attr = ""
item_price_attr = ""
item_size_attr = ""
item_quantity_attr = ""
item_details_attr = ""
item_name_attr = ""

# Function to find the mapped attribute in a local database
def find_mapped_attribute(db_name, subfolder, synonyms, attribute_type):
    path=folder_path+subfolder+"/"+db_name+".json"
    
    with open(path, 'r') as file:
        json_data = file.read()

    data = json.loads(json_data)
    data_dict=data[0]
    
    
    if attribute_type == "products":
        for synonym in synonyms[attribute_type]:
            for key in data_dict:
                if(key==synonym):
                    return key
                
    elif attribute_type in ["categories", "tools", "electrical_supplies", "building_materials", "safety_equipment"]:
        val=data_dict.get(product_attr)
        sub_dict=val[0]
        
        for synonym in synonyms[attribute_type]:
            for key in sub_dict:
                
                if(key==synonym):
                    return key 
                     
    elif attribute_type in ["sub_categories", "power_tools", "hand_tools", "measuring_tools"]:
        val=data_dict.get(product_attr)
        sub_dict=val[0]
        tool_list=sub_dict.get(tools_attr)
        tools=tool_list[0]
        
        for synonym in synonyms[attribute_type]:
            for key in tools:
                
                if(key==synonym):
                    return key 

    
    
    elif attribute_type in ["helmets", "gloves"]:
        val=data_dict.get(product_attr)
        sub_dict=val[0]
        safety_equipments_list=sub_dict.get(safety_equipment_attr)
        safety_equipments=safety_equipments_list[0]
        
        for synonym in synonyms[attribute_type]:
            for key in safety_equipments:
                
                if(key==synonym):
                    return key 
                
    elif attribute_type in ["tiles", "paint", "lumber", "cement", "plumbing"]:
        val=data_dict.get(product_attr)
        sub_dict=val[0]
        
        building_materials_list=sub_dict.get(building_materials_attr)
        

        building_material=building_materials_list[0]
        
        for synonym in synonyms[attribute_type]:
            for key in building_material:
                
                if(key==synonym):
                    return key 
                
    elif attribute_type in ["batteries", "wires", "lighting"]:
        val=data_dict.get(product_attr)
        sub_dict=val[0]
        electrical_supplies_list=sub_dict.get(electrical_supplies_attr)
        electrical_supplies=electrical_supplies_list[0]
        
        for synonym in synonyms[attribute_type]:
            for key in electrical_supplies:
                
                if(key==synonym):
                    return key

    elif attribute_type in ["interior", "exterior"]:
        val=data_dict.get(product_attr)
        sub_dict=val[0]
        building_materials_list=sub_dict.get(building_materials_attr)
        building_materials=building_materials_list[0]
        
        paint_list=building_materials.get(paint_attr)
        paint=paint_list[0]

        for synonym in synonyms[attribute_type]:
            for key in paint:
                
                if(key==synonym):
                    return key

    elif attribute_type in ["composite_wood", "softwood", "hardwood"]:
        val=data_dict.get(product_attr)
        sub_dict=val[0]
        building_materials_list=sub_dict.get(building_materials_attr)
        building_materials=building_materials_list[0]
        
        lumber_list=building_materials.get(lumber_attr)
        lumber=lumber_list[0]

        for synonym in synonyms[attribute_type]:
            for key in lumber:
                
                if(key==synonym):
                    return key
                   
    elif attribute_type in ["item_id", "item_brand", "item_price", "item_size", "item_quantity", "item_name"]:
        val=data_dict.get(product_attr)
        sub_dict=val[0]
        building_materials_list=sub_dict.get(building_materials_attr)
        building_material=building_materials_list[0]
        
        paint_list=building_material.get(paint_attr)
        paint=paint_list[0]

        interior_list=paint.get(interior_attr)
        interior=interior_list[0]

        for synonym in synonyms[attribute_type]:
            for key in interior:
                
                if(key==synonym):
                    return key 
                
    elif attribute_type in ["item_details"]:
        val=data_dict.get(product_attr)
        sub_dict=val[0]
        electrical_supplies_list=sub_dict.get(electrical_supplies_attr)
        electrical_supplies=electrical_supplies_list[0]
        
        lighting_list=electrical_supplies.get(lighting_attr)
        lighting=lighting_list[0]

        for synonym in synonyms[attribute_type]:
            for key in lighting:
                
                if(key==synonym):
                    return key 
    
    return None  # Return None if no matching attribute is found

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
            product_attr = find_mapped_attribute(json_name, subfolder, synonyms, "products")
            categories_attr = find_mapped_attribute(json_name, subfolder, synonyms, "categories")
            tools_attr = find_mapped_attribute(json_name, subfolder, synonyms, "tools")
            sub_category_attr = find_mapped_attribute(json_name, subfolder, synonyms, "sub_categories")
            electrical_supplies_attr= find_mapped_attribute(json_name, subfolder, synonyms,"electrical_supplies")
            building_materials_attr= find_mapped_attribute(json_name, subfolder, synonyms, "building_materials")
            safety_equipment_attr= find_mapped_attribute(json_name, subfolder,synonyms, "safety_equipment")
            hand_tools_attr= find_mapped_attribute(json_name, subfolder,synonyms, "hand_tools")
            measuring_tools_attr= find_mapped_attribute(json_name, subfolder,synonyms, "measuring_tools")
            power_tools_attr = find_mapped_attribute(json_name, subfolder,synonyms, "power_tools")
            helmets_attr = find_mapped_attribute(json_name, subfolder,synonyms, "helmets")
            gloves_attr = find_mapped_attribute(json_name, subfolder,synonyms, "gloves")
            tiles_attr = find_mapped_attribute(json_name, subfolder,synonyms, "tiles")
            paint_attr = find_mapped_attribute(json_name, subfolder,synonyms, "paint")
            lumber_attr = find_mapped_attribute(json_name, subfolder,synonyms, "lumber")
            cement_attr = find_mapped_attribute(json_name, subfolder,synonyms, "cement")
            plumbing_attr = find_mapped_attribute(json_name, subfolder,synonyms, "plumbing")
            interior_attr = find_mapped_attribute(json_name, subfolder,synonyms, "interior")
            exterior_attr = find_mapped_attribute(json_name, subfolder,synonyms, "exterior")
            hardwood_attr = find_mapped_attribute(json_name, subfolder,synonyms, "hardwood")
            softwood_attr = find_mapped_attribute(json_name, subfolder,synonyms, "softwood")
            composite_wood_attr = find_mapped_attribute(json_name, subfolder,synonyms, "composite_wood")
            lighting_attr = find_mapped_attribute(json_name, subfolder,synonyms, "lighting")
            wires_attr = find_mapped_attribute(json_name, subfolder,synonyms, "wires")
            batteries_attr = find_mapped_attribute(json_name, subfolder,synonyms, "batteries")
            item_id_attr = find_mapped_attribute(json_name, subfolder,synonyms, "item_id")
            item_brand_attr = find_mapped_attribute(json_name, subfolder,synonyms, "item_brand")
            item_price_attr = find_mapped_attribute(json_name, subfolder,synonyms, "item_price")
            item_size_attr = find_mapped_attribute(json_name, subfolder,synonyms, "item_size")
            item_quantity_attr = find_mapped_attribute(json_name, subfolder,synonyms, "item_quantity")
            item_details_attr = find_mapped_attribute(json_name, subfolder,synonyms, "item_details")
            item_name_attr = find_mapped_attribute(json_name, subfolder,synonyms, "item_name")
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
