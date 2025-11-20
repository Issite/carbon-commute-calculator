# Class for route object, including origin and destination, time, distance, and HTTP request to Google Route Matrix API
class Route:
    def __init__(self, origin, destination, total_distance=0):
        self.origin = origin
        self.destination = destination
        self.distance = total_distance

    def fetch_route_data(self):
        # Placeholder for HTTP request to Google Route Matrix API
        if self.distance == 0:
            self.distance = 100  # Placeholder distance in miles to prevent failure, replace this with API
        return self.distance