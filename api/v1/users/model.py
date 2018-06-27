from api.v1.rides.model import RideModel

users = []


class UserModel:
    def __init__(self, f_name, l_name, email, city, phone_no, password):
        self.id = RideModel.generate_id(users)
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.city = city
        self.password = password
        self.phone_no = phone_no

    def create_user(self):
        user = {
            "id": self.id,
            "f_name": self.f_name,
            "l_name": self.l_name,
            "email": self.email,
            "city": self.city,
            "phone_no": self.phone_no,
            "password": self.password
        }
        users.append(user)
        return user

    @staticmethod
    def get_user(_id):
        for user in users:
            if user.get("id") == _id:
                return user
        return "User not Found"

    @staticmethod
    def get_users():
        if users:
            return users
        return

    @staticmethod
    def delete_user(user_id):
        """
            This method deletes a ride which has a provided id
        """
        for count, user in enumerate(users):
            if user.get("id") == user_id:
                users.pop(count)
                return users
        return "Ride not Found"
