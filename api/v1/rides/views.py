from flasgger import swag_from
from flask import jsonify, Blueprint
from flask_restful import reqparse
from .model import RideModel
from ..users.model import users

blue_print_rides = Blueprint('blue_print_rides', __name__)


@swag_from('/api/apidocs/get_rides.yml')
@blue_print_rides.route('/api/v1/rides', methods=['GET'])
def get_all_rides():
    rides = RideModel.get_rides()
    return jsonify({"rides": rides}), 200


@swag_from('/api/apidocs/create_ride.yml')
@blue_print_rides.route('/api/v1/rides/create/<int:user_id>', methods=['POST'])
def _create_ride(user_id):
    parser = reqparse.RequestParser()
    parser.add_argument("date")
    parser.add_argument("time")
    parser.add_argument("source")
    parser.add_argument("destination")
    parser.add_argument("user_id")
    arguments = parser.parse_args()

    for user in users:
        if user.get("id") == user_id:

            ride_instance = RideModel(arguments["date"],
                                      arguments["time"], arguments["source"], arguments["destination"], user_id)
            created_ride = RideModel.create_ride(ride_instance)

            return jsonify({"ride": created_ride}), 200
    return jsonify({"error": "User not found"}), 400


@blue_print_rides.route('/api/v1/rides/update/<int:ride_id>', methods=['PUT'])
def update_ride_offer(ride_id):
    parser = reqparse.RequestParser()
    parser.add_argument("date")
    parser.add_argument("time")
    parser.add_argument("source")
    parser.add_argument("destination")
    arguments = parser.parse_args()

    updated = RideModel.update(ride_id, arguments["date"],
                               arguments["time"], arguments["source"], arguments["destination"])

    return jsonify({"updated ride": updated}), 200


@swag_from('/api/apidocs/get_ride.yml')
@blue_print_rides.route('/api/v1/rides/<int:ride_id>', methods=['GET'])
def get_one_ride(ride_id):
    ride = RideModel.get_ride(ride_id)
    if type(ride) == str:
        return ride, 400
    return jsonify({"ride": ride}), 200


@swag_from('/api/apidocs/delete_ride.yml')
@blue_print_rides.route('/api/v1/rides/delete/<int:ride_id>', methods=['DELETE'])
def delete_one_ride(ride_id):
    remaining_rides = RideModel.delete_ride(ride_id)
    return jsonify({'remaining_rides': remaining_rides}), 200


