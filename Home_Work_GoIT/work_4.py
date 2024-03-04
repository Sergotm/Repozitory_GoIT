from datetime import datetime, timedelta

user_list_dict = [
    {'name':'Pawel Oskar','birthday':'2012.03.04'},
    {'name':'Nensi Kuper','birthday':'2012.03.08'},
    {'name':'Nick Baber','birthday':'2002.03.05'},
    {'name':'Renni Fuler','birthday':'2005.03.09'}]

def get_upcoming_birthdays(users:list) -> list:
    TODAY_DATE = datetime.today().date()
    n_upcoming_birthdays = []

    for user in users:
        user['birthday'] = datetime.strptime(user['birthday'], '%Y.%m.%d').date()

    for user in users:
        # Тут присвоим наш 2024 год учаснику для проверки дальше . / 2012-03-01 -> 2024-03-01
        birthday_this_year = user["birthday"].replace(year=TODAY_DATE.year)

        #  Проверка не прошел день рождения
        if birthday_this_year < TODAY_DATE:
            birthday_this_year = birthday_this_year.replace(year=TODAY_DATE.year + 1)
        if birthday_this_year == TODAY_DATE:
            n_upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday_this_year})
            
        
        # Проверяем попадет ли день на суботу или воскресенье
        if (birthday_this_year.weekday() == 5):  # Субота
                birthday_this_year += timedelta(days=2)  # Переход на следущий понедельник

        elif (birthday_this_year.weekday() == 6):  # Воскресенье
                birthday_this_year += timedelta(days=1)  # Переход на следущий понедельник

        # Тут будет разница между Днем рождения и сегодняшним днем для сравнения дальше
        count_day = (birthday_this_year - TODAY_DATE).days

        # Сохраняем дату имя персонажа и дату если оно <= 7 
        if count_day != 0 and count_day <= 7:
            n_upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday_this_year})

    return n_upcoming_birthdays
        

upcoming_birthdays = get_upcoming_birthdays(user_list_dict)
print(f'Список привітань на цьому тижні:{upcoming_birthdays}')
