# Calculator Sequence Diagram
```mermaid
    sequenceDiagram
        actor User
        participant System
        participant Routes API

        User->>System: Start Calculation
        User->>System: Enter Start and Destination
        System->>System: Get Vehicle Information
        System->>Routes API: Get Route Info (Distance, Time)
        System->>System: Calculate Trips & Display

```