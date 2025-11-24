"""Entry point for the Carbon Commute application.

This module provides a small CLI entry point that creates and runs
the main `CarbonCommute` application object.
"""

import carbon_commute


def main():
    """Create and run the CarbonCommute application.

    The function instantiates the application class and starts
    its main loop. This function is intended to be used as the
    module entry point when executed as a script.
    """
    app = carbon_commute.CarbonCommute()
    app.run()


if __name__ == "__main__":
    main()