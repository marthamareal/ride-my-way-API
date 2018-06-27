import unittest
import json
from api import app


def create_sample_user(f_name, l_name, email, city, phone_no, password):
    user = {
        "id": 1,
        "f_name": f_name,
        "l_name": l_name,
        "email": email,
        "city": city,
        "phone_no": phone_no,
        "password": password
    }
    return user


class TestUserCases(unittest.TestCase):
    json_headers = {'Content-Type': 'application/json'}
    sample_user = create_sample_user("martha", "mareal", "marthamareal@gmail.com", "kampala", "+256 7898238278", "pass")

    def setUp(self):

        self.test_client = app.test_client()

    def test_create(self):

        data = json.dumps(self.sample_user)

        response = self.test_client.post('/api/v1/users/create', data=data, headers=self.json_headers)
        result = json.loads(response.data.decode())

        self.assertEqual(result, {'user': self.sample_user})
        self.assertEqual(response.status_code, 200)

    def test_get_user(self):

        response = self.test_client.get('/api/v1/users/1')
        result = json.loads(response.data.decode())

        self.assertEqual(result, {'user': self.sample_user})
        self.assertEqual(response.status_code, 200)

    def test_get_users(self):

        response = self.test_client.get('/api/v1/users')

        if type(response.data) == str:

            self.assertEqual(response.status_code, 400)
        else:
            results = json.loads(response.data.decode())
            print(response.data.decode())
            self.assertEqual(results, {"users": [self.sample_user]})
            self.assertEqual(response.status_code, 200)

    def test_l_delete_user(self):
        response = self.test_client.delete('/api/v1/users/delete/1')
        results = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(results, {"remaining_users": []})
