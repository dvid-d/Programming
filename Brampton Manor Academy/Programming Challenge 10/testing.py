import unittest
from pathlib import Path

from league_table_10 import *


class testingLeagueTable(unittest.TestCase):

    def test_check_file_exists(self):
        csv_file = Path("test.csv")
        self.assertIsNotNone(check_file_exists(csv_file))
        self.assertFalse(check_file_exists(csv_file))   
        
        csv_file = Path("Premier 16-17.csv")
        self.assertTrue(check_file_exists(csv_file))
        
        csv_file = Path("blank.csv")
        self.assertTrue(check_file_exists(csv_file))

        csv_file = Path("one_row.csv")
        self.assertTrue(check_file_exists(csv_file))
        
    def test_read_csv(self):
        csv_file = Path("test.csv")
        self.assertListEqual([], read_csv(csv_file))
        
        csv_file = Path("Premier 16-17.csv")
        self.assertGreaterEqual(len(read_csv(csv_file)), 1)

        csv_file = Path("blank.csv")
        self.assertListEqual([], read_csv(csv_file))

        csv_file = Path("one_row.csv")
        self.assertListEqual([["test", '10']], read_csv(csv_file))
        
if __name__ == '__main__':
    unittest.main()
