from datetime import datetime, timedelta

def get_upcoming_birthdays(users, days=7):
    now = datetime.now()
    upcoming_birthdays_list = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").replace(year=now.year)
        upcoming_date = now + timedelta(days=days)
        
        if now <= birthday <= upcoming_date:
            if birthday.weekday() in [5,6]:
                days_to_monday = (7 - birthday.weekday()) % 7
                birthday = birthday + timedelta(days=days_to_monday)


            upcoming_birthdays_list.append({
                "name": user['name'],
                "congratulation_date": birthday.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays_list

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays_list = get_upcoming_birthdays(users, days=7)
print("Upcoming birthdays within 7 days:")
print(upcoming_birthdays_list)

