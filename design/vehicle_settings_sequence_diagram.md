# Settings Sequence Diagram
```mermaid
    sequenceDiagram
        actor User
        Participant System
        participant Vehicle Dataset

        User->>System: Open Settings

        loop
                System->>System: Display Settings
                User->>System: Add Vehicle
                User->>System: Edit Vehicle
                System->>Vehicle Dataset: Get Vehicle Data
                System->>System: Save Vehicle

                User->>System: Select Preferences
                System->>System: Save Preferences
        end
        
```