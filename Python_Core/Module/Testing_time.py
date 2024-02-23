url_search = '<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>'
_, jet = url_search.split('?')

obj_jet = {}

for el in jet.split('&'):
    key,value = el.split('=')
    obj_jet.update({key: value.replace('+', ' ')})

for key, values in obj_jet.items():
    print(f'Key: {key} | Values: {values}')