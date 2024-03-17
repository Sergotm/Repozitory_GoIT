from pathlib import Path

def proces(path:Path):
    count_day = 0
    with open(path, 'r', encoding='UTF-8') as file:
        for line in file:
            rep_line = line.strip()
            print(rep_line)

det_txt = Path('temp\\temperature.txt')
proces(det_txt)