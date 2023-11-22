import virtualisation_data_mapping as vdm
from flask import Flask, jsonify, request
import sqlite3
import os


app = Flask(__name__)

from flask_cors import CORS
CORS(app)


def map_schema():
    synonyms = vdm.synonyms

    # List all .db files in the folder
    db_files = [file for file in os.listdir(
        vdm.folder_path) if file.endswith('.db')]

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
            cost_attr = vdm.find_mapped_attribute(db_name, synonyms, "cost")
            availability_attr = vdm.find_mapped_attribute(
                db_name, synonyms, "availability")
            work_ex_attr = vdm.find_mapped_attribute(
                db_name, synonyms, "work_ex")
            servicemen_service_id_attr = vdm.find_mapped_attribute(
                db_name, synonyms, "servicemen_service_id")
            service_service_id_attr = vdm.find_mapped_attribute(
                db_name, synonyms, "service_service_id")
            service_name_attr = vdm.find_mapped_attribute(
                db_name, synonyms, "service_name")

            # Add the mapping entry to the mapping table
            if cost_attr and availability_attr and servicemen_service_id_attr and service_service_id_attr and service_name_attr is not None:
                cursor.execute("INSERT INTO mapping (database_name, service_cost, availability, work_ex, servicemen_service_id, service_service_id, service_name) VALUES (?, ?, ?, ?, ?, ?, ?)",
                               (db_name, cost_attr, availability_attr, work_ex_attr, servicemen_service_id_attr, service_service_id_attr, service_name_attr))
                connection.commit()

    # Check and remove entries in the mapping table that correspond to deleted databases
    for existing_db_name in existing_db_names:
        if f"{existing_db_name}.db" not in db_files:
            cursor.execute(
                "DELETE FROM mapping WHERE database_name = ?", (existing_db_name,))
            connection.commit()

    # Close the database connection
    connection.close()

    return "Schema mapped successfully"


def delete_from_global_db():
    conn = sqlite3.connect('../Service_provider_global/service_providers.db')
    query = "SELECT database_name FROM Service_provers_table"
    cursor = conn.cursor()
    cursor.execute(query)
    db_names = cursor.fetchall()

    db_files = [file for file in os.listdir(
        vdm.folder_path) if file.endswith('.db')]

    for db_name in db_names:
        if f"{db_name[0]}" not in db_files:
            cursor.execute(
                "DELETE FROM Service_provers_table WHERE database_name = ?", (db_name[0],))
            conn.commit()


@app.route('/remove-service-db/<db_name>')
def remove_db(db_name):
    # remove the db file from the folder
    os.remove(f"{vdm.folder_path}/{db_name}")
    # remove the db from the mapping table
    map_schema()
    # remove the db from the global db
    delete_from_global_db()

    return "removed db successfully"


if __name__ == '__main__':
    app.run(debug=True)
