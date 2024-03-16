'python -m venv .venv соззать новое Вир.Среду'
'.\.venv\Scripts\Activate.ps1  Открыть ее Win' 
'source .venv/bin/activate macOS'
'pip freeze > requirements.txt создать файл с '
'pip freeze | % {pip uninstall -y $_.split('==')[0]}' 'Удалинеие всех пакетов pip'

