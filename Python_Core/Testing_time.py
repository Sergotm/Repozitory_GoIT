from datetime import datetime, timezone, timedelta


# # Запрашиваем у пользователя год его рожденния ////////////////////////////////////
# user_info = input(f'Please write year of birth: Fortam _YYYY_ \n')
# check_user = datetime.strptime(user_info, '%Y')
# new_time = datetime.now()
# result = new_time.year - check_user.year
# print(f'Your {result} years!')

# # Програма определяет день недели по дате ////////////////////////////////////
# user_info = input(f'Please write of random day: Fortam YYYY_MM_DD \n')
# new = datetime.strptime(user_info, '%Y-%m-%d')
# check_user = new.strftime('%A')

# print(check_user)

# # Програма запрашивае две даты, и выводит разницу между ними ////////////////////////////////////
# new_data_1 = input(f'Please write random date_1\n')
# new_data_2 = input(f'Please write random date_2\n')

# check_data_1 = datetime.strptime(new_data_1,'%Y-%m-%d')
# check_data_2 = datetime.strptime(new_data_2,'%Y-%m-%d')

# result = check_data_1 - check_data_2
# print(f'{result}')

# # Програма расчитывает сколько осталось дней до Нового года ////////////////////////////////////

# TIME = datetime.now()
# NEW_YEAR = datetime(year=2025,month=1,day=1)
# print(f'{NEW_YEAR - TIME}')

# # Програма запрашивает день свадьби и выводит на экран сколько дней прошло с етого момента

# Wedding_DAY = input(f'Please write Wedding day: Format YYYY_MM_DD \n')
# New_time = datetime.now()

# From_W_Day = datetime.strptime(Wedding_DAY, '%Y-%m-%d')
# result_Y = New_time.year - From_W_Day.year
# result_M = New_time.month - From_W_Day.month
# result_D = New_time.day - From_W_Day.day
# print(f'Прошло только: {result_Y} лет: {result_M} месяцев, и {result_D} дней')
