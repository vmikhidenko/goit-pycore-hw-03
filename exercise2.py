import random

def get_numbers_ticket(minimum, maximum, quantity):
    if not (1 <= minimum <= 1000 and 1 <= maximum <= 1000 and 1 <= quantity <= (maximum - minimum + 1)):
        return []

    unique_numbers = set()
    while len(unique_numbers) < quantity:
        random_number = random.randint(minimum, maximum)
        unique_numbers.add(random_number)

    return sorted(unique_numbers)

try:
    minimum = int(input("Введіть мінімальне число від 1 до 1000: "))
    maximum = int(input("Введіть максимальне число від 1 до 1000: "))
    quantity = int(input("Введіть кількість чисел до згенерування: "))

    random_numbers = get_numbers_ticket(minimum, maximum, quantity)
    print(f"Унікальні номери результату: {random_numbers}")

except ValueError:
    print("Неправильний формат введення числа.")
