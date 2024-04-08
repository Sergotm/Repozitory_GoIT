from collections import UserDict,UserList,UserString
def __init__(): #Магічний Метод __init__
    class Evolution():
        def __init__(self, name:str, age:int = 0) -> None:
            
            self.name = name
            self.age = age
            self.is_adult = self.__check_adulthood()

            print(f'Створено Human: {self.name}, Вік: {self.age}, Дорослий{self.is_adult}')

        def say_hello(self):
            return f'Hello! I am {self.name}'
        
        def __check_adulthood(self):
            return self.age >= 18

        
    bill = Evolution('Bill', 19)
    print(bill.say_hello())
    print(f'Вік: {bill.age}, Дорослий: {bill.is_adult}')

    jyle = Evolution('Jyne')
    print(jyle.say_hello())
    print(f'Вік: {bill.age}, Дорослий: {bill.is_adult}')


def __repr__1__str__(): # Магічний метод __repr__ | __str__
    class Point:
        def __init__(self, x:int, y:int):
            self.x = x
            self.y = y

        def __repr__(self) -> str:
            return f'REPR Point(x={self.x}, y={self.y})'
        
        def __str__(self) -> str: # Приорітет перед __repr__
            return f'STR Point(x={self.x}, y={self.y})'
        
    point = Point(2, 3)
    # print(repr(point))
    print(point)
    '////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'
    class Car: 
        store_name = 'GoIT2023'

        def __init__(self, color, model, marka, year ) -> None:
            self.color = color
            self.model = model
            self.year = year
            self.marka = marka

        def __repr__(self) -> str:
            return f"'{self.marka}','{self.model}','{self.color}','{self.year}'" # ',' для eval создание отдельных обьектов
        
        def __str__(self) -> str: # Приорітет перед __repr__
            return f"{self.marka}{self.model}"
    
    car_obj = Car(color='Black', model='Model X',marka='Tesla' , year=2023)
    print(car_obj)
    # print(repr(car_obj))

    # capy_obj = eval(repr(car_obj))
    # print(capy_obj[1])
            

def __getitem__1__setitem(): # Методи __getitem__ __setitem__
    def A1():
        class SimpleDict:
            def __init__(self):
                self.data = {}

            def __getitem__(self, key): # Витягуємо значення по індексу або по ключу
                return self.data.get(key, 'Key not found')
            
            def __setitem__(self, key, value): # Добаляемо нове (Ключ - Значення) 
                self.data[key] = value
            
        simple = SimpleDict()
        simple['name'] = 'Boris'
        print(simple['name'])
        simple.__setitem__('age',24)
        print(simple['age'])
        
    def A2(): # Струкрута керування температурою в примищенні 
        class BoundedList:
            def __init__(self, min_value:int, max_value:int) -> None:
                self.min_value = min_value
                self.max_value = max_value
                self.__data = []

            def __getitem__(self, index:int):
                return self.__data[index]

            def __setitem__(self, index:int, value:int):
                if not (self.min_value <= value <= self.max_value):
                    raise ValueError(f'Value {value} must be betwen {self.min_value} and {self.max_value}')
                if index >= len(self.__data):
                    #Додаємо новий елемент
                    self.__data.append(value)
                else:
                    self.__data[index] = value

            def __repr__(self) -> str:
                return f'BoundedList({self.max_value}, {self.min_value})'
            
            def __str__(self) -> str:
                return str(self.__data)
            
        temperatures = BoundedList(18, 26)
        for i, el in enumerate([20, 22, 25, 27]):
            try:
                temperatures[i] = el
            except ValueError as Er:
                print(Er)
        print(temperatures)
    def A3(): # Струкрута керування температурою в примищенні 
        from collections import UserList
        class BoundedList(UserList):
            def __init__(self, min_value:int, max_value:int,initial_list = None) -> None:
                super().__init__(initial_list if initial_list is not None else [] )
                self.min_value = min_value
                self.max_value = max_value
                self.__validate_list()

            def __validate_list(self):
                for item in self.data:
                    self.__validate_item(item)

            def __validate_item(self, item):
                if not (self.min_value <= item <= self.max_value):
                    raise ValueError(f'Item {item} must be betwen {self.min_value} and {self.max_value}')

            def append(self, item):
                self.__validate_item(item)
                super().append(item)

            # def insert(self, i, item):
            #     self.__validate_item(item)
            #     super().append(item)

            # def __setitem__(self, i, item):
            #     self.__validate_item(item)
            #     super().__setitem__(item)

            def __repr__(self):
                return f'BoundedList({self.max_value},{self.min_value})'

            def __str__(self):
                return str(self.data)


        if __name__ == '__main__':
            temperatures = BoundedList(18, 26,[19, 21, 22])
            print(temperatures)

            for el in [20,22,25,27]:
                try:
                    temperatures.append(el)
                except ValueError as er:
                    print(er)

            print(temperatures)


