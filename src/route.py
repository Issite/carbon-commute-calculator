"""Route model and utilities.

This module defines the :class:`Route` object which contains simple
origin/destination information and a placeholder method for fetching
route metrics such as distance. The real implementation should call
an external routing API (for example, Google Routes API) to populate
the distance and other route metadata.
"""


class Route:
    """Represent a travel route between an origin and a destination.

    Parameters
    ----------
    origin : str
        The starting address or location identifier for the route.
    destination : str
        The destination address or location identifier for the route.
    total_distance : float, optional
        Pre-populated distance for the route in miles (default is 0).
    """

    def __init__(self, origin, destination, total_distance=0):
        self.origin = origin
        self.destination = destination
        self.distance = total_distance

    def fetch_route_data(self):
        """Fetch route metrics and update this Route instance.

        This is a placeholder that should perform an HTTP request to an
        external routing service to determine the route distance and
        other metadata. For now, if no distance is set the method
        assigns a reasonable default to allow downstream logic to run.

        Returns
        -------
        float
            The distance for the route in miles.
        """
        # Placeholder for HTTP request to Google Route Matrix API
        if self.distance == 0:
            self.distance = 100  # Placeholder distance in miles to prevent failure, replace this with API
        return self.distance