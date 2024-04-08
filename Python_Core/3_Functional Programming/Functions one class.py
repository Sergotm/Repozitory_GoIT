from typing import Callable
from functools import wraps
import math

Debug = False
def function(): # Функция первого Класса
    def get_sum(a, b):
        if Debug == True:
            print(f'Тут возврат func get_sum: a*b = {a * b}')
        else:
            return a * b # 12
    res = get_sum
    def get_mull(a, b, func):
        c = a + b # 6
        s = a - b # 2
        if Debug == True:
            print(f'Тут возврат func get_mull: C={c}, S={s}')
        else:
            return func(c,s)

    f = get_mull
    f(4,2,res)
        
    new_dict = {
        'name':'Serhii',
        'age':'24',
        'func': res,
        'fun': f
    }
    print(f'{new_dict["func"](10, 4)}')
    print(f'{new_dict["fun"](4,2,res)}')
    '////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'

    def add(a: int, b: int) -> int:
        return a + b

    def multiply(a: int, b: int) -> int:
        return a * b

    def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
        return operation(a, b)

    # Використання
    result_add = apply_operation(5, 3, add)
    result_multiply = apply_operation(5, 3, multiply)

    print(result_add, result_multiply)

def closure(): # Замикання
    def greeting(name):# зовнишня
        def massage(msg): # В
            return f'{name} - {msg}'
    
        return massage # Возвращаем внуттеннию функ

    msg_for_greaating = greeting('Denys')
    msg_for_greaating_2 = greeting('Ola')
    msg_for_greaating_3 = greeting(2)

    print(msg_for_greaating('Go to lesson'))
    print(msg_for_greaating_2('Go to School'))
    print(msg_for_greaating_3(3))

    def get_cache():
        cahce = {}
        def inner(n):
            if n not in cahce:
                cahce[n] = sum([i for i in range(1, n+1)])
                print(f'Hard word: {n}')
                return cahce[n]
            else:
                print(f'Easy work: {n}')
                return cahce[n]
        return inner
    calc = get_cache()
    print(calc(5))
    print(calc(3))
    print(calc(3))
    print(calc(8))
    '////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'

    def counter() -> Callable[[], int]: # посчет вывовов функции
        count = 0

        def increment() -> int:
            # використовуємо nonlocal, щоб змінити змінну в замиканні
            nonlocal count  
            count += 1
            return count

        return increment

        # Створення лічильника
        count_calls = counter()

        # Виклики лічильника
        print(count_calls())  # Виведе 1
        print(count_calls())  # Виведе 2
        print(count_calls())  # Виведе 3

def currying(): # Currying 
    def greeting_simple(name:str, msg:str):
        return f'{name} - {msg}'
    
    def gretting(name:str): #Розбиваем 1 функ на 2 маленьких с помощю замыкания
        def simple(msg:str): #  Чтоб каждая функ имела 1 *args
            return f'{name} - {msg}'
        return simple
    
    a = gretting('Serhii')
    print(a('Hello'))
    '////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'
    def greeting_simple(name, msg):
        return f'{name} - {msg}'

    b = greeting_simple('Hanna', 'Hello')

    def gretting(name):
        def simple(msg):
            return f'{name} - {msg}'
        return simple

    a = gretting('Hanna')
    text = a('Hello')
    print(text)
    '////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'
    def hello_male(name):
        print(f'Mr. {name}')

    def hello_female(name):
        print(f'Mrs. {name}')

    def hello_pan(name):
        print(f'Hello Pan: {name}')

    MODES = {
        'm':hello_male,
        'f':hello_female,
        'pan': hello_pan,
    }

    def gretting(mode):
        return MODES[mode]


    def main():
        mr = gretting('m')
        mrs = gretting('f')
        pan = gretting('pan')

        mr('Vlad')
        mrs('Olena')
        pan('Taras')
    
def decorator(x, y): # Decorator
    def get_logger(func):
        @wraps(func) #@wraps используеться для сохранения данных а не их копирования
        def inner_loger(a, b):
            print(f'Start fucn {func.__name__}')
            result = func(a, b)
            print(f'Stop func {func.__name__}')
            return result
        return inner_loger

    @get_logger
    def complicated(x: int, y: int) -> int:
        return x + y 
    # complicated = get_logger(complicated)
    print(complicated(2, 3))
    
def comprehensions(x): # Dict Set List comprehensions
    # s = []
    # for i in range(x):
    #     num = i ** 2 
    #     if not num % 2:
    #         s.append(num)
    # print(s)

    l = [el ** 2 for el in range(x) if not el % 2], 'List'
    s = {i ** 2 for i in range(x) if not i % 2}, 'Set'
    d = {a: a ** 2 for a in range(x) if not a % 2}, 'Dict'
    print(d, type(d))

    names = ['dan', 'stiv', 'jane']
    def normalize(name):
        s = [el.title() for el in names]
        return s
    print(normalize(names))
    #3
    new_name = (lambda name: name.title(), names)
    print(list(new_name)) 
    #4 
    new_name = [name.title() for name in names]
    print(list(new_name))   

    user = ['pawel', 'oksana', 'karina']
    user = [x.title() for x in user]
    user_dict = {i[0]: i for i in user}
    check = { i:i**2 for i in range(1, 10)}

    num_1 = [1, 3, 5]
    num_2 = [2, 4, 6]
    wrap = [x + y for x, y in zip(num_1, num_2)] #Аналог чтобы пройтерироваться по 2 и болие списков одновременно 
    print(wrap)

def lambda_f(): # Lambda Ананомная функция автоматически возвращает вычисление
    def radius(d):
        result = d * math.pi
        return result
    print(radius(2))

    new = lambda d: d * math.pi
    print(new(2))
    

    new = [el % 2 for el in range(1,10)]
    print(*new) #*new распаковка списка

    '///////////////////////////////////////////////////////////////   map      /////////////////////////////////////////////////////'
    w = [1,2,3,4,5,6,7,8,9]
    result = map(lambda el : el % 2, w)
    print(*result) # *result распакаовка списка 

    num_1 = [1, 3, 5] # Можно итерироваться по 2 и болие списков
    num_2 = [2, 4, 6]
    pack = map(lambda x, y: x + y, num_1, num_2)
    num_list = [x for x in pack]
    print(num_list)

    '////////////////////////////////////////////////////////////    filter    ////////////////////////////////////////////////////////'
    result = filter(lambda value: value % 2, w)
    print(list(result))

    '////////////////////////////////////////////////////////////    any    ////////////////////////////////////////////////////////'
    nums = [0, False, 5, 0] # Вернет True если хоть один елемент будет истинный
    result = any(nums)  
    print(result)



    '////////////////////////////////////////////////////////////    all    ////////////////////////////////////////////////////////'
    nums = [1, 2, 3, 4] # Вернет True если все елементы будут истинные
    is_all_even = all(x % 2 == 0 for x in nums) 
    print(is_all_even)



if __name__ == '__main__':
    lambda_f()