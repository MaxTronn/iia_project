from flask import Flask, jsonify, request
import sqlite3
import json

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/get-services/<service_id>/<cost>/<work_ex>')
def getservices(service_id, cost, work_ex):
    # get data/service_type_global.json
    service_name = ''
    service_id = int(service_id)
    cost = int(cost)
    work_ex = int(work_ex)

    with open('data/service_type_global.json') as f:
        data = json.load(f)

    for entry in data:
        if entry['id'] == service_id:
            service_name = entry['service_type']
            break

    # Initialize an empty list to store available service providers
    filtered_type_cost_service_providers = []

    # Connect to the Service_provider_global.db
    conn = sqlite3.connect('Service_provider_global/service_providers.db')

    # Fetch database names based on service name and 'general'
    query = 'SELECT database_name FROM service_provers_table WHERE type = ? OR type = ?;'
    cursor = conn.execute(query, (service_name, 'general'))
    dbs = cursor.fetchall()

    for db in dbs:
        db_name = db[0][:-3]
        print(db_name)

        # Connect to the data_mapping database and retrieve columns
        conn = sqlite3.connect('data_mapping/data_mapping.db')
        query = 'SELECT * FROM mapping WHERE database_name = ?;'
        cursor = conn.execute(query, (db_name,))
        cols = cursor.fetchone()

        # Connect to the LocalServiceProviders database for each provider
        conn = sqlite3.connect('LocalServiceProviders/' + db[0])

        # Check availability
        query = f"SELECT * FROM service_men WHERE {cols[2]} = 'Available' OR {cols[2]} = 1 AND {cols[4]} = ?;"
        cursor = conn.execute(query, (service_id,))
        data = cursor.fetchall()

        if len(data) > 0:
            # Check cost
            query = f"SELECT * FROM service WHERE cost <= ? AND name = ?;"
            cursor = conn.execute(query, (cost, service_name))
            data = cursor.fetchall()

            print(data)

            if len(data) > 0:
                filtered_type_cost_service_providers.append({
                    "db": db,
                    "service_cost": data[0][2],
                })

    service_providers = []

    conn = sqlite3.connect('Service_provider_global/service_providers.db')
    for entry in filtered_type_cost_service_providers:
        print(entry)
        query = 'SELECT * FROM service_provers_table WHERE database_name = ?;'
        cursor = conn.execute(query, (entry['db'][0],))
        data = cursor.fetchone()
        service_providers.append({
            "name": data[2],
            "phone": data[5],
            "email": data[4],
            "lat": data[7],
            "long": data[8],
            "service_cost": entry['service_cost'],
        })

    return jsonify(service_providers)


if __name__ == '__main__':
    app.run()
