#   Исключения и их обработка  ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
SyntaxError, 'синтаксична помилка.'
IndentationError, 'помилка, яка виникає, якщо у виділенні блоків інструкцій пробілами допущена помилка.'
TabError, 'виникає, якщо в одному файлі використовувати пробіли i табуляції для виділення блоків інструкцій.'
TypeError, 'виникає, коли операція зі змінною цього типу неможлива.'
ValueError, 'виникає, коли тип операнда відповідний, але значення таке, що операцію неможливо виконати.'
ZeroDivisionError,  'Деленине на ноль'
KeyError, 'Отсутствие ключа в словаре'
NotImplementedError, ''
try:
    result = 10 / 0
    # print(result)
except Exception as x:
    # print(x)
    pass
else:
    # print(f'Ты меня всеравно увидишь если не будет ошибки')
    pass
finally:
    # print(f'Я буду всегда')
    pass


"...............................................Власні Винятки ....................................................................................."


class AgeVerificationError(Exception):
    # messages = 'Вік не задовольняє потреби вимоги'
    def __init__(self, messages) -> None:
        self.messages = messages
        super().__init__(self.messages)
    
def verify_age(age):
    if age < 18:
        raise AgeVerificationError('Вік не задовольняє потреби вимоги')
    
    
if __name__ == '__main__':
    try:
        verify_age(3)
    except AgeVerificationError as my_err:
        print(f'Виникла помилка {my_err}')
        

        

