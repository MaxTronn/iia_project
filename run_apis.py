from flask import Flask
import login_signup_api
import materialization_api
import virtualization_api
import booking_feedback_api
from threading import Thread

app = Flask(__name__)


def run_flask_app(app, port):
    app.run(port=port)

if __name__ == '__main__':


    # Specify the ports for each API
    login_signup_port = 5001
    materialization_port = 5002
    virtualization_port = 5003
    booking_feedback_port = 5004

    login_signup_app = login_signup_api.app
    materialization_app = materialization_api.app
    virtualization_app = virtualization_api.app
    booking_feedback_app = booking_feedback_api.app


    # Start each Flask app in a separate thread
    login_signup_thread = Thread(target=run_flask_app, args=(login_signup_app, login_signup_port))
    materialization_thread = Thread(target=run_flask_app, args=(materialization_app, materialization_port))
    virtualization_thread = Thread(target=run_flask_app, args=(virtualization_app, virtualization_port))
    booking_feedback_thread = Thread(target=run_flask_app, args=(booking_feedback_app, booking_feedback_port))

    # Start the threads
    login_signup_thread.start()
    materialization_thread.start()
    virtualization_thread.start()
    booking_feedback_thread.start()

    # Wait for all threads to finish
    login_signup_thread.join()
    materialization_thread.join()
    virtualization_thread.join()
    booking_feedback_thread.join()