def __Mag_Met__():# Магічні методи
    class Car:
        def __init__(self, color, model, marka, year, price) -> None:
            self.color = color
            self.model = model
            self.year = year
            self.marka = marka
            self.price = price
            
        #'........................................................... Математичні магічні методи .....................................................'
        def __add__(self, other): # для оператора +
            return self.price + other.price
        
        def __sub__(self, other): # для оператора -
            return self.price - other.price
        
        def __mul__(self, other): # для оператора *
            return self.price * other.price
        
        def __truediv__(self, other): # для оператора /
            return self.price / other.price
        
        def __floordiv__(self, other): # для оператора цілочисельного ділення //
            return self.price // other.price
        
        def __mod__(self, other): # для оператора залишку від ділення %
            return self.price % other.price
        
        def __pow__(self, other): # для оператора * піднесення до степеня
            return self.price ** other.price
        
            
        #'........................................................... Порівняльні магічні методи .....................................................'
        def __repr__(self) -> str:
            return f'"{self.color}", "{self.model}", "{self.marka}", "{self.year}"'
        
        def __str__(self) -> str:
            return f'{self.marka}, {self.model}'
        
        def __eq__(self, other): # == По чому будемо порівнювати Класи
            return self.price == other.price
        
        def __ne__(self, other): # для оператора !=
            return self.price != other.price

        def __lt__(self, other): # для оператора <
            return self.year == other.price
        
        def __gt__(self, other): # для оператора >
            return self.price == other.price
        
        def __le__(self, other): # для оператора <=
            return self.year == other.price
        
        def __ge__(self, other): # для оператора >=
            return self.year == other.price
        
    car_BMW = Car(color='Balck', model='BMW', marka='X5',year=2024,price=15000)
    car_AUDI = Car(color='White', model='AUDI', marka='A6',year=2023,price=15000)
    print(car_BMW == car_AUDI)
    print(car_BMW > car_AUDI)
    print(car_BMW != car_AUDI)
        
def __call__():# Функтори
    '''Функтори в Python — це об'єкти класів, які можуть бути викликані як функції. 
    Це досягається за допомогою реалізації спеціального магічного методу __call__ для класу. 
    Коли ви додаєте метод __call__ до класу, екземпляри цього класу можуть бути викликані звичайні функції.'''
    def A1():
        class Mutiplayer:
            def __init__(self, functor) -> None:
                self.functor = functor

            def __call__(self,other):
                return self.functor * other 
            
        by = Mutiplayer(5)
        fy = Mutiplayer(2)

        print(by(2))
        print(fy(2))

    def A2():
        class Count:
            def __init__(self, init_factor) -> None:
                self.factor = init_factor

            def __call__(self,*args, **kwargs):
                inc, = args
                self.factor += inc
        
        num = Count(10)
        num(5)
        num(20)
        print(num.factor)

    def A3():
        class Cafe:
            def __init__(self) -> None:
                self.menu = {
                    'kava':25,
                    'hert':15,
                    'kakao':30,
                    'late':35
                }
                self.orders = []
            def __call__(self, item, quantity:int = 1):
                if item in self.menu:
                    total_price = self.menu[item] * quantity
                    self.orders.append((item, quantity, total_price))
                    print(f'Замовленно {quantity} {item}. Загальна вартість: {total_price}')
                else:
                    print (f'Такого товару {item} немає')

            def show_orders(self):
                if self.orders:
                    print(f'Ваші замовлення')
                    for order in self.orders:
                        print(f'{order[1]} * {order[0]} - {order[2]} грн.')
                else:
                    print(f'Замовлення не зробленно')
                
        user = Cafe()
        # user('kava', 2)
        # user('gogo', 3)
        # user('late')
        user.show_orders()
    
    def A4(): #Функтор зі станом 
        class Counter:
            def __init__(self):
                self.count = 0

            def __call__(self, *args, **kwargs):
                self.count +=1
        counter = Counter()
        counter()
        counter()
        print(f'Викликоно {counter.count} разів')
    
    def A5():
        class Fuctor:
            def __init__(self, operetion: str = 'add') -> None:
                self.operetion = operetion

            def __call__(self, a, b):
                if self.operetion == 'add':
                    return a + b
                elif self.operetion == 'mul':
                    return a - b
                else:
                    raise ValueError('Error object')
                
        functor = Fuctor()
        print(functor(5,5))
        functor = Fuctor('mul')
        print(functor(5,3))
        
def __iter__next__():
    def A1():
        pass
    A1()
__iter__next__() 
def Приклади():
    def A1(): #__add__ __sub__
        class MyDict(UserDict):
            def __add__(self, other):
                temp_dict = self.data.copy()
                temp_dict.update(other)
                return MyDict(temp_dict)

            def __sub__(self, other):
                temp_dict = self.data.copy()
                for key in other:
                    if key in temp_dict:
                        temp_dict.pop(key)
                return MyDict(temp_dict)

        if __name__ == '__main__':
            d1 = MyDict({1: 'a', 2: 'b'})
            d2 = MyDict({3: 'c', 4: 'd'})

            d3 = d1 + d2 # d1=self d2=other
            print(d3)

            d4 = d3 - d2 
            print(d4)
    def A2(): #__add__ __sub__ __mul__
        class ComplexNumber:
            def __init__(self, real, imag):
                self.real = real
                self.imag = imag

            def __add__(self, other):
                return ComplexNumber(self.real + other.real, self.imag + other.imag)

            def __sub__(self, other):
                return ComplexNumber(self.real - other.real, self.imag - other.imag)

            def __mul__(self, other):
                real_part = self.real * other.real - self.imag * other.imag
                imag_part = self.real * other.imag + self.imag * other.real
                return ComplexNumber(real_part, imag_part)

            def __str__(self):
                return f"{self.real} + {self.imag}i"

        if __name__ == "__main__":
            num1 = ComplexNumber(1, 2)
            num2 = ComplexNumber(3, 4)
            print(f"Сума: {num1 + num2}")
            print(f"Різниця: {num1 - num2}")
            print(f"Добуток: {num1 * num2}")