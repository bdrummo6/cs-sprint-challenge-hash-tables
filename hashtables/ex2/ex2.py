#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route_dict = {}

    trip = [None] * length

    for route in tickets:
        route_dict[route.source] = route.destination

    locale = route_dict['NONE']

    for stop in range(length):
        trip[stop] = locale
        locale = route_dict[locale]

    return trip
