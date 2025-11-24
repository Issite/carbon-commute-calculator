"""Vehicle model and emissions lookup utilities.

This module contains the :class:`Vehicle` class which stores
basic vehicle metadata and is expected to fetch emissions or
fuel-efficiency data from an external API. Current network
interactions are placeholders.
"""


class Vehicle:
    """Represent a vehicle and its emissions-related attributes.

    Parameters
    ----------
    make : str
        Vehicle manufacturer (e.g., 'Toyota').
    model : str
        Vehicle model name (e.g., 'Corolla').
    year : int
        Model year of the vehicle.
    fuel_type : str
        Type of fuel used (e.g., 'Gasoline', 'Diesel', 'Electric').
    seats : int
        Number of seats in the vehicle.
    """

    def __init__(self, make, model, year, fuel_type, seats):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type #Gasoline, Diesel, Electric
        self.seats = seats
        self.emissions_data = self.fetch_emissions_data()

    def fetch_fuel_data(self):
        """Fetch fuel/economy data for this vehicle from an API.

        This placeholder should be replaced with a real HTTP request
        to a service that can provide fuel economy or emissions
        factors for the given vehicle. Implementations should return
        structured data that other components can consume.
        """
        # Placeholder for HTTP request to Vehicle Emissions API
        pass