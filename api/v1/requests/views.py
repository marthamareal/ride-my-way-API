from flask import Flask, Blueprint, jsonify
from .requestModel import RequestModel, requests
from ..notifications.notificationsModel import NotificationAPI
from flask_restful import reqparse

app = Flask(__name__)

blue_print_requests = Blueprint('blue_print_requests', __name__)


@blue_print_requests.route('/api/v1/requests', methods=['POST'])
def request_ride():
    parser = reqparse.RequestParser()

    parser.add_argument("user_id")
    parser.add_argument("ride_id")

    arguments = parser.parse_args()

    instance = RequestModel(arguments["user_id"], arguments["user_id"])
    request = RequestModel.create_request(instance)

    return jsonify({"request": request}), 200


@blue_print_requests.route('/api/v1/request/approve', methods=['POST'])
def approve_request():
    parser = reqparse.RequestParser()
    parser.add_argument("request_id")
    parser.add_argument("user_id")
    parser.add_argument("approval")
    args = parser.parse_args()

    # print(args)
    request = RequestModel.get_request(args['request_id'])

    if args["approval"]:
        message = "Your request has been accepted"
    else:
        message = "Your request has been rejected"

    notification = NotificationAPI.create_notification(NotificationAPI(args['user_id'], message))

    return jsonify({"notification": notification}, {"request": request}), "Request approval updated"
