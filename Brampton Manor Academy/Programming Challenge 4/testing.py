import unittest

from windchill import calculate_wind_chill

class testingWindChill(unittest.TestCase):

    def test_windchill_calculation(self):
        air_temp = 10
        air_speed = 15
        self.assertEqual(calculate_wind_chill(air_temp, air_speed), -6.5895344209562525)

if __name__ == '__main__':
    unittest.main()
