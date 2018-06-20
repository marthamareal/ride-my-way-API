from flask import Flask
from .v1.rides.views import blue_print
app = Flask(__name__)

app.register_blueprint(blue_print)
