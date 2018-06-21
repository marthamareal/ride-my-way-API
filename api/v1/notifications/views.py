from flask import Flask, Blueprint, jsonify

from .notificationsModel import NotificationAPI

app = Flask(__name__)

blue_print_notifications = Blueprint('blue_print_notifications', __name__)


@blue_print_notifications.route('/api/v1/notifications', methods=['POST'])
def get_notifications():

        notifications = NotificationAPI.get_notifications()
        return jsonify({"Notifications": notifications}), 200
