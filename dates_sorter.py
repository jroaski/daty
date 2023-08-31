from datetime import datetime
import os



# todo: regex instead of dividing  by words

# todo: add info if block of  text has no date assigned
#: todo: logging, as in file logs, import logging...
def get_date(line):
    date_formats = ["%d.%m.%Y", "%Y-%m-%d", "%d-%m-%Y"]
    for date_format in date_formats:
        parts = line.strip().split(' ')
        for part in parts:
            try:
                date = datetime.strptime(part, date_format)
                return date
            except ValueError:
                pass
        return None

# todo: normalize dateformat, while sorting date it should sort by key, which  is a single type of date :DD-MM-YYYY
#sorts by key and grops together lines, so it goes date-> text...
def sort_key(group):
    date = get_date(group[0])
    if date is None:
        return datetime.max
    return date


def get_valid_file_path(prompt, default_path):
    while True:
        input_file = input(prompt)

        if input_file == "":
            return default_path
        #can be deleted
        else:
            if os.path.exists(input_file):
                return input_file
            else:
                print("Invalid path. Please provide a valid file path.")

# todo: add typing
def read_lines_from_file(file_path, encoding: str = 'utf-8') -> str:
    with open(file_path, 'r', encoding=encoding) as f:
        lines = f.readlines()
    return lines

# todo: date as a key in dict, lines just as a value, lists
# todo: check defaultdict
#todo: try to get rid  of line 61, so I can make it generic
def group_lines_by_dates(lines):
    line_groups = []
    current_group = []

    for line in lines:
        if get_date(line):
            if current_group:
                line_groups.append(current_group)
            current_group = [line]
        else:
            current_group.append(line)

    if current_group:
        line_groups.append(current_group)

    return line_groups


def sort_and_flatten_groups(line_groups):
    sorted_line_groups = sorted(line_groups, key=sort_key, reverse=True) #lambda
    sorted_lines = [line for group in sorted_line_groups for line in group]
    return sorted_lines


def write_lines_to_file(lines, output_file, encoding='utf-8'):
    with open(output_file, 'w', encoding=encoding) as f:
        f.writelines(lines)

# todo: add, arg-pars,output as input form users main
# todo: should take arguments,change main-name,so it corresponds to what it does



def main():
    default_path = r"C:\Users\Jacob\Downloads\kazaniatxt.txt"
    input_path = get_valid_file_path("Provide a path (or press Enter for default): ", default_path)
    print("Selected file path:", input_path)

    output_file = "sorted_output.txt"

    lines = read_lines_from_file(input_path, encoding='utf-8')
    line_groups = group_lines_by_dates(lines)
    # todo: setup pycharm so it properly points to references by cltr lclick
    sorted_lines = sort_and_flatten_groups(line_groups)
    write_lines_to_file(sorted_lines, output_file, encoding='utf-8')

    print("Text file sorted by dates.")


if __name__ == "__main__":
    main()
