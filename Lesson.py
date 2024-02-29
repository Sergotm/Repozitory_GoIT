# sum = 0
# for i in range(1, 11):
#     sum = sum + i
# print(sum)

# def sum_numbers(max_number: int) -> int:
#     if max_number <= 0:
#         return 0
#     if max_number == 1:
#         return 1
#     return max_number + sum_numbers(max_number-1)

# print(sum_numbers(10))

# def index_table(column_name: str)-> int:
#     index = 0
#     for item, char in enumerate(reversed(column_name)):
#         index += (ord(char) - 64) * (26 ** item)
#         return index

# print(f'Index table: {index_table}')

# def second(second=0, minutes=0, hours=0, days=0):
#     number_second_in_minutes = 60
#     number_second_in_hours = 60 * number_second_in_minutes
#     number_second_in_days = 24 * number_second_in_hours

#     return second + minutes * number_second_in_minutes +\
#     hours * number_second_in_hours + days * number_second_in_days

# print(second(minutes=5, days= 1))


