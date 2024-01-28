New_dict = {
    'Age': 24,
    'Name': 'Serhii',
    'koles': [1,2,3]     
}
Do_dict = {
    'city':'Poland',
    'name':'Karina',
    'Name':'SERHII'
}
for key, value in New_dict.items():
    if key != 'koles':
       print(f'Ключ: {key} / Значение: {value}')
    else:
       break
