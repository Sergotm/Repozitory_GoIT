from pathlib import Path, PurePath

absolute_path = Path('Python_Core\Module\example.txt').absolute()
print(absolute_path)

CURRENT_relative = Path("C:\Users\Sergo\Desktop\k_w\repozitory\Python_Core\Module\example.txt")
RELATIVE = absolute_path.relative_to(CURRENT_relative)
print(RELATIVE)