import unittest

from city_functions import format_location

class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        formatted_location = format_location('santiago', 'chile')
        self.assertEqual(formatted_location, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_location = format_location('santiago', 'chile', 5000000)
        self.assertEqual(formatted_location, 'Santiago, Chile - population 5000000')

unittest.main()
