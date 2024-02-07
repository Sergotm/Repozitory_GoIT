'''Основные струкруты данных'''

#   1.  Как создать / изменить / удалить
#   2.  Изменяемые / не изменяемые обьекты
#   3.  Основные методы базовых структур

#    Строки Str  /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# По умолчанию применяеться кодировка UTF-8
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

#...
#    Список List /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
b = []
c = []
a = [1, 2, 3, 4, 5, b, c] 
a = list()
a = [1] * 10
a = [*a]
a.append(5), 'Добавление в конец списка'
a.insert(1, True), 'Добавление по индексу'  
a.sort(), 'Сортирует список'
a.sort(reverse=True), 'Сортирует список, в порядке убывания'
a.remove('Hello'), 'Удаляет указаное значение'
a.pop(1), 'Удаляет по индексу'
a.extend(), 'Добавление (списка в список). В конец. Или соидинение (списка з списоком).'
a.reverse(), 'Обратный порядок'
a.clear(), 'Очисчает список'
a = sum(a), 'Сумма списка'
a = list(set(a)), 'Удаление повторяющихся елементов. Список -> Множество -> Cписок'
q = a.index(f'1'), 'Поиск индекса по значению'
a[3:5], a[0::3], 'Срезы' / 'Вывод каждый 3 символ'
#...

#   Кортежы Tuple ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
b = (1, 2), 'Создание Tuple'
b = tuple([1, 2])
b = b[:] , 'Срезы' / 'Вывод всего'
new_list = tuple(set(a)) , 'Удаление повторяющихся елементов. Кортеж -> Множество -> Кортеж'

#...

#   Множество Set //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
c = {1, 2}, 'Создание множества'
d = set({1, 2}), 'Создание множества без повторений'
d_lst = set(a) , 'Удаление дупликатов значений'
c.add(3) , 'Добавление значений в Множество'
c.remove(3), 'Удаялет указаное значение, если его нет Выдает ошибку'
c.discard(2) , 'Удаялет указаное значение, если его нет НЕ выдает ошибку'
c.update({None, }), ''
_ = c - d , 'Разница между двумя Множествами включает которые есть в 1 но нету в 2 '
c = a.difference(b), ' Аналог ⬆'
_ = c ^ b , 'Симетричная разница. Включает елементы котрые есть в 1 и нету в другой. И наоборот'
c = a.symmetric_difference(b) , 'Аналог ⬆'
_ = c | d , 'Соединение двух Множест без дупликатов' 
c = a.union(b), 'Аналог ⬆'
_ = c & d , 'Пересечение двух множеств'
_ = a.intersection(b), 'Аналог ⬆'
_ = frozenset(c) , 'Не изменяемое Множество. Но можно делать вычесление - ^ | & '
#...

#   Словарь Dict ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
d = dict(none123 = None)

for key, value in c.items():
    print(f'Ключ: {key} / Значение: {value}') , 'Перебор Ключ Значение Словаря'

d = {None: None, **d}
d['Ключ'] = 'Значение' ,'Изменение/Добавление: значение по ключу'
key_ixists = "name" in 'person',    'Проверка есть ли ключ в Словаре'
d = d | {2: 2}
_ = d.setdefault(3, 3)
a = d.pop('age') , 'Удалит Ключ\Знач и вернет в переменную значение' 
d.popitem(), ' Удалит последний ключ значение'
a = d.copy() ,'Делает копию словаря без изменений исходного'
d.items() , 'возвращает объект представления, который отображает список пар кортежей словаря dict  / можно перебрать словарь в цикле for '
d.keys(),   'Вывод всех ключей'
d.values(),    'Вывод всех значений Словаря'
age = a.get("age"), 'Безопасное получение значение, в случаи отсутствия ключа получим None '
name = a["name"], ' Не безопасное возвраащине значения, в случаи отсутствия ключа получим Error'

New_dict = { 'Вытягивание значения с словаря в список '
    'koles': [1,2,3] }
new = New_dict.pop('koles')
print(new[1])
#...