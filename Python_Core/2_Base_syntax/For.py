for _ in range('start','stop','step'):
    break 
else:
    pass

some_list = ["apple", "banana", "cherry"] , 'Перебор списка индекс значение'
for index, value in enumerate(some_list):
    print(index, value)

list1 = ["зелене", "стигла", "червоний"] , 'Перебор 2 и более списков'
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)
