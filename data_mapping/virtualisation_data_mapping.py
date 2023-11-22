import os
import sqlite3


# Path to the folder containing the .db files
folder_path="../LocalServiceProviders"

# synonym dictionary
synonyms={
    "cost": ["cost","charge","charges","amount","payment","pay","service_charge","service_charges"],
    "availability": ["availability","available","isAvailable","free"],
    "work_ex": ["work_experience","work_exp","workExp","work_ex","years","experience"],
    "servicemen_service_id": ["service_id","serviceId","serviceid","idService"],
    "service_service_id": ["id","ID","Id","iD"],
    "service_name" : ["serviceName","service_name","name"]
}

# Function to find the mapped attribute in a local database
def find_mapped_attribute(db_name, synonyms, attribute_type):
    db_path = os.path.join(folder_path, f"{db_name}.db")

    # Connect to the local database
    local_connection = sqlite3.connect(db_path)
    local_cursor = local_connection.cursor()

    if attribute_type in ["cost", "service_service_id","service_name"]:
        # Query the 'service' table for the cost attribute
        for synonym in synonyms[attribute_type]:
            local_cursor.execute(f"PRAGMA table_info(service);")
            table_info = local_cursor.fetchall()
            for col in table_info:
                if synonym in col[1]:
                    return col[1]

    elif attribute_type in ["availability", "work_ex","servicemen_service_id"]:
        # Query the 'service_men' table for availability and work_ex attributes
        for synonym in synonyms[attribute_type]:
            local_cursor.execute(f"PRAGMA table_info(service_men);")
            table_info = local_cursor.fetchall()
            for col in table_info:
                if synonym in col[1]:
                    return col[1]

    local_connection.close()
    return None  # Return None if no matching attribute is found




# List all .db files in the folder
db_files = [file for file in os.listdir(folder_path) if file.endswith('.db')]

# Connect to the data_mapping.db database
connection = sqlite3.connect('data_mapping.db')
cursor = connection.cursor()

# Get a list of existing database names in the mapping table
cursor.execute("SELECT database_name FROM mapping")
existing_db_names = [row[0] for row in cursor.fetchall()]

# Iterate through the .db files
for db_file in db_files:
    db_name = os.path.splitext(db_file)[0]
    
    # Check if the database is not already in the mapping table
    if db_name not in existing_db_names:
        # Find the mapped attributes using synonyms
        cost_attr = find_mapped_attribute(db_name, synonyms, "cost")
        availability_attr = find_mapped_attribute(db_name, synonyms, "availability")
        work_ex_attr = find_mapped_attribute(db_name, synonyms, "work_ex")
        servicemen_service_id_attr = find_mapped_attribute(db_name, synonyms, "servicemen_service_id")
        service_service_id_attr = find_mapped_attribute(db_name, synonyms, "service_service_id")
        service_name_attr = find_mapped_attribute(db_name, synonyms, "service_name")


        # Add the mapping entry to the mapping table
        if cost_attr and availability_attr and  servicemen_service_id_attr and service_service_id_attr and service_name_attr is not None:
            cursor.execute("INSERT INTO mapping (database_name, service_cost, availability, work_ex, servicemen_service_id, service_service_id, service_name) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (db_name, cost_attr, availability_attr, work_ex_attr, servicemen_service_id_attr, service_service_id_attr, service_name_attr))
            connection.commit()

# Check and remove entries in the mapping table that correspond to deleted databases
for existing_db_name in existing_db_names:
    if f"{existing_db_name}.db" not in db_files:
        cursor.execute("DELETE FROM mapping WHERE database_name = ?", (existing_db_name,))
        connection.commit()

# Close the database connection
connection.close()

