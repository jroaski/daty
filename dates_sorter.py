from datetime import datetime
import os


def get_date(line):
    date_format = "%d.%m.%Y"
    parts = line.strip().split(' ')
    for part in parts:
        try:
            date = datetime.strptime(part, date_format)
            return date
        except ValueError:
            pass
    return None


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
        else:
            if os.path.exists(input_file):
                return input_file
            else:
                print("Invalid path. Please provide a valid file path.")


def read_lines_from_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return lines


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


def sort_groups(line_groups):
    sorted_line_groups = sorted(line_groups, key=sort_key, reverse=True)
    sorted_lines = [line for group in sorted_line_groups for line in group]
    return sorted_lines


def write_lines_to_file(lines, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(lines)


def main():
    default_path = r"C:\Users\Jacob\Downloads\kazaniatxt.txt"
    input_path = get_valid_file_path("Provide a path (or press Enter for default): ", default_path)
    print("Selected file path:", input_path)

    output_file = "sorted_output.txt"

    lines = read_lines_from_file(input_path)
    line_groups = group_lines_by_dates(lines)
    sorted_lines = sort_and_flatten_groups(line_groups)
    write_lines_to_file(sorted_lines, output_file)

    print("Text file sorted by dates.")


if __name__ == "__main__":
    main()
