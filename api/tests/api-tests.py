import unittest

from api import app


class TestCases(unittest.TestCase):
    def setUp(self):

        self.test_client = app.test_client()

    def test_get_rides(self):
        response = self.test_client.get('/api/v1/requests')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main':
    unittest.main()
