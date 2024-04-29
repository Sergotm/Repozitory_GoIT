import pickle
from time import sleep
from datetime import datetime
import json
import csv
"Серіалізація об'єктів в Python — це процес перетворення структури даних або об'єкта в потік байтів для зберігання або передачі."

"Десеріалізацією називається Процес відновлення стану об'єкта з серіалізованої форми."
"Dumps -  запаковує в byte-рядок об'єкт"
"Loads- метод потім розпаковує назад з byte-рядка в об'єкт"
 
"Dump -  запаковує в byte-рядок у Файл"
"Load - метод потім розпаковує Файл назад з byte-рядка в об'єкт"
'/////////////////////////////////////////////////////////////////           File         /////////////////////////////////////////////////////////////////////////////////////////////////////////////'
def _file_():
    cena = {'cofe':35, 'hotel':130, 'kava':20, 'taxi':15}# TODO Серіалізація у Файл
    file_name = 'Python_Core\\Module\\Pickle.txt'
    with open(file_name, 'w') as file:
        for key, value in cena.items():
            file.write(f'{key} | {value}\n')
        print('_' * 20)
        
    expenses = {}

    with open(file_name, 'r') as f: # TODO Десеріалізація з Файла
        raw_expenses = f.readlines()
        for line in raw_expenses:
            key,value = line.split('|')
            expenses[key] = int(value)
    return(expenses)

'///////////////////////////////////////////////////////////////////////        Pickle         /////////////////////////////////////////////////////////////////////////////////////////////////////////'
def _pickle_():
    my_data = {'last_name':'Serhii', 'first_name':'Chervonoshapko', 'birthday':'17.01.2000', 'age': 24, 'men':True} # TODO Серіалізація у обьєкт
    serilized_data = pickle.dumps(my_data)
    print(serilized_data)

    print('_' * 35)

    deserilized_data = pickle.loads(serilized_data)# TODO Десеріалізація з Обьєкта
    print(deserilized_data)
    return('_' * 35)

def _pickle_file_():
    my_data = {'last_name':'Serhii', 'first_name':'Chervonoshapko', 'birthday':'17.01.2000', 'age': 24, 'men':True}
    my_file = 'Python_Core\\Module\\Pickle.txt'
    with open(my_file, 'wb') as file: # TODO Серіалізація у Файл
        pickle.dump(my_data, file) 

    with open(my_file,'rb') as f: # TODO Десеріалізація з Файла
        deseralized_data = pickle.load(f) 
    print(deseralized_data)
'///////////////////////////////////////////////////////////////////////        Json           /////////////////////////////////////////////////////////////////////////////////////////////////////////'
def _json_():
    some_data = {
        'key':'value',
        1:[1,2,3],
        'my_tuple':(4,5),
        'my_dict':{'new_key':'new_value'}
    }
    json_string = json.dumps(some_data) # TODO Серіалізація у обьєкт
    print(json_string)

    print('_' * 35)

    unpaked_some_data = json.loads(json_string) # TODO Десеріалізація з Обьєкта
    print(unpaked_some_data)

def _json_file_():
    some_data = {
        'key':'value',
        1:[1,2,3],
        'my_tuple':(4,5),
        'my_dict':{'new_key':'new_value'},
        'isStudent' : True
    }
    my_file = 'Python_Core\\Module\\data.json'
    with open(my_file, 'w', encoding='utf-8') as file: # TODO Серіалізація у Файл
        json.dump(some_data, file, ensure_ascii = False)
        print(some_data)
        print('_' * 90)

    with open(my_file, 'r') as f: # TODO Десеріалізація з Файла
        deserelized_some_data = json.load(f)
        return(deserelized_some_data)
'//////////////////////////////////////////////////////////////////////        csv            //////////////////////////////////////////////////////////////////////////////////////////////////////////'
'csv.writer для запису у файл'
'csv.reader для читання Файлу'

