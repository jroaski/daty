import unittest
from datetime import datetime
from dates_sorter import *


class FunctionsTests(unittest.TestCase):
    def test_get_date_valid(self):
        line = "Some text  01.08.2023 random  different words"
        result = get_date(line)
        expected = datetime(2023, 8, 1)
        self.assertEqual(result, expected)

    def test_get_date_invalid(self):
        line = "Text without date"
        result = get_date(line)
        self.assertIsNone(result)




if __name__ == '__main__':
    unittest.main()