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

    def test_key_valid_date(self):
        group = ["10.08.2023 Some text"]
        result = sort_key(group)
        expected = datetime(2023, 8, 10)
        self.assertEqual(result, expected)

    def test_lines_by_dates(self):
        lines = [
            "01.08.2023 radom shrandom words",
            "Text 2",
            "02.08.2023 Text 3",
            "03.08.2023 Text 4",
        ]
        result = group_lines_by_dates(lines)
        expected = [
            ["01.08.2023 radom shrandom words", "Text 2"],
            ["02.08.2023 Text 3"],
            ["03.08.2023 Text 4"],
        ]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()