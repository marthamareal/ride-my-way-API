from flask import Blueprint, jsonify
from flask_restful import reqparse
from api.v1.requests.ride_requests.model import ride_requests
from .model import RideRequestModel
from ...rides.model import rides
from ...users.model import users
from ...notifications.model import NotificationModel

blue_print_ride_requests = Blueprint('blue_print_ride_requests', __name__)


@blue_print_ride_requests.route('/api/v1/requests/request_ride/<int:ride_id>/<int:user_id>', methods=['POST'])
def create_ride_request(user_id, ride_id):
    instance = RideRequestModel(user_id, ride_id, "pending")
    for user in users:
        if user.get("id") == instance.user_id:
            for ride in rides:
                if ride.get("id") == instance.ride_id:
                    request = RideRequestModel.create_request(instance)
                    ride["requests_no"] = ride.get("requests_no") + 1
                    return jsonify({"ride_request": request}), 200
    return jsonify({"error": "User or ride not found"})


@blue_print_ride_requests.route('/api/v1/requests/approve/<int:request_id>/<int:user_id>', methods=['POST'])
def approve_ride_request(user_id, request_id):
    parser = reqparse.RequestParser()
    parser.add_argument("approval")
    args = parser.parse_args()
    for req in ride_requests:
        if req.get("id") == request_id:
            for user in users:
                if user.get("id") == user_id:
                    for ride in rides:
                        if ride["user_id"] == user_id:
                            if args["approval"].title() == "Yes":
                                req["status"] = "accepted"
                                message = "Your request has been accepted"
                            else:
                                req["status"] = "rejected"
                                message = "Your request has been rejected"

                            notification = NotificationModel.create_notification(NotificationModel
                                                                                 (req.get("user_id"), message))
                            return jsonify({"approved_request": req, "notification": notification}), 200
                        else:
                            return jsonify({"message": "You can not approve this request"})
    return jsonify({"error": "User or request not found"}), 400


@blue_print_ride_requests.route('/api/v1/ride_requests/requests/<int:ride_id>')
def get_ride_requests(ride_id):
    requests = RideRequestModel.get_requests(ride_id)
    return jsonify({"ride_requests": requests}), 200


@blue_print_ride_requests.route('/api/v1/rides/ride_requests/delete/<int:request_id>', methods=['DELETE'])
def delete_ride_request(request_id):
    remaining_requests = RideRequestModel.delete_request(request_id)
    return jsonify({'remaining_requests': remaining_requests}), 200
