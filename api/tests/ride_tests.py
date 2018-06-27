import unittest
import json
from api import app


def create_sample_ride(ride_id, ref_no, date, time):
    ride = {
        "id": ride_id,
        "ref_no": ref_no,
        "date": date,
        "time": time
    }

    return ride


class RideTestCases(unittest.TestCase):
    json_headers = {'Content-Type': 'application/json'}
    sample_ride = create_sample_ride(1, "R0027", "10/02/2009", "10:00 AM")

    def setUp(self):

        self.test_client = app.test_client()

    def test_create_ride(self):

        data = json.dumps(self.sample_ride)

        response = self.test_client.post('/api/v1/rides/create', data=data, headers=self.json_headers)
        result = json.loads(response.data.decode())

        self.assertEqual(result, {'ride': self.sample_ride})
        self.assertEqual(response.status_code, 200)

    def test_get_ride(self):

        response = self.test_client.get('/api/v1/rides/1')
        result = json.loads(response.data.decode())

        self.assertEqual(result, {'ride': self.sample_ride})
        self.assertEqual(response.status_code, 200)

    def test_get_rides(self):

        response = self.test_client.get('/api/v1/rides')

        if type(response.data) == str:

            self.assertEqual(response.status_code, 400)
        else:
            results = json.loads(response.data.decode())
            print(response.data.decode())
            self.assertEqual(results, {"rides": [self.sample_ride]})
            self.assertEqual(response.status_code, 200)

    def test_l_delete_ride(self):
        response = self.test_client.delete('/api/v1/rides/delete/1')
        results = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(results, {"remaining_rides": []})
