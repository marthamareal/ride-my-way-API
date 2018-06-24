from flask import Flask, redirect
from .v1.rides.views import blue_print_rides
from .v1.requests.ride_requests.views import blue_print_ride_requests
from .v1.notifications.views import blue_print_notifications
from flasgger import Swagger

app = Flask(__name__)

# creating my swagger ui info

template = {
    "swagger": 2.0,
    "version": "v1",
    "info": {
        "title": "RIDE MY WAY API",
        "description": "This is a web api built in flask. and you can test its endpoints from here. Enjoy my API"
    }
}

Swagger(app, template=template)

@app.route('/')
def index():

    return redirect('/apidocs/')


app.register_blueprint(blue_print_rides)
app.register_blueprint(blue_print_ride_requests)
app.register_blueprint(blue_print_notifications)
