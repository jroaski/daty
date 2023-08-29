import datefinder


def read_text_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def extract_dates_and_text(full_text):
    text_dict = {}
    previous_key = None
    first_date_beginning = None
    text_len = len(full_text)
    dates = datefinder.find_dates(full_text, index=True, strict=True)

    for date in dates:
        new_key = (date[0], date[1][0])
        text_dict[new_key] = text_len
        if previous_key:
            text_dict[previous_key] = new_key[1]
        else:
            first_date_beginning = new_key[1]

        previous_key = new_key

    unmapped_text_result = full_text[:first_date_beginning]
    mapped_text_result = '\n\n'.join([full_text[key[1]:value] for key, value in sorted(text_dict.items())])

    return unmapped_text_result, mapped_text_result


def save_text_to_file(text, file_path):
    with open(file_path, 'w') as f:
        f.write(text)


input_file_path = r"C:\Users\Jacob\Downloads\kazaniatxt.txt"
output_file_path = r"C:\Users\Jacob\Downloads\output.txt"

full_text_results = read_text_file(input_file_path)
unmapped_text_results, mapped_text = extract_dates_and_text(full_text)

save_text_to_file(unmapped_text, output_file_path)
