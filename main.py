def prest(**kwargs):
    for key, values in kwargs.items():
        print(f'Key: {key}, Values: {values}')
prest(person_1 = 'Serhii', age_person_1 = 24, person_2 = 'Karina',age_person_2 = 22)