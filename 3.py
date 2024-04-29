words = '''
cAnnot
cannOt
fOund
pAge'''

# words = '''
# cAnnot
# cannOt
# fOund
# pAge'''

# test = 'thE pAge cAnnot be found'
test = 'The PAGE cannot be found'
dict_pety = {}
count = 0
for word in words.split():
    # dict_pety[word.lower()] = dict_pety.get(word.lower(), []) + [word]
    dict_pety.setdefault(word.lower(),[]).append(word)
    
print(dict_pety)

for word in test.split():
    if word.lower() in dict_pety:
        if word not in dict_pety[word.lower()]:
            count += 1
    else:
        for el in word:
            if el.isupper():
                count +=1
print(count)

'////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////'

accesses ='''
helloworld.exe R X
pinglog W R
nya R
goodluck X W R
'''
queries = '''
read nya
write helloworld.exe
execute nya
read pinglog
write pinglog'''


operations = {'read':'R',
              'write':'W',
              'execute':'X'}

files = {}

for el in accesses.strip().split('\n'):
    file, *o = el.split()
    files[file] = o
    
for el in queries.strip().split('\n'):
    oper, name = el.split()
    print('-'*20)
    print(el)
    if operations[oper] in files[name]:
        print('Yes')
    else:
        print('Access denied')



