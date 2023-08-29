import datefinder

with open(r"C:\Users\Jacob\Desktop\daty.txt", 'r') as f:
    full_text = f.read()

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

unmapped_text = full_text[0:first_date_beginning]
mapped_text = '\n\n'.join([full_text[key[1]:value] for key, value in sorted(text_dict.items())])