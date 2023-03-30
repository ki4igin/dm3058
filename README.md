## Скрипт чтения напряжения с DM3058

### Внимание:
1. Работает только на python 32-bit
2. При включении мультиметра необходимо включить его вывод
 (Utility&rarr;Print&rarr;On), иначе будет ошибка чтения:  
 `VI_ERROR_IO (-1073807298): Could not perform operation because of I/O error`
 
 ### Запуск
 ```console
 poetry env use "Путь до python 32-bit"
 poetry update
 poetry run dm3058/main.py
 ```