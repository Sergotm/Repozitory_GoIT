#   Строки String ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
s = str
s = '' ,' Одинарные кавычки'
s = " ", ' Двойные кавычки'
s = ''' ''', 'Тройные для длинного текста со смещением'
s = "hello"
s.upper() , 's -> S  Перевод всего в большой регистр'
s.lower() , 'S -> s  Перевод всего в малый регистр'
s.isupper() , ''
s.islower() , ''
s = s.startswith('hello') , 'Проверка начала строки. Вернет True/False'
s = 'image.png'
s = s.endswith('.png') , 'Проверка конца строки. Вернет True/False'
s = 'yes'.capitalize() , 'Сделает первую букву Yes Большой остальные маленькими'
s = 'my name'.title() , ' Сделает каждую первую букву каждого слова в строке Большой остальные маленькими -> My Name'
s = "456".isdigit() , 'Проверяет создана ли строка только с Цифр. Вернет True/False'
s = "Kokos".isalpha(), 'Проверяет создана ли строка только с Букв. Вернет True/False'
s = " ".isspace() , 'Проверяет создана ли строка только с Пробелов. Вернет True/False'

one_line_text = "Textual data in Python is handled with str objects, or strings. \
Strings are immutable sequences of Unicode code points. \
String literals are written in a variety of ways: \
single quotes, double quotes, triple quoted."