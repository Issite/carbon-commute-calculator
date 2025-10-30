# Carbon Footprint Calculator - Project Outline

## 1. System Description and Vision

### Overview
We will create a **Carbon Footprint Calculator** to aid users in selecting sustainable transportation options.

### Requirements and Scope
To accomplish this, we will need:
- **Route Information**: total distance and road type
- **Vehicle Information**: fuel efficiency, fuel type, and passengers

### Data Sources
- **External Sources**: Google API, fueleconomy.gov
- **User Input**: Information provided at calculation time or through presets

### Core Features
The application will:
- Allow users to input information at calculation time or select from/create presets
- Display different transportation options including:
  - Driving
  - Biking
  - Public transportation
- Feature a robust options system with:
  - Preset creation and editing
  - Customizable travel type displays
  - Lifetime and average statistics

### Stakeholders
- Students, faculty, and community members invested in clean, sustainable transportation options
- Transportation system managers or producers interested in sustainability data

### External Systems
1. **Google Routes API**
- **Creator**: Google
- **Description**: Publicly available API providing distance, time, and route information in JSON format
- **Release Date**: May 2023 (builds upon Distance Matrix API from 2005)
- **Input Requirements**: origin, destination, travelMode, and field mask
- **Request Method**: POST HTTP request
- **Usage Limits**: 10,000 free calls per project
- **URL**: [Google Routes API Documentation](https://developers.google.com/maps/documentation/routes?hl=en)
2. **Hosting services** (for potential web application expansion)

## 2. Application Domain Data

### Use Cases
  1. A user provides details for their vehicle and recieves fuel efficiency and C02 emissions for their vehicle.
    - make
    - model
    - year
    - trim
  2. A user can also input a travel destination (and source) to see the Carbon Footprint of their vehicle alongside the carbon footprint of public transportation options.
  3. User is able to save vehicles as presets, and select from them for given trips.
  4. User selects which presets/public transportation options should be displayed.
  5. User can set occurnances for trips, and see their transportation carbon footprint for the day/week/month/year.

### Dataset 1: Fuel Economy Data

- **Creator**: United States Department of Energy
- **Data Source**: Environmental Protection Agency's National Vehicle and Fuel Emissions Laboratory in Ann Arbor, Michigan
- **Publication Schedule**: 
  - Annual guide for each year's vehicles
  - Monthly updates to running list of current year data
  - Master list containing all years' data (updated monthly)
- **Latest Update**: October 6th, 2025
- **Content**: Comprehensive vehicle data including cylinder count, passenger capacity, and fuel efficiency metrics
- **URL**: [www.fueleconomy.gov/feg/download.shtml](http://www.fueleconomy.gov/feg/download.shtml)

## 3. Deployment Environment Overview

We will use Poetry for venv and dependency management, as well as building project deployables. Our project's development structure will follow the pattern set in our initial Rack-O project, split into `src`, `test`, `design`, and other folders. We will use git branches for developing new features and fixing bugs, as well as GitHub's Project feature for tracking, managing, and assigning issues and responsibilities.
In terms of user runtime environment, we will strive for minimalism, requiring only the Python standard library and an internet connection to use the Google Routes API. If the project progresses to the point of using Django or other frontend-focused resources, we may reassess and add more dependencies. Either way, we will use Poetry to create and manage the final build.

## 4. Project Timeline and Responsibilities

- Week 9 (Oct 20 - Oct 27)
  - Deliverables:
    - Use cases
    - Domain Model
    - System Sequence Diagram
    - Glossary
  - Assignee: IA, CH

- Week 10 (Oct 27 - Nov 3)
  - Deliverables:
    - Sequence Model and Class Diagram for the following use cases.
      - Get vehicle information (mpg, seats, make, model, year) from the user, create preset.
      - Input preset into calculator, output CO2 emissions for each preset.
  - Assignee: IA, CH

- Weeks 10–13 (Nov 3 - Nov 24)
  - Deliverables:
    - Algorithm that has MPG and seats as input, travel distance, outputs the CO2 emissions.
  - Assignee: CH

- Weeks 10–13 (Nov 3 - Nov 24)
  - Deliverables:
    - Menu for selecting options (Start a calculation, Manage presets, preferences, exit).
    - When starting a calculation, ask for the miles of the trip, and perform the C02 calculation for all selected presets.
    - When managing a preset, ask the user for the make, model, trim, mpg, seats of the car, add this to presets.
  - Assignee: IA, CH

- Weeks 11–13 (Nov 3 - Nov 24)
  - Deliverables:
    - Instead of asking the user for the distance of the trip, ask for the source and destination of the trip.
    - Make an HTTP request using Calculate Routes Matrix to get the accurate distances for each transportation method.
  - Assignee: CH

- Weeks 11–13 (Nov 3 - Nov 24)
  - Deliverables:
    - Allow users to change default settings for transportation options displayed
    - Implement preset options for
      - Vehicle presets (make, model, year, trim)
      - Route presets (distances, road types)
    - Save and load user preferences between sessions
    - Provide an export feature for precalculated carbon footprint data
  - Assignee: IA

- Weeks 11–13 (Nov 3 - Nov 24)
  - Deliverables:
    - Read and parse the dataset into usable data structures
    - Implement search functionality to find vehicle data based on user input (make, model, year, trim)
    - (Potentially) pare down dataset to only include relevant fields for efficiency
    - Handle edge cases where vehicle data is not found or incomplete
  - Assignee: IA

- Weeks 14+ (Nov 24 - Dec 1)
  - Deliverables: Interface
  - Assignee: IA, CH
---

*Last updated: October 20, 2025*
