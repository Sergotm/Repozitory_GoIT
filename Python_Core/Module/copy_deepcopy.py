from copy import deepcopy, copy
from collections import UserList
'//////////////////////////////////     Поверхнева копія   ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'
# ''' Поверхнева копія створює новий об'єкт, але не копіює вкладені об'єкти. 
# Замість цього, вона копіює лише посилання на вкладені об'єкти. 
# Це означає, що якщо ви змінюєте вкладені об'єктив оригіналі,
# ці зміни також відобразяться у поверхневій копії.

my_list = [1,2,3,4,5,{'name':'Serhii'}]

copy_list = copy(my_list)
copy_list.append(6)
copy_list[5]['age'] = 24
copy_list.append(19)
# print(my_list)
# print(copy_list)


'//////////////////////////////////      Глибока Копія    /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'
# Глибока копія створює новий об'єкт та рекурсивно копіює всі вкладені об'єкти.
# В результаті, ви отримуєте повністю незалежну копію оригінального об'єкта.
qwe_list = [1,2,{'name':'Pawel'}]
copy_l = deepcopy(qwe_list)
copy_l[2]['age'] = 30
# print(qwe_list)
# print(copy_l)
"////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
l = [1,2,3,['a','b','c']]
test_l = l[:]
l_copy = copy(l)
l_deep = deepcopy(l)
# print(l)
# print(l_copy)
# print(l_deep)
print('_' * 40)
l[0] = 8
print(f'original l{l}') # TODO поверхнева копія
print(f'test_l{test_l}') 
print(f'l_copy{l_copy}')
print(f'l_deep{l_deep}') # TODO глибока копія залишився без змін
l[3][0] = 'f'
print('_' * 40)

print(f'original l{l}') # TODO поверхнева копія
print(f'test_l{test_l}')
print(f'l_copy{l_copy}')
print(f'l_deep{l_deep}') # TODO глибока копія залишився без змін
print('_' * 40)
"////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
class CopyList(UserList):
    def __init__(self,*data):
        super().__init__()
        self.data = list(data)

    def __copy__(self):
        n = CopyList()
        n.data = self.data
        return n
    
    def __deepcopy__(self, memodict={}):
        n = CopyList()
        memodict[id(self)] = n
        for el in self.data:
            n.append(deepcopy(el, memodict))
        return n
    
data = CopyList([1,2,3,4,5])
data_copy = copy(data)
data_deep = deepcopy(data)

print(id(data), data)
print(id(data_copy), (data_copy))
print(id(data_deep), (data_deep))
data[0][0] = 'a'
print("_" * 50)
print(id(data[0]), data)
print(id(data_copy[0]), (data_copy))
print(id(data_deep[0]), (data_deep))



