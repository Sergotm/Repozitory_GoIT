# Оператор Match //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

fruits = ('banana', 'orange') , 'Поиск подходящего шаблона, если нету выполняеться заглушка'
match fruits: 
    case 'banana', 'orange':
        print(f'Banana')
    case _:
        pass

pets = ['cat', 'dog', 'fish']
match pets:
    case[_,_,'fish']:
        print(f'DOG,CAT,FISH')
