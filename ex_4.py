from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.12.27"},
    {"name": "Robert Dawson", "birthday": "1989.03.18"},
    {"name": "Robert Davis", "birthday": "1990.03.07"},
    {"name": "Ella Lopez", "birthday": "1990.03.13"},
]

def find_next_weekday(d, weekday: int):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + timedelta(days=days_ahead)

def get_upcoming_birthdays(users, days=7):   
    today = datetime.today().date() 
    upcoming_birthdays = []
    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()  
        except ValueError: 
            print(f'Некоректна дата народження для користувача {user["name"]}')
            continue

        birthday_this_year = datetime(today.year, birthday.month, birthday.day).date()

        if birthday_this_year < today: 
            birthday_this_year = datetime(today.year + 1, birthday.month, birthday.day).date()

        if 0 <= (birthday_this_year - today).days <= days:
            if birthday_this_year.weekday() >= 5:
                birthday_this_year = find_next_weekday(birthday_this_year, 0)
        
            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })
    return upcoming_birthdays



upcoming_birthdays_result = get_upcoming_birthdays(users)
print(upcoming_birthdays_result)


