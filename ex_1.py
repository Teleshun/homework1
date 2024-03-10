from datetime import datetime

def get_days_from_today(date):
    try:
        specified_date = datetime.strptime(date, '%Y-%m-%d')
        current_datetime = datetime.today()
        date_difference = current_datetime - specified_date
        return date_difference.days
    except ValueError as e:
        print(f"Помилка: {e}")
        return None
    
specified_date_str = "2020-10-09"
result = get_days_from_today(specified_date_str)

if result is not None:
    print(f'Різниця складає {result} днів')
else:
    print('Не вдалося обчислити різницю через некоректні вхідні дані.')


