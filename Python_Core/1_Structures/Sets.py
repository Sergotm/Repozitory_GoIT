#   Множество Set //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

a,b,c,d,= {}
my_set = {1, 2}, 'Создание множества'
my_set = set({1, 2}), 'Создание множества без повторений'
my_set.add(3) , 'Добавление значений в Множество'
my_set.remove(3), 'Удаялет указаное значение, если его нет Выдает ошибку'
my_set.discard(2) , 'Удаялет указаное значение, если его нет НЕ выдает ошибку'
my_set.update()
_ = c - d , 'Разница между двумя Множествами включает которые есть в 1 но нету в 2 '
c = a.difference(b), ' Аналог ⬆'

_ = c ^ b , 'Симетричная разница. Включает елементы котрые есть в 1 и нету в другой. И наоборот'
c = a.symmetric_difference(b) , 'Аналог ⬆'

_ = c | d , 'Соединение двух Множест без дупликатов' 
c = a.union(b), 'Аналог ⬆'

_ = c & d , 'Пересечение двух множеств'
_ = a.intersection(b), 'Аналог ⬆'

_ = frozenset(c) , 'Не изменяемое Множество. Но можно делать вычесление - ^ | & '
#...