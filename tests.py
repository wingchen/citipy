import citipy
import unittest


class TestNearestCity(unittest.TestCase):
    def test_tainan(self):
        city = citipy.nearest_city(22.99, 120.21)
        self.assertEqual('tainan', city.city_name)

    def test_Quimper(self):
        city = citipy.nearest_city(48.0, -4.1)
        self.assertEqual('quimper', city.city_name)

    def test_Yako(self):
        city = citipy.nearest_city(12.95, -2.26)
        self.assertEqual('yako', city.city_name)

    def test_NewYork(self):
        city = citipy.nearest_city(40.78, -73.96)
        self.assertEqual('edgewater', city.city_name)

    def test_Wellington(self):
        city = citipy.nearest_city(-41.28, 174.77)
        self.assertEqual('wellington', city.city_name)

if __name__ == '__main__':
    unittest.main()
