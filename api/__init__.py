from flask import Flask
from .v1.rides.views import blue_print_rides
from .v1.requests.ride_requests.views import blue_print_ride_requests
from .v1.notifications.views import blue_print_notifications

app = Flask(__name__)

app.register_blueprint(blue_print_rides)
app.register_blueprint(blue_print_ride_requests)
app.register_blueprint(blue_print_notifications)
