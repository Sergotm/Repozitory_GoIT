from pathlib import Path

def total_salary(path:Path)->None:
    total_sum = 0
    count_person = 0
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            for line in file:
                user = line.strip().split(',')
                print(user)
                # if len(user) > 1:
    #                 sum_float = float(user[1])
    #                 total_sum += sum_float
    #                 count_person +=1
            
    #     if count_person == 0:
    #         total_sum = 0
    #     else:
    #         res_total = total_sum / count_person
    #     return total_sum, res_total

    except FileNotFoundError:
        print(f'Файл отсутсвует !')
        return None, None


# total,average = total_salary('Home_Work_GoIT//Module_4//Text_1.txt')
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
# # print(type(total))

total_salary('Home_Work_GoIT//Module_4//Text_1.txt')