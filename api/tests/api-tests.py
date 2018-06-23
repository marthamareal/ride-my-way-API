import unittest
import json


from api import app


class TestCases(unittest.TestCase):
    json_headers = {'Content-Type': 'application/json'}

    def setUp(self):

        self.test_client = app.test_client()

    def test_create_ride(self):

        data = json.dumps(self.create_sample_ride(1, "R0027", "10/02/2009", "10:00 AM"))

        response = self.test_client.post('/api/v1/rides/create', data=data, headers=self.json_headers)
        result = json.loads(response.data.decode())

        self.assertEqual(result, {'ride': self.create_sample_ride(1, "R0027", "10/02/2009", "10:00 AM")})
        self.assertEqual(response.status_code, 200)

    def test_get_ride(self):

        response = self.test_client.get('/api/v1/rides/1')
        result = json.loads(response.data.decode())

        self.assertEqual(result, {'ride': self.find_sample_ride(1)})
        self.assertEqual(response.status_code, 200)

    def test_get_rides(self):

        response = self.test_client.get('/api/v1/rides')
        results = json.loads(response.data.decode())
        self.assertEqual(results, {"rides": [self.create_sample_ride(1, "R0027", "10/02/2009", "10:00 AM")]})
        self.assertEqual(response.status_code, 200)

    def test_l_delete_ride(self):
        response = self.test_client.delete('/api/v1/rides/delete/1')
        results = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(results, {"remaining_rides": []})

    # REQUEST SECTION

    def test_create_ride_request(self):
        data = json.dumps({"user_id": 1, "ride_id": 1})
        response = self.test_client.post('/api/v1/requests/request_ride', data=data, headers=self.json_headers)
        results = json.loads(response.data.decode())

        self.assertEqual(results, {'ride_request': self.create_sample_ride_request(1, 1, 1)})
        self.assertEqual(response.status_code, 200)

    def test_approve_ride__request(self):
        data = json.dumps({"request_id": "1", "user_id": 1, "approval": "yes"})
        response = self.test_client.post('/api/v1/requests/ride_requests/approve', data=data, headers=self.json_headers)
        if type(response.data.decode()) == str:
            self.assertEqual(response.status_code, 400)
        else:
            results = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(results, {
                "notification": self.create_sample_notification(1, 1, "Your request has been rejected"),
                "ride_request": {"id": 1, "ride_id": 1, "status": "no", "user_id": 1}})

    def test_get_ride_requests(self):

        response = self.test_client.get('/api/v1/ride_requests/requests')
        results = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(results, {"ride_requests": [self.create_sample_ride_request(1, 1, 1)]})

    def test_get_notifications(self):

        response = self.test_client.get('/api/v1/notifications')
        if type(response.data.decode()) == str:
            self.assertEqual(response.status_code, 400)
        else:
            results = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(results, {"notifications": self.create_sample_notification(1, 1, "notification message")})

    @staticmethod
    def create_sample_ride(ride_id, ref_no, date, time):

        ride = {
            "id": ride_id,
            "ref_no": ref_no,
            "date": date,
            "time": time
        }

        return ride

    @staticmethod
    def create_sample_ride_request(request_id, user_id, ride_id):
        ride_request ={
                "id": request_id,
                "user_id": user_id,
                "ride_id": ride_id,
                "status": "pending"
        }
        return ride_request

    @staticmethod
    def create_sample_notification(notification_id, user_id, message):
        notification = {
            "id": notification_id,
            "user_id": user_id,
            "message": message
        }
        return notification

    def find_sample_ride(self, ride_id):

        return self.create_sample_ride(ride_id, "R0027", "10/02/2009", "10:00 AM")


if __name__ == '__main':
    unittest.main()
