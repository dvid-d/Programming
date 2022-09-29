import unittest

from windchill import calculate_wind_chill

class testingWindChill(unittest.TestCase):

    def test_windchill_calculation(self):
        air_temp = 10
        air_speed = 15
        self.assertEqual(calculate_wind_chill(air_temp, air_speed), -6.5895344209562525)

if __name__ == '__main__':
    unittest.main()

    #when executing this, the program also runs the input() methods inside the air_temp and air_speed variables in the other file
    #even though I only imported the calculate_wind_chill method.
    #It would still do the test after that. The only solution to this that I have thought of was to make the two variables comments.
    
