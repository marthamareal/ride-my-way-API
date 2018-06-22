from flask import Flask, Blueprint, jsonify
from .requestModel import RequestModel
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

