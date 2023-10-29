from flask import Flask, jsonify, request
import sqlite3
import json
import math

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/get-services/<service_name>')
def getservices(service_name):
    cost = request.args.get('cost')
    work_ex = request.args.get('work_ex')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    max_dist = request.args.get('max_dist')

    # Convert cost, work_ex, lat, and lon to integers or floats as needed
    if cost is not None:
        cost = int(cost)
    if work_ex is not None:
        work_ex = int(work_ex)
    if lat is not None:
        lat = float(lat)
    if lon is not None:
        lon = float(lon)
    if max_dist is not None:
        max_dist = float(max_dist)
    else:
        max_dist = 15.0

    # Initialize an empty list to store available service providers
    filtered_type_cost_service_providers = []

    # Connect to the Service_provider_global.db
    conn = sqlite3.connect('Service_provider_global/service_providers.db')

    # Fetch database names based on service name and 'general'
    query = 'SELECT database_name FROM service_provers_table WHERE type = ? OR type = ?;'
    cursor = conn.execute(query, (service_name, 'general'))
    dbs = cursor.fetchall()

    print(dbs)

    for db in dbs:
        db_name = db[0][:-3]

        # Connect to the data_mapping database and retrieve columns
        conn = sqlite3.connect('data_mapping/data_mapping.db')
        query = 'SELECT * FROM mapping WHERE database_name = ?;'
        cursor = conn.execute(query, (db_name,))
        cols = cursor.fetchone()

        # Connect to the LocalServiceProviders database for each provider
        conn = sqlite3.connect('LocalServiceProviders/' + db[0])

        # get the service id from the service name
        query = f"SELECT * FROM service WHERE {cols[6]} = ?;"
        cursor = conn.execute(query, (service_name,))
        data = cursor.fetchone()
        if (data == None):
            continue
        print(data)
        service_id = data[0]

        if len(data) == 0:
            continue

        if work_ex is not None and cols[3] is not None:
            print('work_ex is not None', work_ex, db_name)
            query = f"SELECT * FROM service_men WHERE ({cols[2]} = 'Available' OR {cols[2]} = 1 OR {cols[2]} = 'available' OR {cols[2]} = 'yes') AND {cols[4]} = ? AND {cols[3]} >= ?;"
            cursor = conn.execute(query, (service_id, work_ex,))
            data = cursor.fetchall()

        else:
            query = f"SELECT * FROM service_men WHERE ({cols[2]} = 'Available' OR {cols[2]} = 1 OR {cols[2]} = 'available' OR {cols[2]} = 'yes') AND {cols[4]} = ?;"
            cursor = conn.execute(query, (service_id,))
            data = cursor.fetchall()

        if len(data) > 0:
            if cost is not None:
                query = f"SELECT * FROM service WHERE {cols[1]} <= ? AND {cols[6]} = ?;"
                cursor = conn.execute(query, (cost, service_name))
                data = cursor.fetchall()

                if len(data) > 0:
                    filtered_type_cost_service_providers.append({
                        "db": db,
                        "service_cost": data[0][2],
                    })
            else:
                query = f"SELECT * FROM service WHERE {cols[6]} = ?;"
                cursor = conn.execute(query, (service_name))
                data = cursor.fetchall()

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

        if lat is not None and lon is not None:
            # check distance between lat, lon and service provider lat, lon
            # if distance is less than 10km, add to service_providers

            # Check the distance between lat, lon and service provider lat, lon
            provider_lat = float(data[7])
            provider_lon = float(data[8])
            provider_distance = haversine(lat, lon, provider_lat, provider_lon)

            if provider_distance <= max_dist:  # Filter providers within 10km
                service_providers.append({
                    "name": data[2],
                    "phone": data[5],
                    "email": data[4],
                    "lat": provider_lat,
                    "long": provider_lon,
                    "service_cost": entry['service_cost'],
                })
        else:
            service_providers.append({
                "name": data[2],
                "phone": data[5],
                "email": data[4],
                "lat": data[7],
                "long": data[8],
                "service_cost": entry['service_cost'],
            })

    return jsonify(service_providers)


def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    radius = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat/2)**2 + math.cos(lat1) * \
        math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = radius * c

    print('distance is ', distance)

    return distance


if __name__ == '__main__':
    app.run()
