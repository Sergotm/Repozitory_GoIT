# with open('Python_Core\File\\text.txt', 'w', encoding='UTF-8') as file: 
#     pass


# with open('Python_Core\File\\text.txt', 'r', encoding='UTF-8') as file:
#     pass
# byte_array = bytearray(b"Hello")
# byte_array.append(ord("!"))  
# for el in byte_array:
#     print(el)
byte_array = bytearray(b'Kill Bill!')
string = byte_array.decode('UTF-8')
print(string)