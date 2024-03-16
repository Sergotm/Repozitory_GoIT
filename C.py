from colorama import Back,Style,Fore


def log_ingo(message):
    print(f'{Fore.BLUE} [INFO] {Fore.RESET} {message}')

def low_warning(message):
    print(f'{Fore.YELLOW} [WARNING] {Fore.RESET} {message}')

def log_error(message):
    print(f'{Fore.RED} [ERROR] {Fore.RESET} {message}')


def color():
    print(Fore.BLUE + 'Тут Голубой цвет')
    print(Back.GREEN + 'Тут зеленый')
    print(Style.RESET_ALL)
    print(f'Тут пройстой текс без изменений')

def k():
    import math
    from C import log_error, log_ingo, low_warning

    def calculate_square_root(numbers):
        for number in numbers:
            try:
                if number < 0:
                    low_warning(f'Мы нашли отриццательное число! {number} Пропускаем')
                    continue
                root = math.sqrt(number)
                log_ingo(f'Квадратный корень {number} - {root:.2f}')
            
            except Exception as w:
                log_error(f'Ошибка при обчислении кореня {number}:{w}')
        
    if __name__ == '__main__':
        numbers = [16, -4, 9, 25, 0, 4, '16']
        calculate_square_root(numbers)