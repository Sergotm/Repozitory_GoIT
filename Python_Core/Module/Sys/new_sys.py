from pathlib import Path 
import sys
import os 
def Sys():

    sys.argv - "список аргументів командного рядка, переданих скрипту Python. Елемент argv[0] є ім'ям скрипту, а інші елементи – це додаткові аргументи командного рядка."
    sys.exit() - 'функція виходу з Python. Ви можете передати числовий аргумент, що стане статусом виходу програми. Прийнято, що аргумент 0 означає успішне завершення, а ненульові значення вказують на помилку.'
    sys.path - 'список рядків, який визначає шлях пошуку інтерпретатора для модулів. Ви можете модифікувати цей список, щоб додати власні шляхи для пошуку модулів.'
    sys.version - 'рядок, що містить інформацію про версію Python, яка використовується.'
    sys.platform - "рядок, що вказує на ім'я платформи, на якій виконується Python (наприклад, 'linux' для Linux, 'win32' для Windows)."
    sys.modules - "словник, який містить завантажені модулі. Ключі – це назви модулів, а значення – це об'єкти модулів."
    

def main():
    # print(sys.modules.keys()), 'Вернет список имен загруженых модулей'
    # print(sys.builtin_module_names), 'Получим списко модуей встроеных в Python'
    # print(sys.path)











def madin():
    if len(sys.argv) < 2:
        user_input = ''    
    else:
        user_input = sys.argv[1]
    path = Path(user_input)
    if path.exists():
        if path.is_dir():
            # items = path.iterdir()
            items = path.glob('*.py') #'*.py' найдет все файли py | **/* Найдет все файлы в папках
            for item in items:
                print(item)

        else:
            print(f'{path} is a file ')
    else:
        print(f'{path.absolute()} is not exits')

if __name__ == '__main__':
    main()