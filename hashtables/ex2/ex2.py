#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # dict for holding the the source and destination for each leg of the trip
    route_dict = {}

    # Create an array to hold each place in your trip
    trip = [None] * length

    for ticket in tickets:
        route_dict[ticket.source] = ticket.destination

    # Set the initial source to next_source
    next_source = route_dict['NONE']

    # iterate through the length of the trip storing each location in order from first to last in the array trip
    for stop in range(length):
        trip[stop] = next_source
        next_source = route_dict[next_source]

    # return the array of places on your trip
    return trip
