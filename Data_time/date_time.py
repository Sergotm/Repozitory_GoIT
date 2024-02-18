from datetime import datetime, timezone, timedelta, time
'//////////////////////////////////////////////////////////       /DATE_TIME/             ////////////////////////////////////////////////////////////////////////////////////////////'

'Вернет Год. Месяц. День....'
current_datetime = datetime.now()

'Методы для получения Даты и Время'
current_datetime.date(), 'Вернет только Дату'
current_datetime.time(), 'Вернет только Время'
current_datetime.weekday(), ' Номер дня в Неделе начиная с 0 а воскресенье с -6'
current_datetime.total_seconds(), 'Метод для преобразования в секунды'
current_datetime.toordinal(), 'Возвращающий порядковый номер с  1 января 1 года нашей эры '

'Комбинирование обьектов Data, time'
date_path = datetime.date(2023,12,14)
time_path = datetime.time(12, 30, 15)
combined_datetime = datetime.combine(date_path, time_path)

'Создание обьекта с конкретной датой и времям. Если не указать Час.МинутуюСекунду. Будет 0'
specific_date = datetime(year=2000, month=1, day=17, hour=0,minute=0,second=0)

'Сравнение Datetime'
datetime1 = datetime(2023, 12, 17, 12, 0)
datetime2 = datetime(2023, 12, 17, 12)
datetime1 == datetime2 or ((datetime1 != datetime2 or datetime1 <= datetime2)and datetime1 >= datetime2)


'///////////////////////////////////////////////////////////        timedelta       //////////////////////////////////////////////////////////////////////////////////////'
'Используется для представления разницы между двумя моментами времени'

delta = timedelta(
    days=50,
    seconds=12,
    minutes=34,
    hours=3, 
)
'Выход 50 days, 3:34:12'
delta12 = timedelta(
    days=2,
    seconds=54,
    minutes=42,
    hours=6, 
)
'Выход 2 days, 6:42:54'
timedelta = delta - delta12 # Выход 47 days, 20:51:18
timedelta.total_seconds()   # Выход 4135878.0
'Вычисление от сегодня + 10 дней'
new_data = datetime.now()
future_data = new_data + timedelta(days=10)
'Вычисление от даты + 1 неделя'
Last_data = datetime(year=2024, month=1, day=1,hour=12)
New_data = timedelta(weeks=1)
'///////////////////////////////////////////////////////////        timestamp       //////////////////////////////////////////////////////////////////////////////////////'

'Конвертация timestamp в datetime'
New = datetime.now(), 'представляет собой количество секунд c 1 января 1970'
timestamp = datetime.timestamp(New)

'Конвертация datetime в timestamp'
timestamp2 = 1707571837.994006
dj_time = datetime.fromtimestamp(timestamp2)

'///////////////////////////////////////////////////////////        Парсинг дати из строк       ///////////////////////////////////////////////////////////////////////////'
'''%Y - рік з чотирма цифрами (наприклад, 2023).
%y - рік з двома цифрами (наприклад, 23).
%m - місяць як номер (наприклад, 03 для березня).
%d - день місяця як номер (наприклад, 14).
%H - година (24-годинний формат) (наприклад, 15).
%I - година (12-годинний формат) (наприклад, 03).
%M - хвилини (наприклад, 05).
%S - секунди (наприклад, 09).
%A - повна назва дня тижня (наприклад, Tuesday).
%a - скорочена назва дня тижня (наприклад, Tue).
%B - повна назва місяця (наприклад, March).
%b або %h - скорочена назва місяця (наприклад, Mar).
%p - AM або PM для 12-годинного формату.'''

now = datetime.now()
# Форматування дати і часу
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S"), 'Bспользуется для форматирования объектов даты и времени в строки'

# Форматування лише дати
formatted_date_only = now.strftime("%A, %d %B %Y")

# Форматування лише часу
formatted_time_only = now.strftime("%I:%M %p")

# Форматування лише дати
formatted_date_only = now.strftime("%d.%m.%Y")

format = now.strftime('%Y-%m-%d')

reps = datetime.strptime(format, '%Y-%m-%d')

string = '2000-01-17'
datetime_object = datetime.strptime(string, '%Y-%m-%d'), 'используется для форматирования объектов даты из строк в обьекты'


'///////////////////////////////////////////////////////////       ISO format date      ///////////////////////////////////////////////////////////////////////////'

get = datetime.now()
iso_format = get.isoformat() # 2023-12-14T15:43:42.651309

iso_string = '2023-12-14T15:43:42.651309' 
new = datetime.fromisoformat(iso_string), 'Для обратного преобразования строки ISO 8601 в объект'

iso = datetime.now()
day_weekday = iso.isoweekday()
'Согласно этому стандарту, неделя начинается с понедельника, который имеет значение 1, и заканчивается воскресеньем, которое имеет значение 7.'

day_weekday = iso.isocalendar() ,'год ISO, номер недели года и номер дня недели в соответствии со стандартом ISO 8601.isocalendar()'
print(f'Год {day_weekday[2]} : Неделя {day_weekday[1]} : День {day_weekday[0]}') , 'Получение кортежа с параметрами'

#'преобразовать время UTC во время, соответствующее восточному часовому поясу США (UTC-5 часов)'
utc_time = datetime.now(timezone.utc) 
aester_time = utc_time.astimezone(timezone(timedelta(hours= -5)))

'Чтобы перевести местное время в UTC, например по Киеву'
local_time_zone = timezone(timedelta(hours=2))
utc_time = datetime(year=2024, month=3, day=14, hour=12, minute=34, second=23, tzinfo=local_time_zone)
local_time = utc_time.astimezone(timezone.utc)

local_time_zone = timezone(timedelta(hours=2))
utc_time = datetime.now()
local_time = utc_time.astimezone(local_time_zone)

 