# Domain Model

This diagram represents the primary software domains (concepts) and their relationships/interactions. It focuses on how domains relate, not code classes.

```mermaid
classDiagram
direction LR

class User {
  <<actor>>
  +selectsVehicle()
  +providesRoute()
  +viewsEmissions()
  +savesOrDiscardsTrip()
  +viewsStatistics()
}

class System {
  <<application>>
  +manageVehicles()
  +calculateTrip()
  +computeFootprint()
  +aggregateStatistics()
  +saveData()
  +loadData()
}

class VehicleDomain {
  <<domain>>
  +make
  +model
  +year
  +fuelType
  +mpgCity/highway
}

class RouteDomain {
  <<domain>>
  +origin
  +destination
  +distanceMiles
}

class TripDomain {
  <<domain>>
  +vehicleRef
  +routeRef
  +passengers
  +frequencyDays
  +occurrenceCount
  +emissionsLbsCO2
}

class PreferencesDomain {
  <<domain (planned)>>
  +displayOptions
  +presetSelection
}

class FuelEconomyDataset {
  <<external>>
  +vehicleEconomyLookup()
}

class GoogleRoutesAPI {
  <<external>>
  +computeDistance()
}

class FileSystem {
  <<external>>
  +readJSON()
  +writeJSON()
}

%% Relationships
User --> System : interacts
System o-- VehicleDomain : manages
System o-- TripDomain : manages
TripDomain *-- VehicleDomain : references
TripDomain *-- RouteDomain : references
System ..> GoogleRoutesAPI : fetch route distance
System ..> FuelEconomyDataset : lookup economy data
System ..> FileSystem : save/load data
PreferencesDomain <.. System : planned settings
RouteDomain <.. GoogleRoutesAPI : distance source
VehicleDomain <.. FuelEconomyDataset : economy source

```

Notes
- Domains abstract the data/behavior of the application, separate from code classes.
- Preferences are planned per `use_case_model.md` but not implemented yet.
- External systems are modeled as separate domains with directional dependencies.
