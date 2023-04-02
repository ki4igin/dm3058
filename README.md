## Скрипт чтения напряжения с DM3058

### Внимание:
1. Работает только на python 32-bit, для создания виртуального окружения с
необходимой версией python можно воспользоваться командой: `poetry env use "Путь до python 32-bit"`, например
```console
poetry env use "C:\Users\Artem\AppData\Local\Programs\Python\Python310-32\python.exe"
```
2. При включении мультиметра необходимо включить его вывод
 (Utility&rarr;Print&rarr;On), иначе будет ошибка чтения:  
 `VI_ERROR_IO (-1073807298): Could not perform operation because of I/O error`
 
### Запуск
```console
poetry install
poetry run python dm3058/main.py
```