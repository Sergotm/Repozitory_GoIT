#   Строки String ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
s = str
s = '' ,' Одинарные кавычки'
s = " ", ' Двойные кавычки'
s = ''' ''', 'Тройные для длинного текста со смещением'
s = "hello"
x = 'BigBoos'
s.upper() , 's -> S  Перевод всего в большой регистр'
s.lower() , 'S -> s  Перевод всего в малый регистр'
s.isupper() , ''
s.islower() , ''
s = s.startswith('hello') , 'Проверка начала строки. Вернет True/False'
a = '   image.png    '
s = s.endswith('.png') , 'Проверка конца строки. Вернет True/False'
s = 'yes'.capitalize() , 'Сделает первую букву Yes Большой остальные маленькими'
s = 'my name'.title() , ' Сделает каждую первую букву каждого слова в строке Большой остальные маленькими -> My Name'
s = "456".isdigit() , 'Проверяет создана ли строка только с Цифр. Вернет True/False'
s = "Kokos".isalpha(), 'Проверяет создана ли строка только с Букв. Вернет True/False'
s = " ".isspace() , 'Проверяет создана ли строка только с Пробелов. Вернет True/False'
new_replace = a.replace('image', 'image.png'), 'Изменяе или удалает указаную часть изи текста'
s = x.isdigit(), 'Проверяет строку создана он али полностю из цифр Да=True| Нет=False'
s = a.index('h'), 'Поиск по индексу '
s = a.split(','), 'Разделитель c указанием после чего разделить текс в список'
new = ', '.join(a), 'Обратная сторона split'
left = a.lstrip(),'Удалит только левые пробелы'
rait = a.rstrip(),'Удалит только правые пробелы'
cool = a.strip(),'Удалит все пробелы:'
s = x.removeprefix('Big'), 'Удалиние Префикса'
s = x.removesuffix('Boos'), 'Удалиние Суфикса'


s = s.find("er", 0, 10) ,'Поиск символов в строках | Значение/Начало/Конец | Если значения нет вернет -1'
s = s.rfind('wo', 0, 10), 'Аналог только поиск с правой стороны'

one_line_text = "Textual data in Python is handled with str objects, or strings. \
Strings are immutable sequences of Unicode code points. \
String literals are written in a variety of ways: \
single quotes, double quotes, triple quoted."
one_line_text = ("Textual data in Python is handled with str objects,"
                " or strings. Strings are immutable sequences of Unicode"
                " code points. String literals are written in a variety "
                " of ways: single quotes, double quotes, triple quoted.")

s = 'Hello\nWorld' '\n'     'Перенос на новую стоку'
s = 'Hello\tWorld' '\t'     'Табуляция 4-пробела'
s = 'Hello\rWorld' '\r'     'Возвращение каретки перенос всего теста после\r в начало строки'
s = 'Hello\bWorld' '\b'     'Вывод начинаеться с одного деления в лево и выполняет остаток'
s = 'Hello\'World' '\''     'Добавление сомволов в строку '