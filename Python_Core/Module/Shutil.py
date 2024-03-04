import shutil
src, dst, path = []
def Make_archive(): # Создание Архива
    ''' base_name - шлях до файлу, де потрібно зберегти архів, без розширення.
        format - формат архіву, наприклад 'zip', 'tar', 'gztar', 'bztar' або 'xztar'.
        root_dir - директорія, з якої буде створено архів. Якщо не вказано, використовується поточна директорія.
        base_dir - директорія всередині архіву, з якої почнеться архівація'''

    shutil.make_archive(base_name='Python_Core\Module/New_arch',format='zip', root_dir='Python_Core\Module')
    shutil.make_archive(base_name='Python_Core\Module',format='tar', root_dir='Python_Core\Module')
    shutil.make_archive(base_name='Python_Core\Module',format='gztar', root_dir='Python_Core\Module')
    shutil.make_archive(base_name='Python_Core\Module',format='bztar', root_dir='Python_Core\Module')
    shutil.make_archive(base_name='Python_Core\Module',format='xztar', root_dir='Python_Core\Module')
# Make_archive()
    
def Unpack_archive(): # Розпаковка архива
    ''' filename - шлях до архівного файлу, який потрібно розпакувати.
    extract_dir - директорія, куди буде розпаковано вміст архіву. Якщо не вказано, використовується поточна директорія.
    format - формат архіву наприклад, (zip, tar, gztar, bztar, або xztar)
    Якщо параметр не вказано, Python намагається визначити формат автоматично'''

    shutil.unpack_archive(filename='Python_Core\Module/New_arch.zip', extract_dir='Arg',format=None )
    shutil.unpack_archive(filename='Python_Core\Module.tar',extract_dir='Archiv_1',format='tar' )
    shutil.unpack_archive(filename='Python_Core\Module.gztar',extract_dir='Archiv_1',format='gztar' )
    shutil.unpack_archive(filename='Python_Core\Module.bztar',extract_dir='Archiv_1',format='bztar' )
    shutil.unpack_archive(filename='Python_Core\Module.xztar',extract_dir='Archiv_1',format='xztar' )
# Unpack_archive()
    
def main_shutil(): # Методы в модуле shutil
    shutil.copy('Python_Core\Lesson.py', 'Python_Core\Module'), 'копіює файл з src в dst. Якщо dst є директорією, файл буде скопійований зі своїм поточним іменем у цю директорію.'
    shutil.copytree(src, dst), 'рекурсивно копіює всю директорію src в директорію dst.'
    shutil.move('Python_Core\Module\Lesson.py', 'Python_Core'), 'переміщує файл або директорію src в dst.'
    shutil.rmtree('Arg'), 'рекурсивно видаляє директорію path.'
    shutil.disk_usage(path), "повертає статистику використання диска, що містить загальний об'єм, використаний об'єм i вільний об'єм для даного шляху."
# main_shutil()