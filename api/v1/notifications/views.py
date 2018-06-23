from flask import Flask, Blueprint, jsonify

from .model import NotificationModel

app = Flask(__name__)

blue_print_notifications = Blueprint('blue_print_notifications', __name__)


@blue_print_notifications.route('/api/v1/notifications', methods=['GET'])
def get_notifications():

        notifications = NotificationModel.get_notifications()
        if type(notifications) == str:
                return notifications, 400
        else:
                return jsonify({"notifications": notifications}), 200
