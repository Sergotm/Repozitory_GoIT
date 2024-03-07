from datetime import datetime, timedelta
birth_day = datetime(1998,5,20)
now = datetime.now()


result = now + timedelta(birth_day)
print(result)