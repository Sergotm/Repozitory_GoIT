from collections import UserDict, UserList, UserString
from enum import Enum, auto
class Person:
    name = 'Serhii'
    age = 24
    # (Атрибут класу) ——— це змінна, яка визначена на рівні класу, а не екземпляра класу. 
    # Це означає, що вона спільна для всіх екземплярів цього класу. 
    # Атрибути класу використовуються для зберігання даних, які повинні бути однаковими для всіх об'єктів класу.

    # (Поле класу) ——— (іноді називається "атрибут екземпляра") – це змінна, яка визначена на рівні окремого екземпляра класу..
    # Кожен екземпляр класу має свій власний набір полів, які можуть приймати різні значення для різних екземплярів. 
    # Полем може бути будь-який об'єкт Python. Зазвичай це змінна, або контейнер (словник, список, рядок тощо)
    
    # (Метод класу) ——— це функція, яка оперує з полями класу та/або аргументами, які передаються у метод
'///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'
def class_list():
    class Anaimals:
        def __init__(self, name, age) -> None:
            self.name = name
            self.age = age
            
    class Cat(Anaimals):
        def memo(self):
            return 'Meow'

    class Dog(Anaimals):
        def memo(self):
            return 'Woof'      

    def get_zoo(zoo):
        for animal in zoo:
            print(animal.memo())

    A = [Cat('Barsik', 2),Dog('Sharik', 4)]
    get_zoo(A)

'///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'
class Person:
    count = 0

    def __init__(self):
        self.count = 10

person = Person()
print(person.count) # 10
print(Person.count) # 0

class Person:
    count = 0

Person.count = 10
person = Person()
print(person.count) # 10
'///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'
def test():
    class Pokemon:
        def __init__(self,name,type,health) -> None:
            self.name = name
            self.type = type
            self.health = health

        def attack(self, kerry):
            print(f'{self.name} attaks {kerry.name}!')

        def dodge(self):
            print(f'{self.name} dodged the attaks!')

        def evolve(self,new_form):
            print(f'{self.name} is evoling into {new_form}')
            self.name = new_form

    pikachu = Pokemon(
        name='Pikachu',
        type='Elektric',
        health=100
    )

    pikachu.attack(Pokemon('Charmaned', 'Fire', 100))
    pikachu.dodge()
    pikachu.evolve('Raichu')

def tets():
    class Coins:
        def __init__(self, total_sum) -> None:
            self.coins = (1,2,5,10,25,50)
            self.total_sum = total_sum

        def change(self):
            result = dict()
            item = len(self.coins) - 1
            while item >= 0:
                coin = self.coins[item]
                num_of_coin = self.total_sum // coin
                result[coin] = num_of_coin
                self.total_sum -= coin * num_of_coin
                item -=1
            return result
        
    ins = Coins(185)
    print(ins.change())

    ins_2 = Coins(234)
    # print(ins_2.change())


'//////////////////////////////////////////////////////////////////////////    MyException    //////////////////////////////////////////////////////////////////////////////////////////////////////////////////'

class MyException(Exception):
    def __init__(self,value) -> None:
        self.value = value
        
def too(n:int):
    if n < 0:
        raise MyException(f'Value in {n} and it < 0')
    else:
        return 100
    
# print(too(-5))
'//////////////////////////////////////////////  public  _protected __private     /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'
class A:
    def public(self): # Публічний
        print(f'public')

    def _protected(self):
        print(f'protected')

    def __private(self): # Приватний
        print(f'private')

def pets():
    class Person:
        def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
            self.name = name
            self.age = age
            self._is_active = is_active
            self.__is_admin = is_admin

        def greeting(self):
            return f"Hi {self.name}"

        def is_active(self):
            return self._is_active

        def set_active(self, active: bool):
            self._is_active = active

    p = Person("Boris", 34, True, False)
    print(p._Person__is_admin)

'/////////////////////////////////////////////////     Наслідування MRO          ///////////////////////////////////////////////////////////////////////////////////////////////////////////'

