import unittest

from slayer import program

class testing_slayer(unittest.TestCase):

    def test_check_file_exists(self):
        self.assertIsNotNone(self)

    def test_program(self):
        self.assertEqual(program(142857),"True")

if __name__ == '__main__':
    unittest.main()
