# Use Case Sequence Diagrams

This document provides Mermaid sequence diagrams for the use cases defined in `design/use_case_model.md`. All flows start from `CarbonCommute`.

---

## 1) Add Vehicles
```mermaid
sequenceDiagram
    actor User
    participant CarbonCommute
    participant Vehicle
    participant FuelEconomyCSV as Fuel Economy CSV

    User->>CarbonCommute: Select "Add/Manage Vehicles"
    CarbonCommute->>Vehicle: prompt()
    Note over User,Vehicle: User enters make, model, year
    Vehicle->>FuelEconomyCSV: fetch_economy_data(make, model, year)
    FuelEconomyCSV-->>Vehicle: economy_data (dict)
    Vehicle-->>CarbonCommute: new Vehicle(make, model, year)
    CarbonCommute->>CarbonCommute: vehicles.append(vehicle)
```

---

## 2) Calculate Trip
```mermaid
sequenceDiagram
    actor User
    participant CarbonCommute
    participant Vehicle
    participant Route
    participant GoogleAPI as Google Routes API
    participant Trip

    User->>CarbonCommute: Select "Add Trip"
    CarbonCommute->>User: List vehicles and prompt selection
    User-->>CarbonCommute: Vehicle index
    CarbonCommute->>User: Prompt origin, destination, frequency, occurrence, passengers
    User-->>CarbonCommute: Inputs
    CarbonCommute->>Route: new Route(origin, destination)
    Route->>GoogleAPI: fetch_route_data()
    GoogleAPI-->>Route: distance in meters
    Route->>Route: meters_to_miles()
    Route-->>CarbonCommute: distance (miles)
    CarbonCommute->>Trip: new Trip(route, vehicle, frequency, occurrence, passengers)
    Trip->>Vehicle: get_mpg("city")
    Vehicle-->>Trip: mpg
    Trip->>Trip: calculate_emissions()
    Trip-->>CarbonCommute: total_emissions
    CarbonCommute-->>User: Display emissions and confirm added
```

---

## 3) Calculate Carbon Footprint
```mermaid
sequenceDiagram
    actor User
    participant CarbonCommute
    participant Trip
    participant Vehicle

    Note over CarbonCommute,Trip: In current code, footprint is calculated during Trip creation
    User->>CarbonCommute: Proceed after entering trip details
    CarbonCommute->>Trip: __init__(route, vehicle, frequency, occurrence, passengers)
    Trip->>Vehicle: get_mpg("city")
    Vehicle-->>Trip: mpg
    Trip->>Trip: calculate_emissions()
    Trip-->>CarbonCommute: total_emissions
    CarbonCommute-->>User: Show emissions result
```

---

## 4) Display Statistics
```mermaid
sequenceDiagram
    actor User
    participant CarbonCommute
    participant Trip

    User->>CarbonCommute: Select "View Summary"
    loop For each trip
        CarbonCommute->>Trip: read total_emissions
        Trip-->>CarbonCommute: total_emissions (lbs CO2)
    end
    CarbonCommute->>CarbonCommute: Aggregate weekly/monthly/yearly totals
    CarbonCommute-->>User: Show aggregated results
```

---

## 5) Save to File
```mermaid
sequenceDiagram
    actor User
    participant CarbonCommute
    participant Vehicle
    participant File as File System

    User->>CarbonCommute: Select "Save Data"
    CarbonCommute->>User: Prompt filename (default data/savefile.json)
    User-->>CarbonCommute: Filename
    loop For each vehicle
        CarbonCommute->>Vehicle: to_dict()
        Vehicle-->>CarbonCommute: vehicle dict
    end
    CarbonCommute->>CarbonCommute: Build trips JSON payload
    CarbonCommute->>File: write JSON
    File-->>CarbonCommute: write ok
    CarbonCommute-->>User: Confirm save
```

---

## 6) Load from File
```mermaid
sequenceDiagram
    actor User
    participant CarbonCommute
    participant Vehicle
    participant Route
    participant Trip
    participant File as File System

    User->>CarbonCommute: Select "Load File"
    CarbonCommute->>User: Prompt filename (default data/savefile.json)
    User-->>CarbonCommute: Filename
    CarbonCommute->>File: read JSON
    File-->>CarbonCommute: JSON data
    loop Vehicles
        CarbonCommute->>Vehicle: from_dict(data)
        Vehicle-->>CarbonCommute: Vehicle instance
        CarbonCommute->>CarbonCommute: vehicles.append(vehicle)
    end
    loop Trips
        CarbonCommute->>Route: new Route(origin, destination, distance)
        CarbonCommute->>Vehicle: resolve by index or from_dict
        CarbonCommute->>Trip: new Trip(route, vehicle, frequency, occurrence, passengers)
        Trip-->>CarbonCommute: Trip instance
        CarbonCommute->>CarbonCommute: trips.append(trip)
    end
    CarbonCommute-->>User: Show loaded counts
```
