# Class for route object, including origin and destination, time, distance, and HTTP request to Google Route Matrix API
class Route:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.distance = self.fetch_route_data()

    def fetch_route_data(self):
        # Placeholder for HTTP request to Google Route Matrix API
        pass