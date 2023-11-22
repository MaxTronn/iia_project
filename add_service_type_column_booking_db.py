import random

from flask import Flask, request, jsonify
import sqlite3

# SQLite database file
DATABASE = "BookingsAndFeedback/BookingsAndFeedback.db"
USER_DATABASE = "data/users.db"
SERVICE_PROVIDER_DATABASE = "Service_provider_global/service_providers.db"

# Function to establish a database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn



def add_service_name_column():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Add a new column "status" to the "booking" table
    cursor.execute('ALTER TABLE booking DROP COLUMN service_name')
    cursor.execute('ALTER TABLE booking ADD COLUMN service_name TEXT')

    # Fetch all rows from the "booking" table
    cursor.execute('SELECT * FROM booking')
    bookings = cursor.fetchall()

    # Update each row with a random status
    for booking in bookings:
        service_name = random.choice(["welder", "carpenter", "mechanic", "housekeeper", "barber", \
                                    "electrician", "plumber", "painter",  "tailor", "cook","makeupartist"])
        booking_id = booking['b_id']

        # Update the status for the current booking_id
        cursor.execute('UPDATE booking SET service_name=? WHERE b_id=?', (service_name, booking_id))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    add_service_name_column()