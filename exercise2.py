import random

def get_numbers_ticket(minimum, maximum, quantity):
    if minimum < 1 or maximum > 1000 or quantity > (maximum - minimum + 1):
        print("Введіть мінімальне число не менше 1, та максимальне число не більше 1000")
        return []

    unique_numbers = set()
    while len(unique_numbers) < quantity:
        random_number = random.randint(minimum, maximum)
        unique_numbers.add(random_number)

    return sorted(unique_numbers)

try:
    minimum = int(input("Введіть мінімальне число: (>= 1): "))
    maximum = int(input("Введіть максимальне число: (<= 1000): "))
    quantity = int(input("Введіть кількість чисел до згенерування: "))

    random_numbers = get_numbers_ticket(minimum, maximum, quantity)
    print(f"Унікальні номери результату: {random_numbers}")
except ValueError:
    print("Введіть менше число.")
