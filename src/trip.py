# Class containing route object, vehicle object, and methods to calculate total emissions for a trip.
class Trip:
    def __init__(self, route, vehicle, frequency=0, occurance=1, passengers=1):
        self.route = route
        self.vehicle = vehicle
        self.frequency = frequency
        self.occurance = occurance
        self.passengers = passengers
        self.total_emissions = self.calculate_emissions()

    def calculate_emissions(self):
        # Placeholder for emissions calculation logic
        distance = self.route.distance
        emissions = self.vehicle.emissions_data
        gallons_used = distance / emissions
        if self.vehicle.fuel_type == "Gasoline":
            total_emissions = (gallons_used * 19.6) / self.passengers  # Assuming 19.6 lbs CO2 per gallon of gasoline
        elif self.vehicle.fuel_type == "Diesel":
            total_emissions = (gallons_used * 22.4) / self.passengers  # Assuming 22.4 lbs CO2 per gallon of diesel
        elif self.vehicle.fuel_type == "Electric":
            total_emissions = 0  # Electric vehicles assumed to have zero emissions for this placeholder
        return total_emissions * self.frequency * self.occurance