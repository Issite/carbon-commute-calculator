# Statistics Sequence Diagram
```mermaid
    sequenceDiagram
        actor User
        participant System

        User->>System: View Statistics
        System->>System: Get Saved Trips
        System->>System: Display Statistics
```