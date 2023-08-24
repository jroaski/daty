from datetime import datetime

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
# Function for sorting
def sort_key(group):
    date = get_date(group[0])
    if date is None:
        # Place lines without dates at the end
        return datetime.max
    return date


input_file = r"C:\Users\Jacob\Desktop\daty.txt"
output_file = "sorted_output.txt"

with open(input_file, 'r') as f:
    lines = f.readlines()

# Split lines into groups based on dates
line_groups = []
current_group = []

for line in lines:
    if get_date(line):
        if current_group:
            line_groups.append(current_group)
        current_group = [line]
    else:
        current_group.append(line)

# Append the last group
if current_group:
    line_groups.append(current_group)

# Sort lines based on dates in order
sorted_line_groups = sorted(line_groups, key=sort_key, reverse=True)

# Flatten the sorted line groups back into a list of lines
sorted_lines = []

for group in sorted_line_groups:
    for line in group:
        sorted_lines.append(line)

# Write sorted lines back to the text file
with open(output_file, 'w') as f:
    f.writelines(sorted_lines)

print("Text file sorted by dates.")
