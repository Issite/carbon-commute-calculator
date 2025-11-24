"""Vehicle model and emissions lookup utilities.

This module contains the :class:`Vehicle` class which stores
basic vehicle metadata and is expected to fetch emissions or
fuel-efficiency data from an external API. Current network
interactions are placeholders.
"""


class Vehicle:
    """Represent a vehicle and its emissions-related attributes."""

    def __init__(self, make, model, year, fuel_type, seats):
        """Initialize a :class:`Vehicle` instance."""
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type #Gasoline, Diesel, Electric
        self.seats = seats
        self.emissions_data = self.fetch_emissions_data()

    @staticmethod
    def prompt()-> 'Vehicle':
        """Prompt the user for vehicle details and return a Vehicle instance."""
        make = input("Enter vehicle make: ")
        model = input("Enter vehicle model: ")
        year = int(input("Enter vehicle year: "))
        fuel_type = Vehicle.fetch_fuel_data(make, model, year)["fuelType1"]
        seats = Vehicle.fetch_fuel_data(make, model, year)["seats"]
        return Vehicle(make, model, year, fuel_type, seats)

    @staticmethod
    def fetch_fuel_data(make: str, model: str, year: int)->dict:
        """Fetch fuel/economy data for this vehicle from an API."""
        
        pass