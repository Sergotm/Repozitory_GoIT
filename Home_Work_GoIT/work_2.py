import random

def get_numbers_ticket(min:int, max:int, quantity:int) -> int:
    try:
        keys_list = []
        while len(keys_list) <= quantity-1:
            num_random = random.randint(min, max)
            keys_list.append(num_random)
            keys_list = list(set(keys_list))
        return keys_list

    except ValueError:
        return keys_list

lottery_numbers = get_numbers_ticket(min=2, max=20, quantity=10)
print(f'Вашi лотерейнi числа: {lottery_numbers} ')


