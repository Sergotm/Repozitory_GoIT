import re 
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(num:str) -> list:
    pattern_lement = r'[;,\-:!\.\ \(\),\\n,\\t]' # Вказуємо що маємо видалити
    replace = ''
    formatted_number = re.sub(pattern_lement,replace,num) # Удаляємо зайвi символи

    if formatted_number[0] == '0':
        formatted_number = '+38' + formatted_number
        return formatted_number
    
    elif formatted_number[0] == '3':
        formatted_number = '+' + formatted_number
        return formatted_number

    elif formatted_number[0] == '+':
        return formatted_number

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
