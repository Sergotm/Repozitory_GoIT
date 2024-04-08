from collections import namedtuple,Counter, deque, defaultdict
from decimal import Decimal, getcontext, ROUND_HALF_EVEN, ROUND_HALF_UP, ROUND_DOWN
from time import time
def mane_tuple(): # Именнованый Tuple
    name_tuple = namedtuple('Person', ['name', 'age', 'city', 'country', 'pol'])
    user_1 = name_tuple('Serhii', '24', 'Wroclaw', 'Poland', 'Men')
    user_2 = name_tuple('Karina', '34', 'Odessa', 'Poland', 'Women')
    print(f'{user_1.name, user_1.age, user_1.city, user_1.country, user_1.pol}')
    print(f'{user_2[0], user_2[1], user_2.city, user_2[3], user_2[4]}')
    print(f'{user_1[0], user_2[0], user_2.city, user_2.country}')

def count(): # Считаем количество елементов в списке
    student_marks = [4, 2, 4, 6, 7, 4, 2, 4, 4, 7, 7, 8, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
    counter_num = {}
    for el in student_marks:
        if el in counter_num:
            counter_num[el] +=1
        else:
            counter_num[el] = 1
    return counter_num

def counter(): # Быстрий подсчет значений на количество вернет Dict
    student_marks = [4, 2, 4, 6, 7, 4, 2, 4, 4, 7, 7, 8, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
    mark_counts = Counter(student_marks)
    # # return mark_counts #Вернет словарь
    # # return mark_counts.most_common(8) #Вернет список с кортежей

    text = '''So perhaps, you've generated some fancy text, and you're content that you can now copy and paste your fancy text in the 
    comments section of funny cat videos, but perhaps you're wondering how it's even possible to change the font of your text?
    Is it some sort of hack? Are you copying and pasting an actual font?'''

    word = text.split()
    words = Counter(word)
    for word, count in words.items():
        print(f'{word} : {count}')
    
    words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
    new = defaultdict(list)
    news = {new[i[0]].append(i): new for i in words}
    print(news)
    
def Defaultdict(): # Cоздание словаря с ключами которых еще не было
    text = '''ing and pasting an actual font'''
    word_dict = {}
    word = text.split(' ')

    for i in word:
        element = word_dict.get(i[0])
        if element:
            element.append(i)
        else:
            word_dict[i[0]] = [i]
    print(word_dict)
    '////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'
    text = '''ing and pasting an actual font'''
    word_list = text.split(' ')
    word_dict = defaultdict(list)
    for el in word_list:
        word_dict[el[0]].append(el)

    print(word_dict)

    '////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'
    phone_number = ['0981232366', '05034254234', '06809834222','0681232366','0507863498']
    
    phone_operator_number = defaultdict(list)
    for el in phone_number:
        if el.startswith('050'):
            phone_operator_number['Vodafone'].append(el)
        elif el.startswith('068'):
            phone_operator_number['Kyivstar'].append(el)
        elif el.startswith('098'):
            phone_operator_number['Lifecell'].append(el)
        
    print(phone_operator_number)
        
def decimall(): #Decimal 

    f = 0.2 + 0.1 + 0.3 - 0.5 # 0.10000000000000009
    dec_f = Decimal('0.2') + Decimal('0.1') + Decimal('0.3') - Decimal('0.5') # 0.1
    temp = Decimal('1') / Decimal('3') # 0.3333333333333333333333333333
    getcontext().prec = 6 # Значущие числа что будут отображаться
    temp = Decimal('1') / Decimal('3')
    # ''' Визначення значущих цифр:
    #     - Усi ненульові цифри є значущими: 1, 2, 3, 4, 5, 6, 7, 8, 9.
    #     - Нулі між ненульовими цифрами значущі: 102, 2005, 50009.
    #     - Провідні нулі ніколи не бувають значущими: 0.02; 001.887; 0.000515.
    #     - В числі з десятковою або без десяткової крапки знаходяться знакові нулі
    #     (праворуч від останньої ненульової цифри) за умови, якщо вони обґрунтовані 
    #     точністю їх використання: 389.000; 2.02000; 5.400; 57.5400. '''

    '//////////////////////////////////////////////////////////               Округление числа         ///////////////////////////////////////////////////////////'
    num = Decimal('1.45')
    s = num.quantize(Decimal('1.0'), rounding= ROUND_HALF_EVEN), 'Округление к ближайшому парному числу '

    a = num.quantize(Decimal('1.0'), rounding=ROUND_HALF_UP), 'Округление к ближайшому большому числу ' 
    
    w = num.quantize(Decimal('1.0'), rounding=ROUND_DOWN), 'Округление к меньшую сторону '
    # '''ROUND_FLOOR число завжди округляє до найближчого меншого значення, незалежно від знаку числа.
    #  * ROUND_CEILING число завжди округляє до найближчого більшого значення, незалежно від знаку числа.
    #  * ROUND_HALF_DOWN числа округлюються до найближчого значення. У випадку, 
    #     коли число знаходиться точно посередині між двома можливими варіантами округлення (наприклад, 2.5, де можливі варіанти — 2 або 3),
    #     число округляється вниз, тобто до найближчого меншого значення.
    #  * ROUND_HALF_UP числа округлюються до найближчого значення. Проте у випадку нічиї (коли число знаходиться точно 
    #     посередині між двома варіантами), число округляється вгору, тобто до найближчого більшого значення.
    #  * ROUND_UP число округляється від нуля. Це означає, що додатні числа округлюються до більшого, а від'ємні - до більшого за модулем значення.
    #  * ROUND_DOWN число округляється до нуля. Тобто додатні числа округлюються до меншого, а від'ємні - до меншого за модулем значення.
    #  * ROUND_HALF_EVEN числа округлюються до найближчого числа. Цей режим, також відомий як "банківське округлення", 
    #     округлює число до найближчого значення, але у випадку нічиї (коли число точно посередині між двома варіантами), 
    #     воно округляється до найближчого парного цілого числа. Наприклад, як 2.5 округлиться до 2, а 3.5 - до 4. 
    #     Цей метод зменшує сукупну помилку при серії округлень.'''

def lifo(): # Послений пришел первый вышел
    MAX_LEN = 5
    lifo = deque(maxlen=MAX_LEN)

    def push(el):
        lifo.appendleft(el)

    def pop(el):
        return lifo.popleft()
    
    push('Svitlana')
    push('Vova')
    push('Serhii')
    push('Rais')
    push('Karina')
    # print('Denys')

    print(lifo)
    name = pop()
    print(name)
    print(lifo)

def fifo(): # Первый пришел первый вышел
    MAX_len = 5
    fifo = deque(maxlen=MAX_len)

    def push(el):
        fifo.append(el)
    def pop():
        return fifo.pop()

    push('Svitlana')
    push('Ivan')
    push('Nazar')
    push('Petro')
    push('Ihor')
    push('Denys')
    push('Maria')
    name = pop()
    print(name)

def stack():# Проверка Stack На валидацию скобок
    #({[]})
    #({[}})
    def is_balanced(input_string):
        opens = '([{'
        closes = ')]}'
        stack = []
        for symbol in input_string:
            if symbol in opens:
                stack.append(symbol)
            elif symbol in closes:
                pothition = closes.index(symbol)
                if stack and opens[pothition] == stack[-1]:
                    stack.pop()
        if stack:   
            return False
        else:
            return True

    print(is_balanced('({[]})'))
    print(is_balanced('({[}})'))

def generator():
    def test():
        yield 1
        yield 2

    for gen in test():
        get = input(':')
        if get == 'q':
            print(gen)

    def simple_generator():
        yield 'First'
        yield 'Second'

    gen = simple_generator()
    print(gen)

    first = next(gen)
    # print(first)
    second = next(gen)
    print(second)

    def my_range(limit):
        value = 0
        while value < limit:
            yield value
            value +=1

    gen = my_range(10)

    for value in my_range(5):
        print(value)

    while True:
        try:
            r = next(gen)
            print(r)
        except StopIteration:
            break

def Decorator(): # Decorator
    def arg_loger(func):
        def inner(*args):
            if Debug:
                print(f'I am args logger. Args: {args}')
            result = func(*args)
            return result
        return inner

    def result_logger(func):
        def inner(*args):
            result = func(*args)
            if Debug:
                print(f'I am result logger. Result: {result}')
            return result
        return inner

    def timer(func):
        def inner(*args):
            start = time()
            result = func(*args)
            stop = time()
            if Debug:
                print(f'I am timer. Time: {stop - start}')
            return result
        return inner

    @timer
    @result_logger
    @arg_loger
    def calc(x, y):
        result = x + y
        return result

    Debug = True

    print(calc(5 ,8))

def deque_(): # Deque
    tasks = [
    {"type": "fast", "name": "Помити посуд"},
    {"type": "slow", "name": "Подивитись серіал"},
    {"type": "fast", "name": "Вигуляти собаку"},
    {"type": "slow", "name": "Почитати книгу"}
]
    queue = deque()
    for el in tasks:
        if el['type'] == 'fast':
            queue.appendleft(el)
            print(f'Додано швидке завдання: {el["name"]}')
        else:
            queue.append(el)
            print(f'Додано повiльне завдання: {el["name"]}')

    while queue:
        task = queue.popleft()
        print(f'Виконуеться завдання {task["name"]}')

    
if __name__ == '__main__':
    Decorator()
  