from pathlib import Path

def total_salary(path:Path)-> int:
    total = 0
    len_user = 0
    with open('Home_Work_GoIT\Module_4\Text_1.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            user = line.strip().split(',')
            if len(user) > 1:
                count = float(user[1])
                total += count
                len_user += 1
                
    if len_user == 0:
        total = 0
    else:
        sum_total = total / len_user
    
    return total, sum_total



total, average = total_salary(Path('Home_Work_GoIT\Module_4\Text_1.txt'))
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
# total_salary(Path('Home_Work_GoIT\Module_4\Text_1.txt'))