# Проект парсинга pep 
Парсер информации с сайта https://peps.python.org/ 
 
Для начала работы требуется клонировать репозиторий и перейти в него в командной строке: 
 
``` 
git clone https://github.com/oupsfed/scrapy_parser_pep 
``` 
 
``` 
cd scrapy_parser_pep 
``` 
 
Cоздать и активировать виртуальное окружение: 
 
``` 
python -m venv venv 
``` 
 
* Если у вас Linux/macOS 
 
    ``` 
    source env/bin/activate 
    ``` 
 
* Если у вас windows 
 
    ``` 
    source venv/Scripts/activate 
    ``` 
 
``` 
python -m pip install --upgrade pip 
``` 
 
Установить зависимости из файла requirements.txt: 
 
``` 
pip install -r requirements.txt 
``` 
 
Воможности: 
 
- парсит данные обо всех документах PEP;
- считает количество PEP в каждом статусе и общее количество PEP; 
- сохраняет результат в csv-файл. 
 
Пример работы: 
 
```commandline 
scrapy crawl pep       
``` 
 
Создает 2 csv-файла со следующими данными 
``` 
number,name,status
205,Weak References,Final
203,Augmented Assignments,Final
1,PEP Purpose and Guidelines,Active
201,Lockstep Iteration,Final
...
``` 

``` 
"Статус","Количество" 
"Active","31" 
"Withdrawn","56" 
"Final","273" 
"Superseded","20" 
"Rejected","122" 
"Deferred","37" 
"Accepted","49" 
"Draft","25" 
"Total","613" 
``` 