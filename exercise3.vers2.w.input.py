import re

def sanitize_numbers(phone_number):
    phone_number = re.sub(r"[\D]", "", phone_number)
    
    if phone_number.startswith("0"):
        return "+380" + phone_number[1:] 
    elif phone_number.startswith("80"):
        return "+3" + phone_number 
    elif phone_number.startswith("380"):
        return "+" + phone_number 

phone_numbers_input = input("Введіть номер, або номери телефонів через кому: ")
phone_numbers_list = phone_numbers_input.split(',')

pattern = r"^\+?380?\d{9}$"

for phone_number in phone_numbers_list:
    normalized_phone_number = sanitize_numbers(phone_number.strip())

    if re.match(pattern, normalized_phone_number):
        print(f"Форматовані номери телефонів для розсилки: {normalized_phone_number}")
    else:
        print(f"Неправильний формат номера телефону: {normalized_phone_number}")
