from random import randint
'''
(Статичні методи) використовують декоратор @staticmethod і є методами, які не мають доступу до екземпляру класу тобто змінної self, з якого вони були викликані. 
Це означає, що статичні методи не можуть змінювати стан об'єкта або класу, але вони можуть бути корисними для виконання деяких операцій, які не залежать від стану об'єкта. 
Статичні методи можна розглядати як "допоміжні" функції, які мають логічний зв'язок із класом, але не потребують доступу до його атрибутів або методів.

(Класові методи) використовують декоратор @classmethod і, на відміну від статичних методів, мають доступ до самого класу через параметр cls, який автоматично передається Python. 
Це означає, що класові методи можуть змінювати стан класу або викликати інші класові методи. 
Класові методи часто використовуються для фабричних методів, які створюють екземпляри класу, використовуючи різні способи ініціалізації, ніж стандартний конструктор.
'''
def A1():
    class Test:
        def doubler(self, x): # self == test
            print('Mul on 2')
            return  x * 2 
        
        @classmethod
        def triples(cls, x): # cls == class
            print('Mul on 3')
            return  x * 3
        
        @staticmethod
        def quad(x): # Не можно использовать self внутри
            print('Mul on 4')
            return  x * 4 
        
    test = Test()
    print('---Екземпляр класу---')
    # print(test.doubler(4))
    # print(test.triples(4))
    # print(test.quad(4))

def A2(): # staticmethod
    class Geometry:
        PI = 3.14
        @staticmethod
        def my_func(radius):
            return Geometry.PI * radius * 2
        
    print(Geometry.my_func(3))

def A3(): #classmethod
    class Employye:
        def __init__(self, name, position) -> None:
            self.name = name
            self.position = position

        @classmethod
        def from_pothition(cls, value):
            for el in list(range(1,10)):
                if el == value:
                    return f'BINGO'
                else:
                    return f'FAUL'

    print(Employye.from_pothition(randint(1,10)))

A3()