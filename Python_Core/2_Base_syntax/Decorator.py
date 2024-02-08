#   Декораторы  ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
typing = 0
def decorator(multiplier: int):

    def dec(func: typing.Callable):
        #Области видимости функции
        global a, b, c, d
        nonlocal multiplier

        if multiplier % 2 == 0:
            multiplier += 1
        
        def wrap(*args, **kwargs):
            for _ in range(multiplier):

                #Генераторы
                yield func(*args, **kwargs)
        return wrap
    return dec

@decorator(10)
def f(num: int)-> int: 
    return num 

qwe = [*f(1)]
print(qwe)
