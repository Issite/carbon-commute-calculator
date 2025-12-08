import unittest

from src.route import Route


class TestRoute(unittest.TestCase):
    def test_meters_to_miles(self):
        r = Route("A", "B")
        # 1609.34 meters is approximately 1 mile
        self.assertAlmostEqual(r.meters_to_miles(1609.34), 1.0, places=3)

    def test_distance_default_is_zero(self):
        r = Route("origin", "dest")
        self.assertEqual(r.distance, 0)


if __name__ == "__main__":
    unittest.main()
