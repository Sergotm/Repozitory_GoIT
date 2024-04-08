def A1():# Ітератор
    class CountDown:
        def __init__(self, start) -> None:
            self.current = start
            self.count = 0

        def __iter__(self):
            return self
        
        def __next__(self):
            if self.count >= len(self.current):
                raise StopIteration
            value = self.current[self.count]
            self.count +=1
            return value

    if __name__ == '__main__':
        counter = CountDown([1,2,3,4,5,6,7,8,9,10])
        for item in counter:
            print(item)

def A2():# Ітератор
    class MyIter:
        def __init__(self, start) -> None:
            self.start = start
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.start == 0:
                raise StopIteration
            self.start -= 1
            return self.start
    num = MyIter(5)
    for el in num:
        print(el)

def A3(): # Генератор
    def count_down(start):
        current = start
        current -= 1
        while current >= 0:
            yield current
            current -= 1
    
    for el in count_down(5):
        print(el)

def A4(): # Генератор
    from random import randint
    
    def rand_generator(start, stop, end):
        count = 0
        while count < end:
            yield randint(start, end)
            count +=1
            
        
    for el in rand_generator(1,20,5):
        print(el, end=' ')

def A5(): # Простой генератор
    def genf():
        for i in [1,2,3,4,5]:
            yield i
        
    for item in genf():
        print(item)
A5()