Use case model:

We will create a Carbon Footprint Calculator to aid users in selecting sustainable transportation options. To do this, we will need the following information:

 - Route Information: Total distance, Road type
 - Vehicle Information: Fuel efficiency, Fuel type, Passengers

Some of this info can be taken from official sources (Google API, fueleconomy.gov), but some must be provided by the user. The app will allow the user to fill in info at calculation time (or select from/create presets). The app should then display different options for transportation, such as driving, biking, public transportation, etc.

The app will also feature a robust options system that includes preset CRUD and what travel types to display, as well as lifetime and average statistics.

Features:
Dataset storage/retrieval

## Use Cases

### 1. Add Vehciles:
User can enter their vehicle information (Make, Model, Year, etc.) under the add vehicle section of the menu/settings (Prompted by the system after selecting the add 'vehcile section').  The system will then access the fuel economy dataset via an HTTP request to gather other vehicle information such as fuel type, fuel efficiency, vehicle type.  These attributes/key-value pairs are then saved in the system as a vehicle object, to be used for further calculations.

### 2. Change preferences:
The user can select from the main menu to view and change their settings. The system will then display the current preferences, and allow the user to select and modify individual settings. These settings include which vehicle presets to display when calculating trips, which transportation options to display when viewing trip calculations, and other general application preferences. When the user has completed their changes, they can select the save option to have the system store their new preferences for future use.

### 3. Calculate Trip:
When selecting the calculate option from the main menu, the user is then prompted to chose which of their preset vehicle options would be used for the trip.  The system then prompts the user for the route information (source, destination), along with the number of passengers.  The system will then access the Google Routes Matrix via an HTTP request to gather the distance and time of the provided route.  These attributes along with the selected vehicle are then used to create a trip object in the system, to be used for further calculations

### 4. Calculate Carbon Footprint
After a trip has been calculated, the system will perform a simple carbon footprint for the trip, based of the fuel type and fuel efficiency of the vehicle, and the number of passengers and distance of the trip.  The system will display this carbon emissions data to the user, along with the option to save this trip with an occurance.  If the user selects no, the trip is deleted.  If the user selects yes, the system will then prompt the user for the frequency and occurance of the trip.  The trip will then be saved and used for further calculations.

### 5. Display Statistics
When the user selects the statistics option from the menu/settings, the system will then perform the carbon footprint calculation for each of the users saved trips, accounting for the frequency and occurnace of the trip.  Each calculation is aggregated to a total, which is presented to the user by weekly, monthly, and yearly carbon footprint.

### 6. Save to File
The user can select the save to file option from the menu/settings, which will then prompt the system to gather all user data including vehicle presets, preferences, and saved trips.  The system will then format this data into a JSON object, and write this object to a file on the users device for future retrieval.

### 7. Load from File
The user can select the load from file option from the menu/settings, which will then prompt the system to read a JSON object from a file on the users device.  The system will then parse this object, and extract the user data including vehicle presets, preferences, and saved trips.  This data is then used to repopulate the system for the user.