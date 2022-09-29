import unittest
from pathlib import Path

from NN_trick import calculation


class testingTrick(unittest.TestCase):

    def test_check_file_exists(self):
        self.assertIsNotNone(self)

    def test_calculation(self):
        self.assertEqual(calculation(15,72),15)
        
if __name__ == '__main__':
    unittest.main()
