import unittest
import json
import tempfile
import os
from unittest.mock import patch
from types import SimpleNamespace

from src.carbon_commute import CarbonCommute
from src.trip import Trip


class DummyVehicle:
    def __init__(self, mpg=30, fuel_type="Gasoline"):
        self._mpg = mpg
        self.fuel_type = fuel_type

    def get_mpg(self, driving_type: str) -> float:
        return self._mpg

    def to_dict(self):
        return {"make": "Dummy", "model": "D", "year": 2020}


class TestCarbonCommute(unittest.TestCase):
    def test_save_data_writes_json(self):
        cc = CarbonCommute()
        dummy = DummyVehicle()
        cc.vehicles = [dummy]
        route = SimpleNamespace(origin="A", destination="B", distance=10)
        trip = Trip(route, dummy, frequency=7, occurrence=1, passengers=1)
        cc.trips = [trip]

        tf = tempfile.NamedTemporaryFile(delete=False)
        tf.close()
        filename = tf.name

        try:
            with patch('builtins.input', return_value=filename):
                cc.save_data()

            self.assertTrue(os.path.exists(filename))
            with open(filename, 'r', encoding='utf-8') as fh:
                data = json.load(fh)

            self.assertIn('vehicles', data)
            self.assertIn('trips', data)
            self.assertEqual(len(data['vehicles']), 1)
            self.assertEqual(len(data['trips']), 1)
        finally:
            try:
                os.remove(filename)
            except Exception:
                pass


if __name__ == "__main__":
    unittest.main()