def _csv_(): # TODO csv.reader для читання Файлу
    file_name = 'Python_Core\Module\data.csv'
    new_list = []
    with open(file_name, newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for el in reader:
            # print(', '.join(el))
            new_list.append(el)
        # return('_' * 40)
    print(new_list[2])

'writer.writerows(rows) можна записати кілька рядків одразу'
'riter.writerow(row) Якщо потрібно записати один рядок'

def _csv_file_():
    file_name = 'Python_Core\Module\data.csv'
    rows = [
        ['name', 'age', 'sex'],
        ['Karina', '22', 'woman'],
        ['Serhii', '24', 'men'],
        ['Bodya', '23', 'men'],
    ]
    with open(file_name, 'w',newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(rows)
def __csv_file__(): # TODO Запис у CSV файл зі словників
    My_dict = [{'name':'Serhii','age':24,'speciality':'Elektrik'},
               {'name':'Karina','age':21,'speciality':'Parichmacher'},
               {'name':'Masha','age':22,'speciality':'Caring'}]
    file_name = 'Python_Core\Module\data.csv'
    with open(file_name, 'w', encoding='utf-8', newline='') as csvfile:
        columns = My_dict[0].keys()
        fieldnames = ['name', 'age', 'speciality']
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=columns)
        writer.writeheader()

        for el in My_dict:
            writer.writerow(el)

    with open(file_name, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            print(row)

    return '-'*60
'////////////////////////////////////////////////////////////////////////      def fucn       ///////////////////////////////////////////////////////////////////////////////////////////////////////////'
# print(_file_())

# print(_pickle_())

# print(_pickle_file_())

# print(_json_())

# print(_json_file_())

# print(_csv_())

# print(_csv_file_())

# print(__csv_file__())

'..........................................................__getstate__ | __setstate__...........................................................................................................'

class A:
    def __init__(self, important_data):
        self.important_data = important_data
        self.func = lambda: 7
        self.is_valid = True

    def __getstate__(self): # TODO  він використовується для отримання стану об'єкта для серіалізації
        return [self.important_data]
        
    def __setstate__(self, state): # TODO він використовується для відновлення стану об'єкта з даних, отриманих під час десеріалізації.
        self.important_data = state[0]
        self.func = lambda:7
        self.is_valid = True

a = A('Hello world')
s = pickle.dumps(a)

a_obj = pickle.load s(s)
print(a_obj.important_data)
    

'//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'
class A:
    def __init__(self, important_data):
        self.important_data = important_data
        self.func = lambda: 7
        self.is_valid = True

    def __getstate__(self):
        return [self.important_data]
    
            
    def __setstate__(self, state):
        self.important_data = state[0]
        self.func = lambda:7
        self.is_valid = True

a = A('Hello world')
my_file = 'Python_Core\\Module\\Pickle.txt'
with open(my_file, 'wb') as file:
    pickle.dump(a, file)

with open(my_file, 'rb') as f:
    size = pickle.load(file=f)
# print(size.important_data)
# print(size.func())
# print(size.is_valid)

'////////////////////////////////////////////////////////      Виведення початку часу серіалізацаії. Та час кінця десеріалізації     //////////////////////////////////////////////////////////////////////////////////////////////'


class RememberAll:
    def __init__(self, *args) -> None:
        self.data = list(args)
        self.saved = None
        self.restored = None

    def __getstate__(self) -> object:
        state = self.__dict__.copy() #TODO __dict__.copy дає доступ до словника конструктора __init__
        state['saved'] = datetime.now()
        return state

    def __setstate__(self,state) -> object:
        self.__dict__.update(state) # TODO update оновлення словника
        self.restored = datetime.now()


r = RememberAll(1,2,3,4,5,6,7,8,9,10)

# print(r.data)
r_dump = pickle.dumps(r)
sleep(1)
r_load = pickle.loads(r_dump)
# print(r.saved, r.restored)
# print(f'Час початку операції: {r_load.saved}\nЧас закінчення операціі: {r_load.restored}')
'////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'
class TextReder:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.file = open(self.filename, encoding='utf-8')
        self.line_count = 0

    def readlines(self):
        self.line_count +=1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]
        # return f'{self.line_count}: {line}'
        return '%i: %s' % (self.line_count, line) 
    
    def __getstate__(self) -> object:
        state = self.__dict__.copy()
        del state['file']
        return state

    def __setstate__(self, state) -> object:
        self.__dict__.update(state)

        file = open(self.filename, encoding='utf-8')
        for _ in range(self.line_count):
            file.readline()
        self.file = file



name_file = 'Python_Core\Module\poem.txt'
reader = TextReder(name_file)
# print(reader.readlines())
# print(reader.readlines())
# print(reader.readlines())
r_dump = pickle.dumps(reader)
# sleep(1)
r_load = pickle.loads(r_dump)
# new_reader = pickle.loads(pickle.dumps(reader))
while True:
    line = r_load.readlines()
    if line is None:
        break
    else:
        print(line)
# print('-' * 50)
# print(reader.readlines())
# print(reader.readlines())
# print(reader.readlines())