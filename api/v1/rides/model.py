
"""
Declare a global variable list which will hold our rides, initially its empty.
"""
rides = []


class RideModel:

    def __init__(self, ref_no, date, time):
        """
                This method acts as a constructor for our class, its used to initialise class attributes
        """

        self.ride_id = self.generate_id(rides)
        self.ref_no = ref_no
        self.date = date
        self.time = time

    def create_ride(self):
        """
                This method receives an object of the class, creates and returns a dictionary from the object
        """

        ride = {
            "id": self.ride_id,
            "ref_no": self.ref_no,
            "date": self.date,
            "time": self.time
        }

        rides.append(ride)

        return ride

    @staticmethod
    def get_ride(ride_id):
        """
                This method returns a particular ride of the id given to it from the list of available rides
        """
        global rides

        for ride in rides:
            if ride.get('id') == ride_id:
                return ride
            continue

        return "Requested ride is not found"

    @staticmethod
    def get_rides():
        """
                This method returns all ride created in our list above
        """
        global rides

        if rides:
            return rides
        return "No ride_requests Found"

    @staticmethod
    def generate_id(_list):
        """
                This method auto generates ids for the ride_requests by starting from 1
                if first ride in list and increment 1 from the last ride in list
        """
        if _list:
            return _list[-1].get("id") + 1
        return 1
