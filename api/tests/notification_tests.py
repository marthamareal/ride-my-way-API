import unittest
import json
from api import app


def create_sample_notification(notification_id, user_id, message):
    notification = {
        "id": notification_id,
        "user_id": user_id,
        "message": message
    }
    return notification


class NotificationTestCases(unittest.TestCase):
    json_headers = {'Content-Type': 'application/json'}
    sample_notification = create_sample_notification(1, 1, "notification message")

    def setUp(self):

        self.test_client = app.test_client()

    def test_get_notifications(self):
        response = self.test_client.get('/api/v1/notifications')
        if type(response.data.decode()) == str:
            self.assertEqual(response.status_code, 400)
        else:
            results = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(results, {"notifications": self.sample_notification})

    def test_l_delete_notification(self):
        response = self.test_client.delete('/api/v1/notifications/delete/1')
        if type(response.data.decode()) == str:
            self.assertEqual(response.status_code, 400)
        else:
            results = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(results, {"remaining_notifications": []})
