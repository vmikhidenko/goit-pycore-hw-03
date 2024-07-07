from datetime import datetime

def get_days_from_today(date):
    try:
        date_string = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Неправильний формат дати. Введіть дату у форматі 'РРРР-ММ-ДД'.")
        return None

    current_date = datetime.now()

    timedelta = current_date - date_string

    return timedelta.days

while True:
    date = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")

    days_difference = get_days_from_today(date)

    if days_difference is not None:
        print(f"Різниця в днях від заданої дати {date} до сьогoднішньої: {days_difference} днів")
        break  