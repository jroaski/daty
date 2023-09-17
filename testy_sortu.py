import unittest
from datetime import datetime
from dates_sorter import *

class FunctionsTests(unittest.TestCase):
    def test_valid_date(self):
        line = "01.08.2023"
        expected = datetime(2023, 8, 1)
        result_str = get_date(line)  # Get the date as a string
        result = datetime.strptime(result_str, "%d.%m.%Y")  # Convert the string to a datetime object
        self.assertEqual(result, expected)
    def test_invalid_date(self):
        # Test invalid date extraction (no date present)
        line = "Text without date"
        expected = None
        result = get_date(line)
        self.assertIsNone(result)

    def test_key_valid_date(self):
        lines = ["10.08.2023 Some text"]
        expected = datetime(2023, 8, 10)

        date_str = get_date(lines[0])

        result = datetime.strptime(date_str, "%d.%m.%Y")

        self.assertEqual(result, expected)


    def test_lines_by_dates(self):
        # Test grouping lines by dates
        lines = [
            "01.08.2023 radom shrandom words",
            "Text 2",
            "02.08.2023 Text 3",
            "03.08.2023 Text 4"
        ]
        expected = [
            ["01.08.2023 radom shrandom words", "Text 2"],
            ["02.08.2023 Text 3"],
            ["03.08.2023 Text 4"]
        ]
        date_line_dict = group_lines_by_dates(lines)
        actual = [value for value in date_line_dict.values()]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
