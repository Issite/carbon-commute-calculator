import unittest
from types import SimpleNamespace

from src.trip import Trip


class DummyVehicle:
    def __init__(self, mpg, fuel_type):
        self._mpg = mpg
        self.fuel_type = fuel_type

    def get_mpg(self, driving_type: str) -> float:
        return self._mpg

    def to_dict(self):
        return {"make": "Dummy", "model": "D", "year": 2020}


class TestTrip(unittest.TestCase):
    def test_trip_emissions_gasoline(self):
        route = SimpleNamespace(distance=100)
        vehicle = DummyVehicle(25, "Gasoline")
        trip = Trip(route, vehicle)
        expected = round((100 / 25) * 19.6, 2)
        self.assertEqual(trip.total_emissions, expected)

    def test_trip_emissions_electric(self):
        route = SimpleNamespace(distance=50)
        vehicle = DummyVehicle(100, "Electric")
        trip = Trip(route, vehicle)
        self.assertEqual(trip.total_emissions, 0)

    def test_trip_unknown_fuel_type_uses_default(self):
        route = SimpleNamespace(distance=20)
        vehicle = DummyVehicle(10, "Unobtanium")
        trip = Trip(route, vehicle)
        expected = round((20 / 10) * 20, 2)
        self.assertEqual(trip.total_emissions, expected)


if __name__ == "__main__":
    unittest.main()
