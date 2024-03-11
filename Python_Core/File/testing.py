with open('Python_Core\File\\text.txt','w', encoding='UTF-8') as file:
    file.write('Hello my name is Serhii')
    


with open('Python_Core\File\\text.txt','r', encoding='UTF-8') as file:
    # print(file.seek())
    print(file.read(5))
    file.tell()
    file.seek(6)
    print(file.read(7))
    file.tell()
    file.read(1)
    print(file.read(9))
    file.tell()












