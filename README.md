# Final Project, Caleb & Isaac
# Carbon Commute Calculator

Command-line tool for estimating commute-related carbon emissions and comparing transportation options.

## Features
- Add vehicles and trips via an interactive CLI.
- Compute emissions estimates per trip and roll-ups (weekly, monthly, yearly).
- Integration with Google Routes Matrix API for real distances.
- Integration with fuel economy/emissions data sources.

## Requirements
- Python 3.10+ (tested with Python 3.11).
- Poetry for dependency and venv management.
- Google Cloud project with Routes Matrix API enabled (for real distance data).

## Setup
1) Install Poetry (via pipx recommended):
```bash
pipx install poetry
```

2) Install dependencies:
```bash
poetry install
```

3) Configure environment variables:
- Copy `.env.example` to `.env` (create `.env.example` if it is missing) and set:
	- `GOOGLE_ROUTES_API_KEY=<your_api_key>`
- Ensure your Google Cloud project has the Routes Matrix API enabled.

## Run
```bash
poetry run python main.py
```

## Documentation
Generate HTML docs with `pdoc` (after `poetry install`):
```bash
poetry run pdoc ./main.py -o html
poetry run pdoc ./src -o html
```