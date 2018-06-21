from ..rides.rideModel import RideAPI


notifications = []


class NotificationAPI:

    def __init__(self, user_id, message):

        self.notification_id = RideAPI.generate_id(notifications)
        self.user_id = user_id
        self.message = message

    def create_notification(self):

        notification = {
            "id": self.notification_id,
            "user_id": self.user_id,
            "message": self.message
        }
        notifications.append(notification)
        return notification

    @staticmethod
    def get_notifications():

        if notifications:
            return notifications
        return "No Notifications found"
