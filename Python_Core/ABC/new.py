
message = 'Hello world! Привет мир!'
print(message.encode())
print(message.encode('UTF-16'))
print(message.encode('CP1251'))

with open('Python_Core\\ABC\\bytes.bin', 'wb') as file:
    file.write(message.encode('UTF-8'))


with open('Python_Core\\ABC\\bytes.bin', 'rb') as file:
    print(file.read().decode('UTF-8'))