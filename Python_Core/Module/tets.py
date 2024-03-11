from pathlib import Path, PurePath
import shutil
import time

new_dir = Path('Python_Core\\File\\text.txt')
# new_dir.mkdir(parents=True,exist_ok=True)

# creation_time = new_dir.stat().st_ctime
# modification_time = new_dir.stat().st_mtime
# 'stat() --> os.stat_result(st_mode=33206, st_ino=68679894317402086, st_dev=1857344746, st_nlink=1, st_uid=0, st_gid=0, st_size=4818, st_atime=1710178105, st_mtime=1710089317, st_ctime=1709378945)'
# print(f'Дата создания файла: {time.ctime(creation_time)}')
# print(f'Дата последнего изменения файла: {time.ctime(modification_time)}')

if new_dir.exists():
    if new_dir.is_file():
        new_dir.unlink()
        print(f'Файл было удалено: {new_dir}')
else:
    print(f'Файла не существет: !')