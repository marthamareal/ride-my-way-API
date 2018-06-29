"""
Declare a global variable list which will hold our rides, initially its empty.
"""

rides = []


class RideModel:
    def __init__(self, ref_no, date, time, source, destination, user_id):
        """
                This method acts as a constructor for our class, its used to initialise class attributes
        """
        self.ride_id = self.generate_id(rides)
        self.ref_no = ref_no
        self.date = date
        self.time = time
        self.source = source
        self.destination = destination
        self.user_id = user_id
        self.source = source
        self.destination = destination
        self.requests_no = 0

    def create_ride(self):
        """
                This method receives an object of the class, creates and returns a dictionary from the object
        """

        ride = {
            "id": self.ride_id,
            "ref_no": self.ref_no,
            "date": self.date,
            "time": self.time,
            "source": self.source,
            "destination": self.time,
            "user_id": self.user_id,
            "requests_no": self.requests_no
        }
        rides.append(ride)
        return ride

    @staticmethod
    def get_ride(ride_id):
        """
                This method returns a particular ride of the id given to it from the list of available rides
        """
        for ride in rides:
            if ride.get('id') == ride_id:
                return ride
            continue
        return {"ride": "Requested ride is not found"}

    @staticmethod
    def get_rides():
        """
                This method returns all ride created in our list above
        """
        if rides:
            return rides
        return {"ride": "No ride Found"}

    @staticmethod
    def delete_ride(ride_id):
        """
                This method deletes a ride which has a provided id
        """
        for count, ride in enumerate(rides):
            if ride.get("id") == ride_id:
                rides.pop(count)
                return rides
        return rides

    @staticmethod
    def generate_id(_list):
        """
                This method auto generates ids for the ride_requests by starting from 1
                if first ride in list and increment 1 from the last ride in list
        """
        if _list:
            return _list[-1].get("id") + 1
        return 1

    @staticmethod
    def update(ride_id, date, time, source, destination):
        for ride in rides:
            if ride.get("id") == ride_id:
                ride["date"] = date
                ride["time"] = time
                ride["source"] = source
                ride["destination"] = destination
                return ride
        return {"ride": "ride not found"}