def clon(): # Наслідування
    
    class A: # Наслідування з Ліва на Право / Та з низу в верх
        def hi(self):
            return 'A'
        
    class B(A):
        def hi(self):
            return 'B'
        
    class C(B):
        def hi(self):
            return 'C'

    class D(B,A):
        pass
        
    func = D()
    print(func.hi())

def clon_2():
    class Animal:
        def __init__(self, nickname: str, age: int):
            self.nickname = nickname
            self.age = age

    def make_sound(self):
        pass

    class Bird(Animal):
        def make_sound(self):
            return "Chirp"

    class Parrot(Bird):
        def can_fly(self):
            return True

    class TalkingParrot(Parrot):
        def say_phrase(self, phrase):
            return f"The parrot says: '{phrase}'"

    my_parrot = TalkingParrot("Alice", 2)
    print(my_parrot.make_sound())
    print(my_parrot.can_fly())
    print(my_parrot.say_phrase("Hello, World!"))

    '//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'
    class A:
        name = "Я клас A"

    class B:
        name = "Я клас B"
        property = "Я знаходжусь в класі B"

    class C(A, B):
        property = "Я знаходжусь в класі C"

    c = C()
    print(c.name)
    print(c.property)

'/////////////////////////////////////////////////     SUPER    ///////////////////////////////////////////////////////////////////////////////////////////////////////////'

def super(): #Super class

    class Animals:
        def __init__(self,name,age,vavl) -> None:
            self.name = name
            self.age = age
            self.vavl = vavl

        def get_sound(self):
            pass

    class Dog(Animals):
        def __init__(self, name, age, vavl, breed) -> None:
            super().__init__(name, age, vavl)
            self.breed = breed

        def get_sound(self):
            return 'Woof'
        def get_dog(self):
            return f'Im dog. My name is {self.name} im old. My {self.age} years. Im happy {self.vavl}, and my breed {self.breed}'
        
    my_dog = Dog('Sharik', 2,True, 'Taksa')
    print(my_dog.get_sound())
    print(my_dog.get_dog())

'/////////////////////////////////////////////////     Duck typing    ///////////////////////////////////////////////////////////////////////////////////////////////////////////'
def Duck():
    class Duck:
        def memo(self):
            print("Quack, quack!")

    class Person:
        def memo(self):
            print("I'm Quacking Like a Duck!")

    def item(duckk):
        duckk.memo()

    person = Person()
    duck = Duck()
    item(duck)
    item(person)

Duck()
'//////////////////////////////////////////////////////  User_list / Dict/ String///////////////////////////////////////////////////////////////////////////////////////////////'

def User_list_Dict_String():
    def User_List():
        class My_colections(UserList):
            def add_item(self, item):
                if item not in self.data:
                    self.data.append(item)

        my_class = My_colections([1,2,3,4,5]) # [1, 2, 3, 4, 5]
        my_class.append(6) # [1, 2, 3, 4, 5, 6]
        my_class.add_item(7) # [1, 2, 3, 4, 5, 6, 7]

        class Coutable(UserList):
            def suma(self):
                return sum(map(lambda x: int(x), self.data))

        my_list  = [1,'2',3,4]
        coutable = Coutable(my_list)
        print(coutable.suma())
        coutable.append(5)
        print(coutable.suma())

    def User_Dict():
        contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris.net",
        "phone": "(542) 451-7038",
        "favorite": True,
    }
]
        class Custom_number(UserDict):
            def name_phone(self):
                return f'{self.get("name")}:{self.get("phone")}'

            def email_favo(self):
                return f'{self.get("email")}:{self.get("favorite")}'
            
        customer = [Custom_number(el) for el in contacts]
        print('------------------------')
        for cust in customer:
            print(cust.name_phone())   
        print('------------------------')
        for cust in customer:
            print(cust.email_favo())

        '/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'
        class My_colections(UserDict):
            def add_key(self, key, value):
                self.data[key] = value

        flip = My_colections()
        flip.add_key(1, 'c')
        print(flip)
        '/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'

    def User_String():
        class My_string(UserString):
            def string(self):
                return True if self.data == self.data[::-1] else False

        my_string = My_string('Oko')
        print(f'String: {my_string}')
        print(f'What is string palindrom? {my_string.string()}')

        my_string2 = My_string('NUN')
        print(f'String: {my_string2}')
        print(f'What is string palindrom? {my_string2.string()}')


        class TruncatedString(UserString):
            MAX_LEN = 7

            def truncade(self):
                self.data = self.data[self.MAX_LEN:]

        ts = TruncatedString('My name is Serhii. What is you name?')
        ts.truncade()
        print(ts)

