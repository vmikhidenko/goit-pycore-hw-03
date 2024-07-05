from datetime import datetime

def get_days_from_today(date):

    date_string = datetime.strptime(date, "%Y-%m-%d")

    current_date = datetime.now()

    timedelta = current_date - date_string

    return timedelta.days

date = input("Введіть дату: РРРР-ММ-ДД: ")

days_difference = get_days_from_today(date) 

print(f"До заданої дати: {(days_difference)}")