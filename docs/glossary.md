# Glossary

Carbon Footprint Calculator
: An application that estimates the greenhouse gas emissions (CO2 equivalent) associated with transportation choices by combining route distance, vehicle characteristics, and travel mode.

Route
: Data describing a trip between an origin and destination. It will include total distance and road type and is obtained from a routing API.

Google Routes API
: An external web API (provided by Google) used to obtain route geometry, distance, and travel-time information. The project will use this to replace user-entered distances with accurate route data.

Vehicle
: Characteristics of a vehicle used for calculations, such as make, model, year, trim, fuel efficiency (MPG), fuel type, and passenger capacity.

Fuel efficiency (MPG)
: Miles per gallon (or equivalent for other fuels); a measure of how far a vehicle travels per unit of fuel. Used to convert distance into fuel consumed and then into CO2 emissions.

Fuel type
: The kind of fuel a vehicle uses (e.g., gasoline, diesel, electric). Fuel type affects the emissions factor used when converting fuel consumption to CO2e.

Passengers / Seats
: The number of occupants in a vehicle. Emissions can be expressed per-person by dividing vehicle emissions by the number of passengers.

CRUD
: Create, Read, Update, Delete — the four basic operations supported for managing preset Vehicles, Routes, and similar persisted objects.

Dataset / Fuel Economy Data
: Structured data used by the application (for example, the EPA/DOE fuel economy dataset from fueleconomy.gov) that contains vehicle attributes and efficiency metrics used to map make/model/year to MPG values.

Vehicle Dataset
: The local or imported dataset that stores vehicle records used for searching and Vehicle preset creation. Taken from the Fuel Economy Data.

Trip / Saved Trip
: A recorded occurrence of travel (origin, destination, distance, date, selected vehicle) that can be saved for later statistics and analysis.

Statistics (lifetime and average statistics)
: Aggregated metrics computed from saved trips and presets. Examples include lifetime emissions, average emissions per trip, and emissions by time window (day/week/month/year).

Settings / Preferences
: User-configurable options that control app behavior and what travel types or Vehicles are displayed/saved. Settings includes both pre-saved vehicles and app preferences.

CO2 emissions / Carbon footprint
: The calculated greenhouse gas impact of travel, typically expressed as kilograms or metric tons of CO2-equivalent for a trip or for an aggregated period.

Travel mode / Travel types
: The mode of transport used for a trip (e.g., driving, biking, public transportation). Each mode has different emissions calculations or may be treated as zero-emission (e.g., biking).

External Sources
: Any data or services external to the app (for instance, Google Routes API or fueleconomy.gov) that provide authoritative route or vehicle data.

Poetry
: A Python dependency and packaging tool used by this project for virtual environment and dependency management.

Hosting services
: Infrastructure used to deploy a web application or API (e.g., cloud hosting). A possible future requirement if the project expands beyond a CLI or local tool.

MPG
: Abbreviation for miles per gallon. See "Fuel efficiency (MPG)".
