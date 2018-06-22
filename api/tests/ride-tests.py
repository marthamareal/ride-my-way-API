import unittest
import json


from api import app


class TestCases(unittest.TestCase):
    def setUp(self):

        self.test_client = app.test_client()

    def test_create_ride(self):

        data = json.dumps(self.create_sample_ride(1, "R0027", "10/02/2009", "10:00 AM"))
        headers = {'Content-Type': 'application/json'}

        response = self.test_client.post('/api/v1/rides/create', data=data, headers=headers)
        result = json.loads(response.data.decode())

        self.assertEqual(result, {'ride': self.create_sample_ride(1, "R0027", "10/02/2009", "10:00 AM")})
        self.assertEqual(response.status_code, 200)

    def test_get_rides(self):

        response = self.test_client.get('/api/v1/rides')
        results = json.loads(response.data.decode())
        self.assertEqual(results, {"rides": [self.create_sample_ride(1, "R0027", "10/02/2009", "10:00 AM")]})
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


if __name__ == '__main':
    unittest.main()
