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

    def fetch_fuel_data(self):
        """Fetch fuel/economy data for this vehicle from an API."""
        pass