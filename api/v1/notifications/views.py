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


@blue_print_notifications.route('/api/v1/notifications/delete/<int:notification_id>', methods=['DELETE'])
def delete_notification(notification_id):
    remaining_notifications = NotificationModel.delete_notification(notification_id)
    if type(remaining_notifications) == str:
        return remaining_notifications, 400
    else:
        return jsonify({'remaining_notifications': remaining_notifications}), 200
