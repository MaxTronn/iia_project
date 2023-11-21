from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# SQLite database file
DATABASE = "BookingsAndFeedback/BookingsAndFeedback.db"

# Function to establish a database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn



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

    cursor.execute('INSERT INTO booking (b_id, user_id, service_provider_id, status) VALUES (?, ?, ?, ?)',
                   (new_booking_id, data['user_id'], data['service_provider_id'], 'pending'))

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
        return jsonify([dict(booking) for booking in pending_bookings])
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
        return jsonify(dict(booking_details))
    else:
        return jsonify({'error': 'Booking details not found for the given booking ID'}), 404

if __name__ == '__main__':
    app.run(debug=True)
