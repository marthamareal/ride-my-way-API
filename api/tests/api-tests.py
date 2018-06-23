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

    # REQUEST SECTION

    def test_request_ride(self):
        data = json.dumps({"user_id": 1, "ride_id": 1})
        response = self.test_client.post('/api/v1/requests', data=data, headers =self.json_headers)
        results = json.loads(response.data.decode())

        self.assertEqual(results, {'request': self.create_sample_request(1, 1, 1)})
        self.assertEqual(response.status_code, 200)

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
    def create_sample_request(request_id, user_id, ride_id):
        request ={
                "id": request_id,
                "user_id": user_id,
                "ride_id": ride_id,
                "status": "pending"
        }

        return request

    def find_sample_ride(self, ride_id):

        return self.create_sample_ride(ride_id, "R0027", "10/02/2009", "10:00 AM")


if __name__ == '__main':
    unittest.main()
