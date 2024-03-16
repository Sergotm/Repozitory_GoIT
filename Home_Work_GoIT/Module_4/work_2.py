from pathlib import Path

def get_cats_info(path:Path)->list:
    cat_list = []
    with open(path, 'r',encoding='UTF-8') as file:
        for line in file:
            get_new_line = line.strip().split(',')
            cat_list.append({'id':get_new_line[0],'name':get_new_line[1],'age':get_new_line[2]})
        return cat_list
        
cats_info = get_cats_info(Path("Home_Work_GoIT\\Module_4\\Text_2.txt"))
print(cats_info)

