import re
import logging
from datetime import datetime
import os
from typing import List, Dict, Optional
from collections import defaultdict


# todo: regex instead of dividing  by words

# todo: add info if block of  text has no date assigned
#: todo: logging, as in file logs, import logging...


#I'm not sure if I'm supposed to switch return so it returns datetime object, or this approach with Optional is actually
# usable. Like ???
def get_date(line: str) -> Optional[datetime]:
    date_formats = ["%d.%m.%Y", "%Y-%m-%d", "%d-%m-%Y"]
    for date_format in date_formats:
        parts = line.strip().split(' ')
        for part in parts:
            try:
                date = datetime.strptime(part, date_format)
                return date
            except ValueError:
                logging.error("Invalid date")
                pass
    return None


# todo: normalize dateformat, while sorting date it should sort by key, which  is a single type of date :DD-MM-YYYY
#sorts by key and grops together lines, so it goes date-> text...

def sort_key(group: List[str]) -> datetime:
    date = get_date(group[0])
    if date is None:
        return datetime.max
    return date


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


# todo: add typing(done)

def read_lines_from_file(file_path: str, encoding: str = 'utf-8') -> List[str]:
    with open(file_path, 'r', encoding=encoding) as f:
        lines = f.readlines()
    return lines


# todo: date as a key in dict, lines just as a value, lists (done?)
# todo: check defaultdict


def group_lines_by_dates(lines: List[str]) -> Dict[datetime, List[str]]:
    date_line_dict = defaultdict(list)

    for line in lines:
        date = get_date(line)
        if date:
            date_line_dict[date].append(line)

    return date_line_dict


def sort_and_flatten_groups(date_line_dict: Dict[datetime, List[str]]) -> List[str]:
    sorted_dates = sorted(date_line_dict.keys(), key=lambda x: (x.year, x.month, x.day), reverse=True)
    sorted_lines = []

    for date in sorted_dates:
        sorted_lines.extend(date_line_dict[date])

    return sorted_lines


def write_lines_to_file(lines: List[str], output_file: str, encoding: str = 'utf-8') -> None:
    with open(output_file, 'w', encoding=encoding) as f:
        f.writelines(lines)


# todo: add, arg-pars,output as input form users main
# todo: should take arguments,change main-name,so it corresponds to what it does

def main() -> None:
    default_path = r"C:\Users\Jacob\Downloads\kazaniatxt.txt"
    input_path = get_valid_file_path("Provide a path (or press Enter for default): ", default_path)
    print("Selected file path:", input_path)

    output_file = "sorted_output.txt"

    lines = read_lines_from_file(input_path, encoding='utf-8')
    date_line_dict = group_lines_by_dates(lines)
    # todo: setup pycharm so it properly points to references by cltr lclick
    sorted_lines = sort_and_flatten_groups(date_line_dict)
    write_lines_to_file(sorted_lines, output_file, encoding='utf-8')

    print("Text file sorted by dates.")


if __name__ == "__main__":
    main()
