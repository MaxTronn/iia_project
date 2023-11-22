from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

from flask_cors import CORS
CORS(app)

# SQLite database file
DATABASE = "BookingsAndFeedback/BookingsAndFeedback.db"
USER_DATABASE = "data/users.db"
SERVICE_PROVIDER_DATABASE = "Service_provider_global/service_providers.db"

# Function to establish a database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Functions to establish a database connection to user database
def get_user_db_connection():
    conn = sqlite3.connect(USER_DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_service_provider_db_connection():
    conn = sqlite3.connect(SERVICE_PROVIDER_DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# get user details given a user id
def get_user_details(user_id):
    conn = get_user_db_connection()
    cursor = conn.cursor()

    # Fetch user details by ID
    cursor.execute('SELECT name, email, phone_number, latitude, longitude FROM users_table WHERE id=?', (user_id,))
    user_details = cursor.fetchone()

    conn.close()

    if user_details:
        return dict(user_details)
    else:
        print("Error in get_user_details for user_id = ", user_id)
        return {'error': 'User not found'}


def merge_user_details(bookings_list):
    for booking in bookings_list:
        user_id = booking['user_id']
        if user_id is not None:
            user_details = get_user_details(user_id)

            # Merge user details into the booking dictionary
            if user_details and "error" not in user_details:
                booking.update(user_details)
            else:
                print("error while fetching user_id = ", user_id)

    return bookings_list



# Endpoint to fetch feedback by booking ID
@app.route('/fetch_feedback/<int:booking_id>', methods=['GET'])
def fetch_feedback(booking_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    feedback_details = {}

    # Fetch rating and comment from feedback table
    cursor.execute('SELECT comment FROM feedback WHERE booking_id=?', (booking_id,))
    comment = cursor.fetchone()
    if not comment :
        comment = {"comment" : None}

    feedback_details.update(comment)

    cursor.execute('SELECT rating FROM booking WHERE b_id=?', (booking_id,))
    rating = cursor.fetchone()
    if not rating :
        rating = {"rating" : None}
    feedback_details.update(dict(rating))

    conn.close()

    return jsonify(feedback_details)

# JSON PAYLOAD for FETCHING SERVICE PROVIDER ID
# {
#   "email": "delcoat1@comsenz.com",
#   "password": "eU9(<cZ=vL0w""q0"
# }


# Given email, password fetch service_provider_id
@app.route('/fetch_service_provider_id', methods=['POST'])
def fetch_service_provider_id():
    data = request.json
    email = data.get('email')

    conn = get_service_provider_db_connection()
    cursor = conn.cursor()

    # Check if the shopkeeper exists with the given email and password
    cursor.execute('SELECT id FROM service_provers_table WHERE email=?', (email,))
    shopkeeper = cursor.fetchone()

    conn.close()

    if shopkeeper:
        return jsonify(dict(shopkeeper))
    else:
        return jsonify({"error" : "error in fetch_service_provider_id function"})



# JSON PAYLOAD for STORING FEEDBACK
# {
#   "booking_id": 1,
#   "comment": "Great service!",
#   "rating": 5
# }

# Endpoint to store feedback
@app.route('/store_feedback', methods=['POST'])
def store_feedback():
    data = request.json

    # Fetch the highest feedback ID from the feedback table
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(feedback_id) FROM feedback')
    max_feedback_id = cursor.fetchone()[0]
    conn.close()

    # Increment the highest feedback ID by 1 (or set it to 1 if there are no existing records)
    new_feedback_id = max_feedback_id + 1 if max_feedback_id is not None else 1

    # Insert new feedback into the feedback table with the calculated feedback ID
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO feedback (feedback_id, booking_id, comment) VALUES (?, ?, ?)',
                   (new_feedback_id, data['booking_id'], data['comment']))

    # Update rating for the corresponding booking ID in the booking table
    cursor.execute('UPDATE booking SET rating=? WHERE b_id=?', (data['rating'], data['booking_id']))
    cursor.execute('UPDATE booking SET feedback_id=? WHERE b_id=?', (new_feedback_id, data['booking_id']))

    conn.commit()
    conn.close()

    return jsonify({'result': 'Feedback stored successfully'})



# JSON PAYLOAD FOR PENDING BOOKING
# {
#   "user_id": 123,
#   "service_provider_id": 456,
#   "service_name": "carpenter"
# }


# Endpoint for pending booking
@app.route('/pending_booking', methods=['POST'])
def pending_booking():
    data = request.json

    # Fetch the highest booking ID from the booking table
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT MAX(b_id) FROM booking')
    max_booking_id = cursor.fetchone()[0]
    conn.close()

    # Increment the highest booking ID by 1 (or set it to 1 if there are no existing records)
    new_booking_id = max_booking_id + 1 if max_booking_id is not None else 1

    # Insert new pending booking into the booking table with the calculated booking ID and status "pending"
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO booking (b_id, user_id, service_provider_id, service_name ,status) VALUES (?, ?, ?, ?, ?)',
                   (new_booking_id, data['user_id'], data['service_provider_id'], data['service_name'],'pending'))

    conn.commit()
    conn.close()

    return jsonify({'result': 'Pending booking stored successfully'})

# Endpoint to accept a booking
@app.route('/accept_booking/<int:booking_id>', methods=['GET'])
def accept_booking(booking_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Set status = "accepted" for the given booking_id
    cursor.execute('UPDATE booking SET status=? WHERE b_id=?', ('accepted', booking_id))

    conn.commit()
    conn.close()

    return jsonify({'result': 'Booking accepted successfully'})

# Endpoint to reject a booking
@app.route('/reject_booking/<int:booking_id>', methods=['GET'])
def reject_booking(booking_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Set status = "rejected" for the given booking_id
    cursor.execute('UPDATE booking SET status=? WHERE b_id=?', ('rejected', booking_id))

    conn.commit()
    conn.close()

    return jsonify({'result': 'Booking rejected successfully'})

# Endpoint to fetch pending bookings for a service provider
@app.route('/fetch_pending_booking/<int:service_provider_id>', methods=['GET'])
def fetch_pending_booking(service_provider_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch all rows with the given service_provider_id and status = "pending"
    cursor.execute('SELECT * FROM booking WHERE service_provider_id=? AND status=?',
                   (service_provider_id, 'pending'))
    pending_bookings = cursor.fetchall()

    conn.close()
    if pending_bookings:
        pending_bookings = [dict(booking) for booking in pending_bookings]
        pending_bookings = merge_user_details(pending_bookings)
        return jsonify(pending_bookings)
    else:
        return jsonify({'result': 'No pending bookings found for the given service provider'}), 404


# Endpoint to fetch booking details by booking ID
@app.route('/fetch_booking_details/<int:booking_id>', methods=['GET'])
def fetch_booking_details(booking_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch all details related to the booking ID from the booking table
    cursor.execute('SELECT * FROM booking WHERE b_id=?', (booking_id,))
    booking_details = cursor.fetchone()
    conn.close()
    if booking_details:
        booking_details =  [dict(booking_details)]
        booking_details = merge_user_details(booking_details)
        return jsonify(booking_details)
    else:
        return jsonify({'error': 'Booking details not found for the given booking ID'}), 404


# Endpoint to fetch all bookings of a service_provider
@app.route('/fetch_all_bookings/<int:service_provider_id>', methods=['GET'])
def fetch_all_bookings(service_provider_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch all details related to the booking ID from the booking table
    cursor.execute('SELECT * FROM booking WHERE service_provider_id=?'
                   'ORDER BY b_id DESC', (service_provider_id,))
    booking_details = cursor.fetchall()

    conn.close()

    if booking_details:
        booking_details = [dict(booking) for booking in booking_details]
        booking_details = merge_user_details(booking_details)
        return jsonify(booking_details)
    else:
        return jsonify({'error': 'Booking details not found for the given service provider ID'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
