import re 

text = ''' 
        Karina: 050-152-4455
        Serhii: 098-102-1588
        Marius: 577-209-4499
        '''
new_pattern = r'(\d{3})-(\d{3})-(\d{4})'
replace = r'(\1)-\2-\3'
new_kolab = re.sub(new_pattern,replace,text)
print(new_kolab)