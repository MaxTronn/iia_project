from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
from flask_cors import CORS
CORS(app)


# SQLite database file
USER_DATABASE = "data/users.db"
SERVICE_PROVIDER_DATABASE = "Service_provider_global/service_providers.db"



# Functions to establish a database connection
def get_user_db_connection():
    conn = sqlite3.connect(USER_DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_service_provider_db_connection():
    conn = sqlite3.connect(SERVICE_PROVIDER_DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# json payload for user_login
# {
#   "email": "aaditya@gmail.com",
#   "password": "FeUaoyMi"
# }


# Endpoint for user user_login
@app.route('/user_login', methods=['POST'])
def user_login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    conn = get_user_db_connection()
    cursor = conn.cursor()

    # Check if the user exists with the given email and password
    cursor.execute('SELECT * FROM users_table WHERE email=? AND password=?', (email, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        user = dict(user)
        user.update({'result':True})
        return jsonify(user)
    else:
        return jsonify({'result':False})




# Send a json payload for user_signup
# {
#   "name": "John Doe",
#   "email": "john.doe@example.com",
#   "phone_number": "1234567890",
#   "password": "securepassword",
#   "latitude": 37.7749,
#   "longitude": -122.4194
# }


# Endpoint for user user_signup
@app.route('/user_signup', methods=['POST'])
def user_signup():
    data = request.json

    # Fetch the highest ID from the users_table
    conn = get_user_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(id) FROM users_table')
    max_id = cursor.fetchone()[0]
    conn.close()

    # Increment the highest ID by 1
    new_id = max_id + 1 if max_id is not None else 1

    # Insert new user into the database with the calculated ID
    conn = get_user_db_connection()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO users_table (id, name, email, phone_number, password, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?)',
                   (new_id, data['name'], data['email'], data['phone_number'], data['password'], data['latitude'], data['longitude']))

    conn.commit()
    conn.close()

    return jsonify({'result': 'User registered successfully'})




# Endpoint to get user details by ID
@app.route('/get_user_details/<int:user_id>', methods=['GET'])
def get_user_details(user_id):
    conn = get_user_db_connection()
    cursor = conn.cursor()

    # Fetch user details by ID
    cursor.execute('SELECT name, email, phone_number, latitude, longitude FROM users_table WHERE id=?', (user_id,))
    user_details = cursor.fetchone()

    conn.close()

    if user_details:
        return jsonify(dict(user_details))
    else:
        return jsonify({'error': 'User not found'}), 404





# json payload for service provider login
# {
#   "email": "user@example.com"
# }



# Endpoint for service provider login
@app.route('/service_provider_login', methods=['POST'])
def service_provider_login():
    data = request.json
    email = data.get('email')

    conn = get_service_provider_db_connection()
    cursor = conn.cursor()

    # Check if the shopkeeper exists with the given email and password
    cursor.execute('SELECT * FROM service_provers_table WHERE email=? ', (email, ))
    shopkeeper = cursor.fetchone()

    conn.close()

    # Return True if the shopkeeper exists, else return False
    return jsonify({'result': True if shopkeeper else False})



# Endpoint for independent service provider login
@app.route('/idpt_service_provider_login', methods=['POST'])
def idpt_service_provider_login():
    data = request.json
    email = data.get('email')


    conn = get_service_provider_db_connection()
    cursor = conn.cursor()

    # Check if the shopkeeper exists with the given email and password
    cursor.execute('SELECT * FROM service_provers_table WHERE email=? '
                   'AND database_name="individual"', (email, ))
    shopkeeper = cursor.fetchone()
    shopkeeper = dict(shopkeeper)
    
    conn.close()

    if shopkeeper:
        shopkeeper.update({'result':True})
        return jsonify(dict(shopkeeper))
    else:
        return jsonify({'result':False})



# json payload for service provider signup
# {
#   "store_name": "My Store",
#   "email": "store@example.com",
#   "phone": "1234567890",
#   "password": "securepassword",
#   "latitude": 37.7749,
#   "longitude": -122.4194,
#   "type": "Retail",
#   "database_name": "my_store_db"
# }

# Endpoint for service provider signup
@app.route('/service_provider_signup', methods=['POST'])
def service_provider_signup():
    data = request.json

    # Fetch the highest ID from the service_providers_table
    conn = get_service_provider_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(id) FROM service_provers_table')
    max_id = cursor.fetchone()[0]
    conn.close()

    # Increment the highest ID by 1 (or set it to 1 if there are no existing records)
    new_id = max_id + 1 if max_id is not None else 1

    # Insert new service provider into the database with the calculated ID
    conn = get_service_provider_db_connection()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO service_provers_table (id, store_name, email, phone, password, latitude, longitude, type, database_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   (new_id, data['store_name'], data['email'], data['phone'], data['password'], data['latitude'], data['longitude'], data['type'], data['database_name']))

    conn.commit()
    conn.close()

    return jsonify({'result': 'service provider registered successfully'})



# Endpoint to get service provider details by ID
@app.route('/get_service_provider_details/<int:service_provider_id>', methods=['GET'])
def get_service_provider_details(service_provider_id):
    conn = get_service_provider_db_connection()
    cursor = conn.cursor()

    # Fetch service provider details by ID
    cursor.execute('SELECT id, store_name, email, phone, latitude, longitude, type, database_name FROM service_provers_table WHERE id=?', (service_provider_id,))
    service_provider_details = cursor.fetchone()

    conn.close()

    if service_provider_details:
        return jsonify(dict(service_provider_details))
    else:
        return jsonify({'error': 'Shopkeeper not found'}), 404



if __name__ == '__main__':
    app.run(debug=True, port=5006)
