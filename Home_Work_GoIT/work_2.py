import random

def get_numbers_ticket(min:int, max:int, quantity:int) -> int:
    try:
        keys_list = []
        while max - min >= quantity:
            num_random = random.randint(min, max)
            keys_list.append(num_random)
            keys_list = list(set(keys_list))
            if len(keys_list) == quantity:
                break
        return keys_list

    except ValueError:
        return keys_list

lottery_numbers = get_numbers_ticket(min=5, max=20, quantity=10)
print(f'Вашi лотерейнi числа: {lottery_numbers} ')


# Тут надо проверку сделать на количество 