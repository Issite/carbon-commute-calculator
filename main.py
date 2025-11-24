"""Entry point for the Carbon Commute application.

This module provides a small CLI entry point that creates and runs
the main `CarbonCommute` application object.
"""

import carbon_commute


def main():
    """Create and run the CarbonCommute application."""
    app = carbon_commute.CarbonCommute()
    app.run()


if __name__ == "__main__":
    main()