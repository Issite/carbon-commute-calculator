# Class for handling IO and UI, as well as managing the main program flow and objects

class CarbonCommute:
    def __init__(self):
        self.vehicles = []
        self.trips = []

    def run(self):
        pass

    def calculator(self):
        pass

    def add_vehicle(self):
        pass

    def view_summary(self):
        for trip in self.trips:
            print(f"Trip from {trip.route.origin} to {trip.route.destination}: {trip.total_emissions} lbs CO2")
        weekly_emissions = sum(trip.total_emissions*(trip.occurance / trip.frequency)*7 for trip in self.trips)
        monthly_emissions = sum(trip.total_emissions*(trip.occurance / trip.frequency)*30 for trip in self.trips)
        yearly_emissions = sum(trip.total_emissions*(trip.occurance / trip.frequency)*365 for trip in self.trips)
        print(f"Weekly Emissions: {weekly_emissions} lbs CO2")
        print(f"Monthly Emissions: {monthly_emissions} lbs CO2")
        print(f"Yearly Emissions: {yearly_emissions} lbs CO2")

    def save_data(self):
        pass