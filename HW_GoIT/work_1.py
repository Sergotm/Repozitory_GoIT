import datetime

def get_days_from_today(date:str)->int:
    today_data = datetime.datetime.today()
    date = input(f'Please write a random date: \n')
    get_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    result = (today_data - get_date).days

    return f'{result} days'

print(get_days_from_today(date='2020-01-01'))

# 4 Стрiчка коду використовується як модифiкацiя коду. 
# Щоб Користувач мiг сам ввести випадкову дату