import datetime
try:
    print(f'Введите дату рождения в формате YYYY-MM-DD')
    check_S = input(f'Введите дату рождения 1 человека: \n')
    check_K = input(f'Введите дату рождения 2 человека: \n')

    New_S = datetime.datetime.strptime(check_S, '%Y-%m-%d')
    New_K = datetime.datetime.strptime(check_K, '%Y-%m-%d')

    result_year = New_K.year - New_S.year
    result_month = New_K.month - New_S.month
    result_days = New_K.day - New_S.day
    print(f'У вас разница {result_year} года {result_month} месяца, и {result_days} дней!')
    
except ValueError:
    print(f'Вам надо ввести дату коректно. В формате YYYY-MM-DD')


# # Просим пользователя вести дату своего рождения
# My_date = input(f'Введите дату своего рождение YYYY-MM-DD: ')
# New_my_date  = datetime.datetime.strptime(My_date, '%Y-%m-%d')

# # Вычисляем сегодняшнюю дату
# touday_data = datetime.datetime.now()


# # Делаем вычесление сколько пользователю лет 
# result = touday_data.year - New_my_date.year
# result_1 = touday_data.month - New_my_date.month
# # Выводим пользователю на екран количетво лет 
# print(f'Вам {result} года, и {result_1} м!')