from datetime import datetime, timedelta
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

def normalize_phone(phone_number:list) -> list:
    ret_list = []
    # print(phone_number) # Выводим для себя список номеров
    # 1. Цикл будет удалять все лишние знаки в номере
    for element in phone_number:
        pattern_lement = r'[;,\-:!\.\ \(\),\+,\\n,\\t]' # Вказуємо що маємо видалити
        replace = ''
        formatted_number = re.sub(pattern_lement,replace,element) # Удаляємо зайвi символи

        if formatted_number:
            pattern_num = r'38'
            match = re.search(pattern_num,formatted_number,re.IGNORECASE)# Провiряємо перше входження
            if match:
                formatted_number = '+' + formatted_number # Якщо в початку маємо 38 то дадамо тiльки +
                ret_list.append(formatted_number)
            else:
                formatted_number = '+38' + formatted_number # Якщо в початку нема +38 дадаємо його
                ret_list.append(formatted_number)

    return ret_list

sanitized_numbers = normalize_phone(phone_number=raw_numbers)
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

