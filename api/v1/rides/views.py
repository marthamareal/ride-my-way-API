from flasgger import swag_from
from flask import jsonify, Blueprint
from flask_restful import reqparse
from .model import RideModel
blue_print_rides = Blueprint('blue_print_rides', __name__)


@swag_from('/api/apidocs/get_rides.yml')
@blue_print_rides.route('/api/v1/rides', methods=['GET'])
def get_all_rides():
    rides = RideModel.get_rides()
    if type(rides) == str:
        return rides, 400
    else:
        return jsonify({"rides": rides}), 200


@swag_from('/api/apidocs/create_ride.yml')
@blue_print_rides.route('/api/v1/rides/create', methods=['POST'])
def _create_ride():
    parser = reqparse.RequestParser()
    parser.add_argument("ref_no")
    parser.add_argument("date")
    parser.add_argument("time")
    arguments = parser.parse_args()

    ride_instance = RideModel(arguments["ref_no"], arguments["date"], arguments["time"])
    created_ride = RideModel.create_ride(ride_instance)

    return jsonify({"ride": created_ride}), 200


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
    if type(remaining_rides) == str:
        return remaining_rides, 400
    return jsonify({'remaining_rides': remaining_rides}), 200


