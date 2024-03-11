from pathlib import Path, PurePath
import shutil
import time

'''Модуль pathlib в Python є сучасним інструментом для роботи з файловою системою, що надає об'єктно-орієнтований інтерфейс для роботи з шляхами. 
Він прийшов на заміну застарілому модулю os, роботу з яким ще можна зустріти в старих прикладах коду.'''
def _PurePath():
    PurePath - '''це базовий клас у pathlib, який надає об'єктно-орієнтовані методи для маніпуляції шляхами без доступу до файлової системи. 
    Він може бути використаний для роботи з шляхами на різних операційних системах. 
    PurePath дозволяє виконувати такі операції, як розділення шляху на частини, перевірка суфіксів, імен файлів, шляхів тощо.'''

    new_path = PurePath('/usr/bin/simple.jpg')
    print(f'Тут будет имя файла: {new_path.name}')
    print(f'Тут будет тип файла: {new_path.suffix}')
    print(f'Тут будет путь к файлу: {new_path.parent}')

    new_dir = Path('Python_Core\\File\\text.txt')

def _Path():
    Path - '''Клас наслідує всі методи з PurePath i додає методи для виконання операцій, які вимагають доступу до файлової системи, таких як читання, запис файлів, перевірка існування файлів тощо. 
    З класом Path можна створювати нові файли, читати та записувати дані, перевіряти існування шляхів, перелічувати файли у директорії тощо'''

    s = Path('Python_Core\Module\example.txt') # Создание файла
    s.write_text('Hello wrold!') # В этот файл записывает текст
    print(s.read_text()) # Файл считываеться и выводится на екарн
    print(f'Exitst: {s.exists()}') # Проверка пути на существование и вывод на екран вернет True или False

    '///////////////////////////////////////////////////////////////////     Создание путей Path      /////////////////////////////////////////////////////////////////////////////////'
    # Начало пути
    base_path = Path('/url/google')
    new_path = base_path / 'Go_IT' / 'Home_work.py'
    print(new_path), '\url\google\Go_IT\Home_work.py'

    '//////////////////////////////////////////////// Относительные | абсолютные пути        with_name | suffix_name  /////////////////////////////////////////////////////////////////////////////////'

    'Абсолютный путь' - 'C:\Users\Sergo\Desktop\k_w\\repozitory\Python_Core\Module\Pathlib.py'
    'Относительный путь' - 'Python_Core\Module\Pathlib.py'

    new_file = Path('Python_Core/Module/nix.txt')
    text = 'Hello my friends. Go to school and my dog. I have a brother, and sisters'
    new_file.write_text(data=text, encoding='UTF-8',errors='')
    '''data - рядок, який необхідно записати в файл.
        encoding - необов'язковий, ім'я кодування, яке використовується для декодування файлу. Якщо не вказано, використовується кодування за замовчуванням.
        errors - необов'язково, інструкція, як обробляти помилки декодування. 
    errors='strict'. Це значення за замовчуванням. Якщо виникає помилка декодування, буде викинуто виключення UnicodeDecodeError.
    errors='ignore'. Якщо ми хочемо ігнорувати помилки декодування. Частини тексту, що не можуть бути декодовані, будуть просто пропущені.
    errors='replace'. Якщо пропускати ми не хочемо, то замінимо неможливі для декодування символи на спеціальний символ заміни, згідно документації символ '?'.  '''
    
    file = Path('Python_Core/Module/nix.txt')
    read_text = file.read_text(encoding='UTF-8')
    '''
    encoding - необов'язковий, ім'я кодування, яке використовується для декодування файлу. Якщо не вказано, використовується кодування за замовчуванням.
    errors - необов'язково, інструкція, як обробляти помилки декодування.'''
    print(read_text)


    absolte_path = new_file.absolute()
    print(f'Тут абсолютный путь: {absolte_path}')

    relative_path = Path('C:\\Users\\Sergo\\Desktop\\k_w\\repozitory\\Python_Core')
    result_relavite_path = absolte_path.relative_to(relative_path)
    print(f'Тут относительный путь: {result_relavite_path}')

    new_name = result_relavite_path.with_name('Nensi.txt'),             'Тут меняем имя, но сам путь не меняеться'
    new_suffix = new_name.with_suffix('.py')
    new_absolute_path = new_suffix.absolute()
    print(f'Тут поменяли name | suffix: {new_absolute_path}')

    original_path = Path('Python_Core/Module/Text_file.txt')
    new_path = original_path.with_name('Fack.txt'),                      'rename меняет название name | suffix глобально '
    original_path.rename(new_path)


    new_dir = Path('Python_Core\File\File.py')

    if new_dir.exists():
        if new_dir.is_file():
            new_dir.unlink(missing_ok=True),   'Удаляем файл если существует !' 'missing_ok=True если не существует ошибки не будет '
            print(f'Файл было удалено: {new_dir}')
    else:
        print(f'Файла не существет: !')

def Bytes_Path():
    file_path = Path('Python_Core/Module/Pack/example.bin')
    data_bin = b'Python landguage class'
    file_path.write_bytes(data=data_bin)

    read_bytes = file_path.read_bytes()
    print(read_bytes)  

def Path_sys():
    import sys
    def main():
        if len(sys.argv) < 2:
            user_input = ''    
        else:
            user_input = sys.argv[1]
        path = Path(user_input)
        if path.exists():
            if path.is_dir():
                # items = path.iterdir()
                items = path.glob('*.py') #'*.py' найдет все файли py | **/* Найдет все файлы в папках
                for item in items:
                    print(item)

            else:
                print(f'{path} is a file ')
        else:
            print(f'{path.absolute()} is not exits')

        if __name__ == '__main__':
            main()

def Folder():
    directory = Path('Python_Core')
    for path in directory.iterdir(): # Используеться для получения дерева всех файлов в дикертории
        print(path)

    new_dir = Path('Python_Core/Dir')
    new_dir.mkdir(parents=True,exist_ok=True)
    new_dir.rmdir() # 'Удалит Пустую деректрию -> shutil.rmtree удалит все'

    if new_dir.exists():
        print(f'{new_dir} Существует'), 'Проверит пути или файл на существование вернет True или False'

    if new_dir.is_dir():
        print(f'{new_dir} Это папка'), 'Проверит обьект на папку и True или False'

    if new_dir.is_file():
        print(f'{new_dir} Это файл'), 'Проверит обьект на файл и True или False'

    shutil.rmtree('Python_Core/Dir'), 'Удалит папка с файлами'

    if new_dir.exists():
        if new_dir.is_file():
            new_dir.unlink(missing_ok=True),   'Удаляем файл если существует !' 'missing_ok=True если не существует ошибки не будет '
            print(f'Файл было удалено: {new_dir}')
    else:
        print(f'Файла не существет: !')

def Time():
    new_dir = Path('Python_Core\File\File.py')

    creation_time = new_dir.stat().st_ctime, 'Атрибут создания'
    modification_time = new_dir.stat().st_mtime, 'Атрибут последнего изменения '

    'stat() --> os.stat_result(st_mode=33206, st_ino=68679894317402086, st_dev=1857344746, st_nlink=1, st_uid=0, st_gid=0, st_size=4818, st_atime=1710178105, st_mtime=1710089317, st_ctime=1709378945)'
    print(f'Дата создания файла: {time.ctime(creation_time)}')
    print(f'Дата последнего изменения файла: {time.ctime(modification_time)}')