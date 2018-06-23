from flask import Flask, Blueprint, jsonify
from .model import RideRequestModel
from ...notifications.model import NotificationModel
from flask_restful import reqparse

app = Flask(__name__)

blue_print_ride_requests = Blueprint('blue_print_ride_requests', __name__)


@blue_print_ride_requests.route('/api/v1/requests/request_ride', methods=['POST'])
def create_ride_request():
    parser = reqparse.RequestParser()

    parser.add_argument("user_id")
    parser.add_argument("ride_id")

    arguments = parser.parse_args()

    instance = RideRequestModel(arguments["user_id"], arguments["user_id"])
    request = RideRequestModel.create_request(instance)

    return jsonify({"ride_request": request}), 200


@blue_print_ride_requests.route('/api/v1/requests/ride_requests/approve', methods=['POST'])
def approve_ride_request():
    parser = reqparse.RequestParser()
    parser.add_argument("request_id")
    parser.add_argument("user_id")
    parser.add_argument("approval")
    args = parser.parse_args()

    request = RideRequestModel.get_request(args['request_id'])

    if type(request) is str:

        return request, 400

    else:

        request['status'] = args['approval']

        if str(args["approval"]).title() == "Yes":
            message = "Your request has been accepted"
        else:
            message = "Your request has been rejected"

        notification = NotificationModel.create_notification(NotificationModel(args['user_id'], message))

        return jsonify({"notification": notification, "ride_request": request}), 200


@blue_print_ride_requests.route('/api/v1/ride_requests/requests')
def get_ride_requests():
    ride_requests = RideRequestModel.get_requests()
    if type(ride_requests) == str:
        return ride_requests, 400
    else:
        return jsonify({"ride_requests": ride_requests}), 200
