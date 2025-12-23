import re


def normalize_phone(phone_number):
    pattern = r"[A-Za-z\s;,\-:!\.()\\]"
    replacement = ""
    formatted_phone = re.sub(pattern, replacement, phone_number) #find characters based on the pattern and remove it
    formatted_phone = f"+38{formatted_phone[-10:]}" #get the last 10 digits of the numbers and add +38 to it
    return formatted_phone


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)