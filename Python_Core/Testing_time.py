from datetime import datetime, timezone, timedelta
# Запрашиваем у пользователя год его рожденния
user_info = input(f'Please year of birth: Fortam _YYYY_ \n')
check_user = datetime.strptime(user_info, '%Y')
new_time = datetime.now()

result = new_time.year - check_user.year


print(f'Your {result} years!')