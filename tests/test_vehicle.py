import unittest

from src.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def test_fetch_economy_data_matches_csv_row(self):
        # This project includes a large `data/vehicles.csv` file; pick a known entry
        row = Vehicle.fetch_economy_data("Toyota", "Corolla", 1993)
        self.assertIsNotNone(row)
        self.assertEqual(row["make"], "Toyota")
        self.assertEqual(row["model"], "Corolla")

    def test_vehicle_get_mpg_and_to_from_dict(self):
        v = Vehicle("Toyota", "Corolla", 1993)
        mpg_city = v.get_mpg("city")
        self.assertIsInstance(mpg_city, float)

        d = v.to_dict()
        self.assertEqual(d["make"], v.make)

        v2 = Vehicle.from_dict({"make": v.make, "model": v.model, "year": v.year})
        self.assertIsInstance(v2, Vehicle)
        self.assertEqual(v2.make, v.make)


if __name__ == "__main__":
    unittest.main()
