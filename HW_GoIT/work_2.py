import random

def get_numbers_ticket(min:int, max:int, quantity:int)->int:
    keys_list = []
    for _ in range(quantity):
        num_random = random.randint(min, max)
        keys_list.append(num_random)
    
    get_lottery_num = list(set(keys_list))
    get_lottery_num.sort()

    if len(get_lottery_num) == 10:
        return get_lottery_num
    else:
        keys_list.clear()
        return keys_list


lottery_numbers = get_numbers_ticket(min=1,max=1000,quantity=10)
print(f'Вашi лотерейнi числа: {lottery_numbers} ')



