# k = int(input('Enter a number: '))
# l = int(input('Enter a number: '))
# if k != l:
#     if k < l:
#         k = l
#     else:
#         l = k
# else:
#     l = 0
#     k = 0
    
# print(k, l)
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#swap 
# baz = int(input('Enter a number baz: '))
# foo = int(input('Enter a number foo: '))
# # if baz < foo:
# #     temp = baz
# #     baz = (baz + foo)
# #     foo = temp * foo
# # else:
# #     temp = foo
# #     foo = (foo + baz) / 2
# #     baz = temp * foo

# if baz < foo:
#     baz,foo = (baz + foo) / 2, baz * foo
# else:
#     foo,baz = (foo + baz) / 2, foo * baz
    
# print(f'Baz: {baz} | Foo: {foo}')
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# s = input(f'Enter a string: ')
# index = 0
# for char in s:
#     if char == 'a':
#         break
#     index +=1
# print(f'Перше входження: {index}')
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# s = input(f'Enter a string: ') My name is Karina, 5,13
# index = 0
# count = 0
# for char in s:
#     if char == 'a':
#         index = count
#     count+=1
# print(f'Останне входження: {index}')
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# res = ('/', 5, 2)
# match res:
#     case('+', x, y):
#         print(x + y)
#     case('-', x, y):
#         print(x - y)
#     case('*', x, y):
#         print(x * y)
#     case('/', x, y):
#         print(x / y)
#     case('/', x, 0):
#         print('На 0 не делиться')
#     case _:
#         print()
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# num = input(f'Please number: ')
# is_poly = num == num[::-1]
# print(num[::-1] == num)


# is_palindrom = True
# for item in range(len(num)):
#     if num[item] != [-item - 1]:
#         is_palindrom = False
#         break
# if is_palindrom:
#     print(num, ' is a palindrom')
# else:
#     print(num 'a not palindrom')

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

students = {}
count = int(input(f'How many students: '))
s = 0
for i in range(count):
    name = input('Please enter name: ')
    point = int(input(f'Please enter point: '))
    students[name] = point # {'Anna':5, 'Andrii': 4}
    s += point 
avg = sum / count
print(f'The average point is: {avg}. Students with average point is:')
for student in students:
    if students[student] > avg:
        print(student)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# days = {
#     1: 'Monday',
#     2: 'Tuesday',
#     3: 'Wednesday',
#     4: 'Thursday',
#     5: 'Friyday',
#     6: 'Satuday',
#     7: 'Sunday'
# }

# while True:
#     i = int(input(f'Enter a day: '))
#     try:
#         value = int(i)
#         print(f'{days.get(value, 'Такого дня нема')}')
#     except ValueError:
#         if i == 'q':
#             break
#         print(f'Нада ввести число')
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# first = int(input(f'Enter the first integer: '))
# second = int(input(f'Enter the first integer: '))
# gcd = min(first, second)

# while not(first % gcd == 0 and second % gcd == 0):
#     gcd = gcd -1 

# print(gcd)
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# list_1 = [1, 2, 3]
# list_2 = [10, 20, 30]

# for i in list_1:
#     for j in list_2:
#         print(i , j)
#         if i == 2 and j == 20:
#             print('break')
#             break
#     break
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# list_1 = [1, 2, 3]
# list_2 = [10, 20, 30]
# for i in list_1:
#     print('START')
#     for j in list_2:
#         print('-> ', i, j)
#         if i == 2 and j == 20:
#             print(f'break inner for')
#             break
#     else:
#         print('Finsh inner for')
#         continue
#     print(f'break outer for')
#     break