import os
import re
from datetime import datetime
from typing import List, Dict, Optional
import argparse
import logging
from collections import defaultdict

# check flask/ fast api, rest API, so it takes a file as an input and produces a file as output
# dates_sorter should be used as dependencies for the service/rest api
# pre-commit <-check

# Clean up virtual environment, so it has only pip/wheel installed

# Configure logging so it's used instead of printing
logging.basicConfig(filename='../log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Define date formats
date_formats = ["%d.%m.%Y", "%Y-%m-%d", "%d-%m-%Y"]

# Define a regular expression pattern for date detection
date_pattern = rf"\d{{2}}[-./]\d{{2}}[-./]\d{{4}}|\d{{4}}[-./]\d{{2}}[-./]\d{{2}}"


def get_date(line: str) -> Optional[str]:
    match = re.search(date_pattern, line)
    if match:
        date_str = match.group()
        for date_format in date_formats:
            try:
                date = datetime.strptime(date_str, date_format)
                return date.strftime("%d.%m.%Y")  # Normalize to DD.MM.YYYY format
            except ValueError:
                pass
    return None


# todo: normalize date format, while sorting date, it should sort by a key, which is a single type of date: DD-MM-YYYY
# sorts by key and groups together lines, so it goes date-> text...


def get_valid_file_path(prompt: str, default_path: str) -> str:
    while True:
        input_file = input(prompt)

        if input_file == "":
            return default_path
        else:
            if os.path.exists(input_file):
                return input_file
            else:
                print("Invalid path. Please provide a valid file path.")
                logging.warning(f"Invalid file path provided: {input_file}")


def read_lines_from_file(file_path: str, encoding: str = 'utf-8') -> List[str]:
    with open(file_path, 'r', encoding=encoding) as f:
        lines = f.readlines()
    return lines


# defaultdict has a date which is the key in the dict, and value would be the line

def group_lines_by_dates(lines: List[str]) -> Dict[str, List[str]]:
    date_line_dict = defaultdict(list)
    current_date = None
    list_of_dates = []

    for line in lines:
        date = get_date(line)
        if date in list_of_dates:
            current_date = date
        else:
            if date:
                current_date = date
                date_line_dict[current_date] = []
                list_of_dates.append(date)

        if current_date:
            date_line_dict[current_date].append(line)
        else:
            logging.warning(f"Line without date: {line.strip()}")

    return date_line_dict


def sort_and_flatten_groups(date_line_dict: Dict[str, List[str]]) -> List[str]:
    sorted_lines = []

    sorted_dates = sorted(set(date_line_dict.keys()), key=lambda x: datetime.strptime(x, "%d.%m.%Y"), reverse=True)

    for date in sorted_dates:
        # Add text lines
        sorted_lines.extend(date_line_dict[date])

        # Add an empty line for separation
        sorted_lines.append("")

    return sorted_lines


def write_lines_to_file(lines: List[str], output_file: str, encoding: str = 'utf-8') -> None:
    with open(output_file, 'w', encoding=encoding) as f:
        f.write('\n'.join(lines))


# check if default is ACTUALLY default
# make it so whel launching the script from terminal

#HAVE TO CHANGE THE WAY IN WHICH THE FILE IS TAKEN TO PRECESS
def group_text_by_dates(input_file, output_file, use_default=False):
    if not use_default:
        input_file = get_valid_file_path("Enter the path to the input text file: ", input_file)

    lines = read_lines_from_file(input_file, encoding='utf-8')
    date_line_dict = group_lines_by_dates(lines)
    sorted_lines = sort_and_flatten_groups(date_line_dict)
    write_lines_to_file(sorted_lines, output_file, encoding='utf-8')

    print("Text file sorted by dates.")

def sort_text_by_dates(input_file, output_path):
    lines = input_file.read().decode('utf-8').splitlines()
    date_line_dict = group_lines_by_dates(lines)
    sorted_lines = sort_and_flatten_groups(date_line_dict)
    write_lines_to_file(sorted_lines, output_path, encoding='utf-8')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort text lines by dates.")
    parser.add_argument("--use_default", action="store_true")
    parser.add_argument("--input_file", type=str, default=r"C:\Users\Jacob\Downloads\kazaniatxt.txt")
    parser.add_argument("--output_file", type=str, default="sorted_output.txt")

    args = parser.parse_args()
    group_text_by_dates(args.input_file, args.output_file, args.use_default)