'//////////////////////////////////////////////////////////  dataclasses   ///////////////////////////////////////////////////////////////////////////////////////////////'

def dataclass():
    from dataclasses import dataclass

    @dataclass
    class Rectangle:
        weight: int # Создание класса без конструктора и инициализации аргументов
        wight: int


        def area(self)-> int:
            return self.wight * self.weight
        
    rect_1 = Rectangle(4, 4)
    print(f'Площа прямокутника 1: {rect_1.area()}')
    print(dataclass(rect_1))                                    #Питання

'//////////////////////////////////////////////////////////  Enum Іменованні константи   ///////////////////////////////////////////////////////////////////////////////////////////////'
def Enumerate():
    class OrderStatus(Enum):
        NEW = auto()
        PROCESING = auto()
        SHIPPED = auto()
        DELIVERED = auto()

    class Order:
        def __init__(self, name:str, status:OrderStatus) -> None:
            self.name = name
            self.status = status

        def update_status(self, new_status:OrderStatus):
            self.status = new_status
            print(f"Замовлення '{self.name}' оновленно до статусу {self.status.name}")

        def display_status(self):
            print(f"Статус замолення '{self.name}':{self.status.name}")


    order1 = Order('Laptop', OrderStatus.NEW)
    order2 = Order('Lampa', OrderStatus.NEW)

    order1.display_status()
    order2.display_status()

    order1.update_status(OrderStatus.PROCESING)
    order2.update_status(OrderStatus.SHIPPED)

    order1.display_status()
    order2.display_status()

'//////////////////////////////////////////////////////////  Асоціація Композиція Агрегація  ///////////////////////////////////////////////////////////////////////////////////////////////'

def Asociation_Agregation():
    def Asotiation():
        """
    Асоціація
    Це коли один клас включає інший клас як один з полів. Асоціація описується словом "має".
    Тварина має господаря.

    Виділяють два окремі випадки асоціації: композицію та агрегацію.

    Композиція
    Це коли господар не існує окремо від вихованця.
    Він створюється при створенні вихованця і повністю управляється вихованцем.
    """

        class Animal:
            def __init__(self, nickname, age):
                self.nickname = nickname
                self.age = age

            def info(self):
                return f"It's animal with name: {self.nickname}, age: {self.age}"

        class Owner:
            def __init__(self, name, phone):
                self.name = name
                self.phone = phone

            def info(self):
                return f"It's owner with name: {self.name}"

        class Cat(Animal):
            def __init__(self, nickname, age, name, phone):
                super().__init__(nickname, age)
                self.owner = Owner(name, phone)  # Композиція

            def sound(self):
                return 'SOUND'


        cat = Cat('Bob', 4, 'Vova', '123-456-7890')
        print(cat.owner.info())
        print(cat.owner.name)
        print(cat.owner.phone)

    def Agregation():
        """
Агрегація
Це коли екземпляр господаря створюється десь в іншому місці коду,
і передається в конструктор вихованця як параметр
"""


        class Animal:
            def __init__(self, nickname, age):
                self.nickname = nickname
                self.age = age

            def info(self):
                return f"It's animal with name: {self.nickname}, age: {self.age}"


        class Owner:
            def __init__(self, name, phone):
                self.name = name
                self.phone = phone

            def info(self):
                return f"It's owner with name: {self.name}"


        class Cat(Animal):
            def __init__(self, nickname, age, owner: Owner):
                super().__init__(nickname, age)
                self.owner = owner

            def sound(self):
                return 'SOUND'


        owner = Owner('Vova', '0951111111')
        print(owner.name)
        print(owner.phone)
        print(owner.info())

        cat = Cat('Bob', 4, owner)
        print(cat.owner.info())
        print(cat.owner.name)
        print(cat.owner.phone)