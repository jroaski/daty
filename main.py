from datetime import datetime

# Read the content of the text file
with open(r'C:\Users\Jacob\Downloads\kazaniatxt.txt', 'r') as file:
    lines = file.readlines()

# Parse dates and create a list of tuples (date, line)
date_lines = []
for line in lines:
    parts = line.strip().split('\t')  # Assuming the date is tab-separated
    if len(parts) == 2:
        date_str = parts[0]
        content = parts[1]
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            date_lines.append((date, line))
        except ValueError:
            pass  # Skip lines with invalid dates

# Define a function to extract the date from a tuple
def get_date(item):
    return item[0]

# Sort the list of tuples by date
date_lines.sort(key=get_date)

# Write the sorted content back to the text file
with open('sorted_output.txt', 'w') as file:
    for date, line in date_lines:
        file.write(line)

print("File sorted by dates and saved as 'sorted_output.txt'")


def main():
    file_path = input("Provide a file path: ")
    input_text = load_text(file_path)

    if input_text is None:
        print("Failed to load the file. Please check the path and encoding.")
        return

    text_parts = split_text_by_dates(input_text)
    save_text_parts(text_parts)

    print('Splitting and saving complete.')

if __name__ == "__main__":
    main()
