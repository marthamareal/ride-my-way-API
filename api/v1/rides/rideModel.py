
"""
Declare a global variable list which will hold our rides, initially its empty.
"""
rides = []


class RideAPI:
    """
        This method returns all rides created in our list
        """
    def __init__(self, ref_no, date, time):
        self.ride_id = self.generate_id(rides)
        self.ref_no = ref_no
        self.date = date
        self.time = time

    """
        This method returns all rides created in our list
    """

    @staticmethod
    def get_rides():

        global rides
        if rides:
            return rides
        return "No rides Found"

    """
        This method returns a particular ride of the id given to it from the list of available rides
    """

    @staticmethod
    def get_ride(ride_id):
        global rides
        for ride in rides:
            if ride.get('id') == ride_id:
                return ride
            continue

        return "Requested ride is not found"

    """
        This method recieve an object of the class, creates and returns a dictionary from the object
    """

    def create_ride(self):

        ride = {
            "id": self.ride_id,
            "ref_no": self.ref_no,
            "date": self.date,
            "time": self.time
        }

        rides.append(ride)

        return ride

    """
        This method auto generates ids for the rides by starting from 1 
        if first ride in list and increment 1 from the last ride in list
    """

    @staticmethod
    def generate_id(_list):
        if _list:
            return _list[-1].get("id") + 1
        return 1
