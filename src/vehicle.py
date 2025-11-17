# Class for vehicle object, including make, model, year, fuel type, and emissions data, handling the HTTP request to the Vehicle Emissions API
class Vehicle:
    def __init__(self, make, model, year, fuel_type, seats):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        self.seats = seats
        self.emissions_data = self.fetch_emissions_data()

    def fetch_fuel_data(self):
        # Placeholder for HTTP request to Vehicle Emissions API
        pass