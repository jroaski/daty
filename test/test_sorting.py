import unittest
from datetime import datetime
from parameterized import parameterized
from dates_sorter import *

# expected and result should swap places, so expected should be first


class FunctionsTests(unittest.TestCase):
    @parameterized.expand(
        [
            ("01.08.2023", datetime(2023, 8, 1)),
            ("Text without date", None),
            ("10.08.2023 Some text", datetime(2023, 8, 10)),
        ]
    )
    def test_valid_date(self, line, expected):
        result_str = get_date(line)  # Get the date as a string
        result = (
            datetime.strptime(result_str, "%d.%m.%Y") if result_str else None
        )  # Convert the string to a datetime object
        self.assertEqual(result, expected)

    @parameterized.expand(
        [
            (
                ["01.08.2023 radom shrandom words", "Text 2"],
                [["01.08.2023 radom shrandom words", "Text 2"]],
            ),
            (["Text 2"], []),
        ]
    )
    def test_lines_by_dates(self, lines, expected):
        date_line_dict = group_lines_by_dates(lines)
        actual = [value for value in date_line_dict.values()
                  ] if date_line_dict else []
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
