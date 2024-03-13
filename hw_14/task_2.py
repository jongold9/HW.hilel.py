import re

def format_phone_number(phone_number):
    # Видаляємо всі символи, окрім цифр
    cleaned_number = re.sub(r'\D', '', phone_number)

    # Перевірка довжини номера та його формату
    if len(cleaned_number) == 10:
        formatted_number = f"({'+38'}) {cleaned_number[:3]} {cleaned_number[3:6]}-{cleaned_number[6:8]}-{cleaned_number[8:]}"
        return formatted_number
    elif len(cleaned_number) == 12 and cleaned_number.startswith('380'):
        formatted_number = f"({'+38'}) {cleaned_number[3:6]} {cleaned_number[6:9]}-{cleaned_number[9:11]}-{cleaned_number[11:]}"
        return formatted_number
    elif len(cleaned_number) == 9:
        formatted_number = f"({'+38'}) {cleaned_number[:2]} {cleaned_number[2:5]}-{cleaned_number[5:7]}-{cleaned_number[7:]}"
        return formatted_number
    else:
        return 'Failed to recognize number'

# Приклади використання
phone_numbers = [
    "063-999-99-99",
    "063 999-99-99",
    "063-99999-99",
    "+3806399-999-99",
    "380639999999"
]

for number in phone_numbers:
    print(format_phone_number(number))
