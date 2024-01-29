# coin = {
#     'Anna': 85,
#     'Petr': 92,
#     'Mari': 78,
#     'Ivan': 88
# }
# coin['Natali'] = 90

# for a, b in coin.items():
#     print(f'У {a} {b} монет')

product = {
    'Apple': 2.5,
    'Milk': 1.0,
    'Bread': 0.8,
    'Eggs': 1.5,
}
magazine = {
    'Apple': 3,
    'Bread': 1,
    'Eggs': 6,
}
total_cost = sum(product[key]* value for key, value in magazine.items())
# print(f'Всего потрачено {total_cost}')

print(f'{product.items()}')