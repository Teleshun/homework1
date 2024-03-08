from datetime import datetime

def get_days_from_today(date):
    specified_date = datetime.strptime(date, '%Y-%m-%d')
    current_datetime = datetime.today()
    date_difference = current_datetime - specified_date
    return date_difference.days

specified_date_str = "2020-10-09"
result = get_days_from_today(specified_date_str)
print(f'Різниця складає {result} днів')


