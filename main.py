from datetime import datetime

# List of encodings to try out
encodings = ['utf-8', 'latin-1', 'windows-1252']

file_path = input("Provide a file path: ")

for encoding in encodings:
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            text = file.read()
        break  # Break the loop if file reading succeeds
    except UnicodeDecodeError:
        continue  # Try the next encoding if reading fails
dates = []
for word in text.split():
    try:

        date = datetime.strptime(word, '%Y.%m.%d')
        dates.append(date)
    except ValueError:
        try:
            # If the parsing fails, try parsing the date assuming the format is 'DD-MM-YYYY'
            date = datetime.strptime(word, '%d.%m.%Y')
            dates.append(date)
        except ValueError:
            pass

dates.sort()

# Split the text by dates
text_parts = []
prev_date = None
for date in dates:
    if prev_date is not None:
        index = text.find(prev_date.strftime('%Y.%m.%d')) or text.find(prev_date.strftime('%d.%m.%Y'))
        text_parts.append(text[:index].strip())
        text = text[index:]
    prev_date = date

# Append the remaining text
text_parts.append(text.strip())

# Save the divided text as separate file
for i, part in enumerate(text_parts):
    filename = f'output_{i+1}.txt'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(part)
    print(f'Saved {filename}')

print('Splitting and saving complete.')
