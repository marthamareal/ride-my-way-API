
def generate_id(_list):
    """
            This method auto generates ids for the ride_requests by starting from 1
            if first ride in list and increment 1 from the last ride in list
    """
    if _list:
        return _list[-1].get("id") + 1
    return 1