from pathlib import Path
import shutil
NUMBER_LINES = 4

try:
    lines = []
    with open('Python_Core\\Module\\test.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            lines.append(line)
            if len(lines) > NUMBER_LINES:
                lines.pop(0)
    print(lines)
except OSError as err:
    print(f'Помилка дотупа к файлу: {err}')



with open('Python_Core\\Module\\test.txt', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    last_n_lines = lines[-NUMBER_LINES:]
print(last_n_lines)

folder = Path('Python_Core\\Path\\temp.txt')



try:
    with open('Python_Core\\Path\\temp.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            print(line, end='')
except Exception:
    print('Error: ')
finally:
    print('Happy end')

archive = shutil.make_archive('my_archive', 'zip', 'Python_Core\Path')
shutil.unpack_archive('my_archive.zip','ABC')

n = []
n.append(el for el in Exception)
print(n)