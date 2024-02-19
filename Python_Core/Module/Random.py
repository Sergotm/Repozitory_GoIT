import random

ran_number = random.randint(4,7), 'Возвращает случайное число из указано диапазона'
# print(ran_number)

len_pi = random.random(), 'Он генерирует случайное число между (0) и (1)'
# print(len_pi)

by_py = random.randrange(1,10,2), 'Start,stop,step'
# print(by_py)

ny_list = ['list','tuple','dict','range']
random.shuffle(ny_list) , 'Перемешиваем список'
# print(f'{ny_list}')

new_value = random.choice(ny_list)
# print(f'{new_value}')
weights = [1,1,1,1] , 'Вероятность выпадения'
new_choices = random.choices(population=ny_list, weights=weights,k=3) 
# print(f'{new_choices}')

one_sample = random.sample(population=ny_list, k=3), 'Аналог choices только выбор значений без повторений'
# print(one_sample)

patern = random.uniform(a=14,b=56) ,'Метод повертає випадкове дійсне число N, таке що a <= N <= b.'
# print(patern)


