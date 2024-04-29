'/////////////////////////////////////////////////////////////////     Принципи проектування SOLID     ///////////////////////////////// //////////////////////////////////////////////////////'

'Single responsibility — принцип єдиної відповідальності'   # TODO (Кожен клас виконує щось одне)
'Open-closed — принцип відкритості / закритості'            # TODO (Код відкритий для розширення, але закритий для змін)
'Liskov substitution — принцип підстановки Барбари Лісков'  # TODO (Побудові ієрархії наслідування класів)
'Interface segregation — принцип розділення інтерфейсу'     # TODO (Принцип розділення інтерфейсу)
'Dependency inversion — принцип інверсії залежностей'       # TODO ()



'//////////////////////////////////////////////////   S    (Кожен клас виконує щось одне)    /////////////////////////////////////////////////////////////////////'

class PersonAddres:
    def __init__(self,zip, city, street):
        self.zip = zip
        self.city = city
        self.street = street

    def get_address(self):
        return f'{self.zip}, {self.city}, {self.street}'

class Person:
    def __init__(self, name, addres:PersonAddres) -> None:
        self.name = name
        self.addres = addres

    def voice(self):
        return f'{self.name}:{self.addres.get_address()}'

person = Person('Alexander', PersonAddres('36007', 'Poltava', 'European, 28'))
# print(person.voice())
'......................................................................................................................................................'
class PersonInfo:
    def voice(self):
        raise NotImplementedError

class PersonAddres(PersonInfo):
    def __init__(self, zip:str, city:str, stret:str):
        self.zip = zip        
        self.city = city
        self.stret = stret

    def voice(self):
        return f'{self.city}: {self.stret}: zip:{self.zip}'

class PersonPhone(PersonInfo):
    def __init__(self, operator:str, number:str):
        self.operator = operator
        self.number = number

    def voice(self):
        return f'+380({self.operator}){self.number}'
    
class Person:
    def __init__(self, name:str, age:str, phone:PersonInfo, addres: PersonInfo):
        self.name = name
        self.age = age
        self.phone = phone
        self.addres = addres

    def get_phone_number(self):
        return f'{self.name}, {self.phone.voice()}'
    
    def get_addres(self):
        return f'{self.name}, {self.addres.voice()}'

user_addres = PersonAddres(zip='54-130', city='Wroclaw', stret='Maslicka 177' )
user_phone = PersonPhone(operator='50', number='981021588')

person = Person(name='Serhii',age='24', addres=user_addres, phone=user_phone)
# print(person.get_addres())
# print(person.get_phone_number())

'/////////////////////////////////////////////////   O   (Код відкритий для розширення, але закритий для змін)   ////////////////////////////////////'
from math import pi
class Shape:
    def voice(self):
        raise NotImplementedError

class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def voice(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def voice(self):
        return self.radius ** 2 * pi

class Square(Shape):
    def __init__(self, sharps) -> None:
        self.sharps = sharps
    
    def voice(self):
        return self.sharps ** 2
        
class AreaCalculator:
    def __init__(self, shapes: list[Shape]):
        self.shapes = shapes

    def total_area(self) -> float:
        sum = 0
        for shape in self.shapes:
            sum += shape.voice()
        return sum

if __name__ == '__main__':
    ar_sh = AreaCalculator([Rect(10, 10), Rect(4, 5), Circle(20), Square(3)])
    area = ar_sh.total_area()
    # print(area)
'......................................................................................................................................................'
import json
from pathlib import Path
import yaml

class Storage:
    def voice(self):
        raise NotImplementedError
    
class JSONStorage(Storage):
    def __init__(self, filename):
        self.filename = filename
    
    def get_value(self, key):
        with open(self.filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data.get(key)

class YAMLStrorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def get_value(self, key):
        with open(self.filename, 'r', encoding='utf-8') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            return data.get(key)

json_storage = JSONStorage(Path('Python_Web\\SOLID\\data.json'))
# print(json_storage.get_value('name'))
yaml_storage = YAMLStrorage(Path('Python_Web\\SOLID\\data.json'))
# print(yaml_storage.get_value('id'))
'////////////////////////////////////////////////////  L    (Побудові ієрархії наслідування класів)    /////////////////////////////////////////////'
from abc import ABC, abstractmethod

class Engine:
    @abstractmethod
    def start(self):
        pass

class GazEngine(Engine):
    def start(self):
        return f'GazEngine start'
    
class ElectricEngine(Engine):
    def start(self):
        return f'ElectricEngine start'

# Автомобілі
class Car(ABC):
    def __init__(self, engine: Engine):
        self.engine = engine

    @abstractmethod
    def start(self):
        pass

class ElectricCar(Car):
    def start(self):
        return f"Electric car: {self.engine.start()}\n{'_'*35}"
        
class GazCar(Car):
    def start(self):
        return f"Gaz car: {self.engine.start()}\n{'_'*35}"

gaz_en = GazEngine()
el_en = ElectricEngine()

volvo = GazCar(gaz_en)
tesla = ElectricCar(el_en)

# print(volvo.start())
# print(tesla.start())
'/////////////////////////////////////////////////////    I  (Принцип розділення інтерфейсу)  /////////////////////////////////////////////////////////////////////////////////'
# TODO Сутності не повинні залежати від інтерфейсів, які вони не використовують.

from abc import ABC, abstractmethod

class Print(ABC):
    @abstractmethod
    def print(self, dokument):
        pass

class Skan(ABC):
    @abstractmethod
    def skan(self, dokument):
        pass
class Fax(ABC):
    @abstractmethod
    def fax(self, dokument):
        pass

class OLDPrinter(Print):
    def print(self, dokument):
        pass
'...........................................................................................................'
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Man(Workable, Eatable):
    def work(self):
        return "Working hard."

    def eat(self):
        return "Eating lunch."

class Robot(Workable):
    def work(self):
        return "Working automatically."
'//////////////////////////////////////////////////////////////    D    /////////////////////////////////////////////////////////////////////////////////'