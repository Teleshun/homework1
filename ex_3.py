import re

phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

def normalize_phone(phone_number):
    cleaned_numbers = re.sub(r'[^0-9+]', '', phone_number)

    if cleaned_numbers:
        if not cleaned_numbers.startswith('+'):
            if cleaned_numbers.startswith('380'):
                cleaned_numbers = "+" + cleaned_numbers
            else:
                cleaned_numbers = "+38" + cleaned_numbers

    return cleaned_numbers

for phone_number in phone_numbers:
    normalized_number = normalize_phone(phone_number)
    print(normalized_number)

    
