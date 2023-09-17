import unittest
from datetime import datetime
from dates_sorter import *
from parameterized import parameterized



class FunctionsTests(unittest.TestCase):
    @parameterized.expand([
        ("01.08.2023", datetime(2023, 8, 1)),
        ("02.08.2023", datetime(2023, 8, 2)),

    ])
    def test_valid_date(self, line, expected):
        result = get_date(line)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ("Text without date", None),
        ("Another text without date", None),
        # Add more test cases here as needed
    ])
    def test_invalid_date(self, line, expected):
        result = get_date(line)
        self.assertIsNone(result)

    @parameterized.expand([
        (["10.08.2023 Some text"], datetime(2023, 8, 10)),
        # Add more test cases here as needed
    ])
    def test_key_valid_date(self, lines, expected):
        date_line_dict = group_lines_by_dates(lines)
        sorted_lines = sort_and_flatten_groups(date_line_dict)
        result = get_date(sorted_lines[0])  # Get the date from the first line in the sorted list
        self.assertEqual(result, expected)
    @parameterized.expand([
        (["01.08.2023 radom shrandom words", "Text 2", "02.08.2023 Text 3", "03.08.2023 Text 4"], [
            ["01.08.2023 radom shrandom words", "Text 2"],
            ["02.08.2023 Text 3"],
            ["03.08.2023 Text 4"],
        ]),
        # Add more test cases here as needed
    ])
    def test_lines_by_dates(self, lines, expected):
        date_line_dict = group_lines_by_dates(lines)
        # I have no other idea how to approach this than converting date_line_dict to a list of lists

        actual = [value for value in date_line_dict.values()]

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
