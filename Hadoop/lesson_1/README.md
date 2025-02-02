# Урок 1. Введение в Hadoop

## Задания

### Задание 1 
Получить доступы и зайти на кластер.

Выполнить “hdfs dfs -ls” и “hdfs dfs -ls /” и сказать, в чём разница между этими командами.

### Задание 2:
Представим, что вы работаете в крупной сети гипермаркетов и вам предстоит с 0 строить платформу для Аналитики и Data Science.
Для каждого из приведенных примеров решить, что лучше использовать для хранения данных: классическую RDBMS, Hadoop HDFS или простой FTP-сервер.
Каждый ответ пояснить 1-3 предложениями.

1. Куда лучше загружать чеки с информацией о купленных товарах? Данные предполагается использовать на каждодневной основе для аналитики продаж, а также для генерирования фичей для будущих рекомендательных систем.
2. Куда лучше загружать xlsx-файлы с отчётами, которые будет делать команда аналитиков?
3. Куда загружать презентации и фотоотчеты с прошедших корпоративных мероприятий?
4. Бизнес решил копировать и хранить данные, которые генерирует платформа Google Analytics, на своей стороне. Куда лучше сохранять эти многочисленные тяжелые логи?
5. Куда лучше сохранять записи с камер, учитывая, что в планах лежит разработка ряда нейросетей по противодействию кражам и постепенного перехода к концепции Unmanned store.
6. Куда лучше выгружать логи всех наших IT-систем, для анализа, который будет проводиться раз в несколько месяцев.
7. Куда лучше сохранять хешированные данные наших клиентов, для обмена с партнёрами (кобренд-активности)?


### Решение:

#### Задание 1.

“hdfs dfs -ls” - показывает содержание домашней папки пользователя /user/<currentUser>
“hdfs dfs -ls /” - показывает содержание корневой папки hdfs

#### Задание 2

Вопрос 1- Куда лучше загружать чеки с информацией о купленных товарах?

Ответ 1. Чеки имеют определённый один формат для всех видов товаров. Поэтому можно сразу загружать в реляционную базу данных для OLTP. Затем переносить в базу для OLAP.


Вопрос 2- Куда лучше загружать xlsx-файлы с отчётами, которые будет делать команда аналитиков?

Ответ 2. Отчёты обычно не имеют стандартного формата. И считывать их файлы будут редко. Поэтому стоит грузить на FTP сервер (лучше через SSH!). 


Вопрос 3- Куда загружать презентации и фотоотчеты с прошедших корпоративных мероприятий?

Ответ 3. Презентации и фотоотчеты не имеют стандартного формата. И считывать их файлы будут редко. Поэтому стоит грузить на FTP сервер (лучше через SSH!). 


Вопрос 4- Бизнес решил копировать и хранить данные, которые генерирует платформа Google Analytics, на своей стороне. Куда лучше сохранять эти многочисленные тяжелые логи?

Ответ 4. Если логи больше размера блока HDFS (64 мегабайт) и в будущем их надо будет быстро читать, то стоит записывать их в Hadoop HDFS. Если читать не надо будет, а только складировать, то FTP.


Вопрос 5- Куда лучше сохранять записи с камер, учитывая, что в планах лежит разработка ряда нейросетей по противодействию кражам и постепенного перехода к концепции Unmanned store.

Ответ 5. Видео файлы довольно большие. Для их быстрого чтения стоит поместить их в Hadoop HDFS. Иначаче создание моделей машинного обучения будет медленным.


Вопрос 6- Куда лучше выгружать логи всех наших IT-систем, для анализа, который будет проводиться раз в несколько месяцев.

Ответ 6. В файл на отдельном сервере (через SSH), на который будет действовать механизм logrotate с разбиением на файлы по размеру и gz сжатием старых файлов.


Вопрос 7- Куда лучше сохранять хешированные данные наших клиентов, для обмена с партнёрами (кобренд-активности)?

Ответ 7. Если к этой информации партнёры будут получать доступ через API с большой частотой запросов, то стоит использоватьреляционную базу данных. Поиск по колонке с хешами может быть быстрее, чем делать файлы с именами-хешами и записывать туда информацию.




## Решение

Решение домашних заданий (см.файлы)
