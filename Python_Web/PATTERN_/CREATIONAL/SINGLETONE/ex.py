
# Паттерн проектування, який гарантує, що клас має лише один екземпляр і надає до нього глобальну точку доступу.
class Singltone:
    
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance
    
    def __init__(self, user, psw, port) -> None:
        self.user = user
        self.psw = psw
        self.port = port

    def conect(self):
        print(f'Звязок з БД: {self.user},{self.psw},{self.port}')

    def close(self):
        print(f'Закриття звязку з БД')

    def read(self):
        return 'Данні з БД'

    def write(self, data):
        print(f'Запис в БД {data}')



s = Singltone('Serhii','12345','80')
s1 = Singltone('Karina','67890','40')
print(s.conect())
print(f'{id(s)} | {id(s1)}')

'////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'


class Point:

    def __new__(cls, *args, **kwargs): # TODO Виконується перед строверення екземпляра классу
        print('Визов __cls__ для' + str(cls))
        return super().__new__(cls) # TODO Повернем адрес екземпляра классу

    def __init__(self, x = 0, y = 1): # TODO Виконується після строверення екземпляра классу
        print('Визов __init__ для' + str(self))
        self.x = x
        self.y = y

    def say(self):
        return self.x + self.y

point = Point(1, 2)
# print(point)
# print(point.say())