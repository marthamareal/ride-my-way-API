from api.v1 import generate_id
"""
Declare a global variable list which will hold our notifications, initially its empty.
"""
notifications = []


class NotificationModel:
    def __init__(self, user_id, message):
        """
                This method acts as a constructor for our class, its used to initialise class attributes
        """
        self.notification_id = generate_id(notifications)
        self.user_id = user_id
        self.message = message

    def create_notification(self):
        """
                 This method receives an object of the class, creates and returns a dictionary from the object
        """
        notification = {
            "id": self.notification_id,
            "user_id": self.user_id,
            "message": self.message
        }
        notifications.append(notification)
        return notification

    @staticmethod
    def get_notifications():
        """
                This method returns all notifications created in our notifications list above
        """
        if notifications:
            return notifications
        return "No Notifications found"

    @staticmethod
    def delete_notification(notification_id):
        """
                This method deletes a notification which has a provided id
        """
        for count, notification in enumerate(notifications):
            if notification.get("id") == notification_id:
                notifications.pop(count)
                return notifications
        return "Notification not Found"
