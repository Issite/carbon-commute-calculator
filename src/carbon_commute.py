"""CLI and application control for the Carbon Commute calculator.

This module provides the :class:`CarbonCommute` class which implements
a minimal command-line interface for managing vehicles, trips and
producing simple summaries. The current implementation contains
placeholder I/O and persistence methods and is suitable for
interactive experimentation and further extension.
"""

from route import Route
from trip import Trip


class CarbonCommute:
    """Main application class handling I/O and program flow.

    The class holds in-memory lists of vehicles and trips and exposes
    methods for running a text-based menu, adding trips, and viewing
    simple emissions summaries.
    """

    def __init__(self):
        """Create a new CarbonCommute application instance."""
        self.vehicles = []
        self.trips = []

    def run(self):
        """Start the interactive application loop."""

        print("Welcome to the Carbon Commute Calculator!")
        while True:
            print("0. Load File")
            print("1. Add Vehicle")
            print("2. Add Trip")
            print("3. View Summary")
            print("4. Save Data")
            print("5. Exit")
    
            choice = input("Select an option: ")
            if choice == '0':
                self.load_file()
            elif choice == '1':
                self.add_vehicle()
            elif choice == '2':
                self.calculator()
            elif choice == '3':
                self.view_summary()
            elif choice == '4':
                self.save_data()
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

    def calculator(self):
        """Interactively create a :class:`Trip` and add it to the app."""
        print("Please select a vehicle:")
        for idx, vehicle in enumerate(self.vehicles):
            print(f"{idx}. {vehicle.make} {vehicle.model} ({vehicle.year}) - {vehicle.fuel_type}")
        
        vehicle_choice = int(input("Enter the number for the vehicle: "))
        while vehicle_choice < 0 or vehicle_choice >= len(self.vehicles):
            vehicle_choice = int(input("Invalid choice. Enter the number of the vehicle: "))
        selected_vehicle = self.vehicles[vehicle_choice]
        
        origin = input("Enter the origin address: ")
        destination = input("Enter the destination address: ")
        route = Route(origin, destination)
        route.fetch_route_data()
        
        #Occurance is the number of times the trip occurs within the frequency (days) period.
        frequency = int(input("Enter the frequency of the trip in days (e.g., 7 for a week, 30 for a month): "))
        occurance = int(input("Enter the number of times this trip occurs in the given frequency: "))
        passengers = int(input("Enter the number of passengers in the vehicle: "))

        trip = Trip(route, selected_vehicle, frequency, occurance, passengers)
        self.trips.append(trip)

        print(f"Trip added! Total emissions for this trip: {trip.total_emissions} lbs CO2")

    def add_vehicle(self):
        """Placeholder for adding a vehicle to the application."""
        pass

    def view_summary(self):
        """Print a human-readable summary of recorded trips and totals."""

        for trip in self.trips:
            print(f"Trip from {trip.route.origin} to {trip.route.destination}: {trip.total_emissions} lbs CO2")

        weekly_emissions = sum(trip.total_emissions*(trip.occurance / trip.frequency)*7 for trip in self.trips)
        monthly_emissions = sum(trip.total_emissions*(trip.occurance / trip.frequency)*30 for trip in self.trips)
        yearly_emissions = sum(trip.total_emissions*(trip.occurance / trip.frequency)*365 for trip in self.trips)

        print(f"Weekly Emissions: {weekly_emissions} lbs CO2")
        print(f"Monthly Emissions: {monthly_emissions} lbs CO2")
        print(f"Yearly Emissions: {yearly_emissions} lbs CO2")

    def save_data(self):
        """Placeholder for persisting application data to disk."""
        pass

    def load_file(self):
        """Placeholder for loading persisted application data."""
        pass