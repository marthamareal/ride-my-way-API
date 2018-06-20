from flask import Flask, jsonify, Blueprint, request, json

app = Flask(__name__)
blue_print = Blueprint('rides', __name__)

rides = [
    {
        "id": 1,
        "ref_no": "RF0001",
        "date": "20/02/2018",
        "time": "11:30 AM"

    },
    {
        "id": 2,
        "ref_no": "RF0001",
        "date": "20/02/2018",
        "time": "11:30 AM"

    }
]


@blue_print.route('/api/v1/rides', methods=['GET'])
def get_rides():

    return jsonify({"rides": rides}), 200


@blue_print.route('/api/v1/rides/<int:ride_id>', methods=['GET'])
def get_ride(ride_id):
    for ride in rides:
        if ride.get('id') == ride_id:
            return jsonify({"ride": ride}), 200
        continue

    return "No ride found", 400


@blue_print.route('/api/v1/rides/create', methods=['POST'])
def create_ride():
    data = request.data
    json_data = get_data(data)

    result = (json_data["rides"]["id"], json_data["rides"]["ref_no"],
              json_data["rides"]["date"], json_data["rides"]["time"])

    print(result)


"""This data deserializes json
 object"""


def get_data(data):

    json_data = json.loads(data)
    print(json_data)
    return json_data
