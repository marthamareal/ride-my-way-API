from ..rides.rideModel import RideAPI

requests = []


class RequestModel:

    def __init__(self, user_id, ride_id):
        self.request_id = RideAPI.generate_id(requests)
        self.user_id = user_id
        self.ride_id = ride_id
        self.status = "pending"

    def create_request(self):

        request = {

            "id": self.request_id,
            "user_id": self.user_id,
            "ride_id": self.ride_id,
            "status": "pending"
        }
        requests.append(request)

        return request

    @staticmethod
    def get_request(request_id):
        for request in requests:
            if request.get("id") == request_id:
                return request
            break

        return "Ride request not found"

