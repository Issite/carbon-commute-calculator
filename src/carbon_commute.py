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
        """Create a new CarbonCommute application instance.

        The application starts with empty `vehicles` and `trips`
        lists. Persistence and vehicle-creation functionality are
        intentionally left as placeholders for later implementation.
        """
        self.vehicles = []
        self.trips = []

    def run(self):
        """Start the interactive application loop.

        The method prints a simple menu and dispatches user choices to
        the corresponding handler methods until the user exits.
        """
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
        """Interactively create a :class:`Trip` and add it to the app.

        Prompts the user to select a vehicle, enter origin and
        destination addresses, and specify frequency/occurrence and
        passenger count. The created :class:`Trip` is appended to the
        application's `trips` list.
        """
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
        """Placeholder for adding a vehicle to the application.

        Implementations should prompt the user for vehicle fields,
        create a :class:`vehicle.Vehicle` instance and append it to
        ``self.vehicles``.
        """
        pass

    def view_summary(self):
        """Print a human-readable summary of recorded trips and totals.

        The method iterates over stored trips and prints each trip's
        emissions, then prints aggregated weekly, monthly and yearly
        estimates. Aggregation uses simple scaling based on the trip's
        configured frequency and occurrence values.
        """
        for trip in self.trips:
            print(f"Trip from {trip.route.origin} to {trip.route.destination}: {trip.total_emissions} lbs CO2")

        weekly_emissions = sum(trip.total_emissions*(trip.occurance / trip.frequency)*7 for trip in self.trips)
        monthly_emissions = sum(trip.total_emissions*(trip.occurance / trip.frequency)*30 for trip in self.trips)
        yearly_emissions = sum(trip.total_emissions*(trip.occurance / trip.frequency)*365 for trip in self.trips)

        print(f"Weekly Emissions: {weekly_emissions} lbs CO2")
        print(f"Monthly Emissions: {monthly_emissions} lbs CO2")
        print(f"Yearly Emissions: {yearly_emissions} lbs CO2")

    def save_data(self):
        """Placeholder for persisting application data to disk.

        A future implementation should serialize `self.vehicles` and
        `self.trips` to a file (for example JSON) and handle errors.
        """
        pass

    def load_file(self):
        """Placeholder for loading persisted application data.

        A real implementation should deserialize previously saved data
        and populate `self.vehicles` and `self.trips` appropriately.
        """
        pass