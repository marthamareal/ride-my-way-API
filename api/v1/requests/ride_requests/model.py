from api.v1.rides.model import RideModel
"""
     Declare a global variable list which will hold our ride_requests, initially its empty.
"""
ride_requests = []


class RideRequestModel:
    def __init__(self, user_id, ride_id):
        """
               This method acts as a constructor for our class, its used to initialise class attributes
        """
        self.request_id = RideModel.generate_id(ride_requests)
        self.user_id = user_id
        self.ride_id = ride_id
        self.status = "pending"

    def create_request(self):
        """
              This method receives an object of the class, creates and returns a dictionary from the object
        """
        request = {
            "id": self.request_id,
            "user_id": int(self.user_id),
            "ride_id": int(self.ride_id),
            "status": "pending"
        }
        ride_requests.append(request)
        return request

    @staticmethod
    def get_request(request_id):
        """
              This method returns a particular ride of the id given to it from the list of available rides
        """
        global ride_requests
        for request in ride_requests:
            if request.get("id") == int(request_id):
                return request
            continue
        return "Ride request not found"

    @staticmethod
    def get_requests():
        """
             This method returns all requests created in our ride_requests list declared above
        """
        if ride_requests:
            return ride_requests
        else:
            return "No ride requests found"

    @staticmethod
    def delete_request(request_id):
        """
                This method deletes a request which has a provided id
        """
        for count, request in enumerate(ride_requests):
            if request.get("id") == request_id:
                ride_requests.pop(count)
                return ride_requests
        return "Request not Found"
