from collections import namedtuple

person_1 = ('Bob', 30, 'Kyiv')
print(f'Simple tuple: Name {person_1[0]} Age {person_1[1]} City {person_1[2]}')


Persons = namedtuple('Person', ['name', 'age', 'city'])
person_2 = Persons('Nike', 40, 'Lviv')
person_3 = Persons('Olena', 27, 'Odessa')
print(f'Named Tuple: Name {person_2.name} Age {person_3[1]} City {person_2.city}')