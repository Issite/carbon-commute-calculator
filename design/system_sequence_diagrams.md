# System Sequence Diagrams (Use Case Coverage)

System-level sequence diagrams for all use cases in `design/use_case_model.md`. These show only interactions between the User, the System (CarbonCommute), and External Systems, aligned with current code.

---

## 1) Add Vehicles
```mermaid
sequenceDiagram
    actor User
    participant System
    participant FuelCSV

    User->>System: Open "Add/Manage Vehicles"
    alt Add new vehicle
        User->>System: Enter make, model, year
        System->>FuelCSV: Lookup economy data
        FuelCSV-->>System: Economy data
        System->>User: Confirm vehicle added
    else Edit existing vehicle
        User->>System: Select vehicle to edit
        User->>System: Update details
        System->>FuelCSV: Refresh economy data
        FuelCSV-->>System: Economy data
        System->>User: Confirm vehicle updated
    end
```

---

## 2) Calculate Trip
```mermaid
sequenceDiagram
    actor User
    participant System
    participant RoutesAPI

    User->>System: Select "Add Trip"
    User->>System: Choose vehicle
    User->>System: Input origin and destination
    User->>System: Provide frequency, occurrence, passengers
    System->>RoutesAPI: Compute distance for origin to destination
    RoutesAPI-->>System: Distance (meters)
    System->>User: Show trip emissions result
```

---

## 3) Calculate Carbon Footprint
```mermaid
sequenceDiagram
    actor User
    participant System

    User->>System: Proceed after entering trip details
    System->>System: Compute emissions (fuel type, mpg, distance, passengers)
    System->>User: Display emissions and prompt to save or discard
```

---

## 4) Display Statistics
```mermaid
sequenceDiagram
    actor User
    participant System

    User->>System: Select "View Summary"
    System->>System: Aggregate weekly/monthly/yearly from saved trips
    System->>User: Display aggregated results
```

---

## 5) Save to File
```mermaid
sequenceDiagram
    actor User
    participant System
    participant File as "File System"

    User->>System: Select "Save Data"
    System->>User: Prompt filename
    User-->>System: Provide filename
    System->>File: Write JSON (vehicles, trips)
    File-->>System: Write ok
    System->>User: Confirm save
```

---

## 6) Load from File
```mermaid
sequenceDiagram
    actor User
    participant System
    participant File as "File System"

    User->>System: Select "Load File"
    System->>User: Prompt filename
    User-->>System: Provide filename
    System->>File: Read JSON
    File-->>System: JSON data
    System->>User: Show loaded vehicle/trip counts
```
