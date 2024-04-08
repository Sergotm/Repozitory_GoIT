'///////////////////////////////////////////////////////////////Setter | Getter'
'''
Гетери (від англ. get - отримувати) - це методи, які дозволяють отримати значення поля. 
Вони використовуються, коли доступ до поля потребує якоїсь додаткової обробки або коли безпосередній доступ до поля не бажаний з міркувань 
інкапсуляції. Наприклад, якщо потрібно завжди повертати значення поля у вигляді рядка, навіть якщо воно зберігається як число.

Сетери (від англ. set - встановлювати) - це методи, які дозволяють встановити значення поля. 
Вони найчастіше використовуються для валідації даних, які намагаються присвоїти полю. Наприклад, якщо ми маємо поле, 
який повинно приймати значення лише додатні числа, можна в сетері додати перевірку, 
яка буде викидати виняток або повертати помилку, якщо намагатися присвоїти йому від'ємне число.'''
def A1():
    class Person:
        def __init__(self, ages):
            self.__age = None
            self.age = ages

        @property # Getter
        def age(self):
            return self.__age
        
        @age.setter
        def age(self, value):
            if value < 0:
                raise ValueError("18")
            
            self.__age = value
            

    if __name__ == "__main__":
        person = Person(-5)
        print(person.age)

def A2():
    class Person:
        def __init__(self, name:str, age:int, is_active:bool, is_admin:bool) -> None:
            self.name = name
            self.age = age
            self.__is_active = None
            self.__is_admin = None
            self.__is_active = is_active
            self.__is_admin = is_admin

        @property
        def is_active(self):
            return self.__is_active

        @is_active.setter
        def is_active(self, value:bool):
            if value != True:
                raise '[Is_active not True]'
            self.is_active = value

        @property
        def is_admin(self):
            return self.__is_admin

        @is_admin.setter
        def is_admin(self, value:bool):
            if value == True:
                raise '[Is_admin not False]'
            self.__is_admin = value

        def gretting(self):
            return f'Hi{self.name}'
        

    if __name__ == "__main__":
        user = Person(name='Serhii', age= 24, is_active=True, is_admin=False)
        print(f'is_admin:{user.is_admin}')
        print(f'is_active:{user.is_active}')
        # user.is_admin = True
        user.is_active = False
        print(f'is_admin:{user.is_admin}')
        print(f'is_active:{user.is_active}')

def A3():
    class Animal:
        def __init__(self,nickname, age, weight) -> None:
        
            self.__nickname = None
            self.__age = None
            self.__weight = None

            self.nickname = nickname
            self.age = age
            self.weight = weight


        @property
        def nickname(self):
            return self.__nickname

        @nickname.setter
        def nickname(self, nickname):
            if len(nickname) > 0:
                self.__nickname = nickname
            else:
                raise ValueError('Тваринка має мати імя')
            
        @property
        def age(self):
            return self.__age

        @age.setter
        def age(self, age):
            if age in list(range(0, 50)):
                self.__age = age
            else:
                raise ValueError('Тваринки стільки не живуть')
            
        @property
        def weight(self):
            return self.__weight

        @weight.setter
        def weight(self, weight):
            if weight > 0:
                self.__weight = weight
            else:
                raise ValueError('Тваринка має мати вагу')
            
    cat = Animal('',2,3)
    cat.nickname
    # cat.age

A3()