from collections import UserDict,UserList
info = '''Ivanov paper 10
Petrov pens 5
Ivanov marker 3
Ivanov paper 7
Petrov envelope 20
Ivanov envelope 5'''

class Buyer():
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return '\n'.join([f'{key}:{value}'for key, value in self.__dict__.items()])
    
class Buyers(UserList):
    def find(self, name):
        for person in self:
            if name == person.name:
                return person
        else:
            return None
        
    def __str__(self) -> str:
        return '\n\n'.join([str(i) for i in self])

        
        
buyers = Buyers()
for line in info.split('\n'):
    name, product, count = line.split()
    person = buyers.find(name)
    if person is None:
        person = Buyer(name)
        buyers.append(person)
    person.__dict__[product] = person.__dict__.get(product, 0) + int(count)

print(buyers)