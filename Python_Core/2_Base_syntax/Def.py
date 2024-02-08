#   Функции ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

'Изменямые возвращение','Int','Str','Float','Tuple'
'Не Изменямые возврашение','List','Dict','Set'
def name (name:str = 'Serhii', age:int=24)-> tuple:
    return name, age

'*args' 'Принимает любое количество параметров в функцию и делает из них кортеж/////////  *args////////'
def main(*args)->str: 
    pass
print(main('hello', ' ', '', 'world','!'))

'**kwargs' 'Принимает любое количество параметров в функцию и делает из них словарь/////////  **kwargs////////'
def prest(**kwargs):
    for key, values in kwargs.items():
        print(f'Key: {key}, Values: {values}')
prest(person_1 = 'Serhii', age_person_1 = 24, person_2 = 'Karina',age_person_2 = 22)
































#    Рекурсия 
def fibonachi(n):
    if n <= 1: # Случайный случай
        return n
    else:
        return fibonachi(n-1)+(n-2) # Рекурсивный случай
print(fibonachi(20))
