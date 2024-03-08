from datetime import datetime, timedelta

users = [ 
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Robert Dawson", "birthday": "1989.05.18"},
    {"name": "Robert Davis", "birthday": "1990.03.07"},
    {"name": "Ella Lopez", "birthday": "1990.03.10"},
]

def find_next_weekday(d, weekday: int):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7  
    return d + timedelta(days=days_ahead) 

def prepared_users(users):
    prepared_users = []
    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()  
            prepared_users.append({"name": user['name'], 'birthday': birthday}) 
        except ValueError: 
            print(f'Некоректна дата народження для користувача {user["name"]}')
    return prepared_users

def check_upcoming_birthdays(prepared_users, days=7):   
    today = datetime.today().date() 
    upcoming_birthdays = []
    for user in prepared_users:
        birthday_this_year = user["birthday"].replace(year=today.year)

        if birthday_this_year < today: 
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if 0 <= (birthday_this_year - today).days <= days:
            if birthday_this_year.weekday() >= 5:
                birthday_this_year = find_next_weekday(birthday_this_year, 0)
        
            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })
    return upcoming_birthdays



prepared_users_list = prepared_users(users)
upcoming_birthdays_result = check_upcoming_birthdays(prepared_users_list)
print(upcoming_birthdays_result)



