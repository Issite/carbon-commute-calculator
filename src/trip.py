# Class containing route object, vehicle object, and methods to calculate total emissions for a trip.
class Trip:
    def __init__(self, route, vehicle, frequency, occurance):
        self.route = route
        self.vehicle = vehicle
        self.frequency = frequency
        self.occurance = occurance
        self.total_emissions = self.calculate_emissions()

    def calculate_emissions(self):
        # Placeholder for emissions calculation logic
        pass