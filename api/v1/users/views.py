from flask import jsonify, Blueprint
from flask_restful import reqparse
from .model import UserModel

blue_print_users = Blueprint('blue_print_users', __name__)


@blue_print_users.route('/api/v1/users', methods=['GET'])
def get_users():
    users = UserModel.get_users()
    if type(users) == str:
        return users, 400
    else:
        return jsonify({"users": users}), 200


@blue_print_users.route('/api/v1/users/create', methods=['POST'])
def create():
    parser = reqparse.RequestParser()
    parser.add_argument("f_name")
    parser.add_argument("l_name")
    parser.add_argument("email")
    parser.add_argument("phone_no")
    parser.add_argument("password")
    parser.add_argument("city")
    arguments = parser.parse_args()

    user_instance = UserModel(arguments["f_name"], arguments["l_name"], arguments["email"],
                              arguments["city"], arguments["phone_no"], arguments["password"])

    created_user = UserModel.create_user(user_instance)

    return jsonify({"user": created_user}), 200


@blue_print_users.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    user = UserModel.get_user(user_id)

    if type(user) == str:
        return user, 400
    return jsonify({"user": user}), 200


@blue_print_users.route('/api/v1/users/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    remaining_users = UserModel.delete_user(user_id)
    if type(remaining_users) == str:
        return remaining_users, 400
    return jsonify({'remaining_users': remaining_users}), 200


