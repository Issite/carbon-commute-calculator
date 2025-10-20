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
2. **US Department of Energy's fuel economy data**
3. **Hosting services** (for potential web application expansion)

## 2. Application Domain Data

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

### Dataset 2: Compute Routes Matrix

- **Creator**: Google
- **Description**: Publicly available API providing distance, time, and route information in JSON format
- **Release Date**: May 2023 (builds upon Distance Matrix API from 2005)
- **Input Requirements**: origin, destination, travelMode, and field mask
- **Request Method**: POST HTTP request
- **Usage Limits**: 10,000 free calls per project
- **URL**: [Google Routes API Documentation](https://developers.google.com/maps/documentation/routes?hl=en)

## 3. Project Timeline and Responsibilities

| Week(s) | Deliverables | Assignee |
|---------|-------------|----------|
| Week 9 | Use Cases, Analysis/Elaboration Models | IA, CH |
| Week 10 | Design Models | IA, CH |
| Weeks 11-13 | Core algorithms for calculating footprint | CH |
| Weeks 11-13 | CLI Input/Output | IA, CH |
| Weeks 11-13 | Google Compute Routes Matrix integration | CH |
| Weeks 11-13 | Settings and Preferences | IA |
| Weeks 11-13 | Fuel Efficiency Dataset Integration | IA |
| Weeks 14+ | Interface | IA, CH |

---

*Last updated: October 20, 2025*
