# Settings Sequence Diagram
```mermaid
    sequenceDiagram
        actor User
        Participant System
        participant Vehicle Dataset

        User->>System: Open Settings

        loop until exit
            System->>System: Display Settings
            User->>System: Select Setting
            User->>System: Change Setting
            
            System->>System: Save Settings
        end
```