# Mongo DB

## Установка

Устанавливал я следуя [инструкциям](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/#import-the-public-key-used-by-the-package-management-system) официального сайта

![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/install1.png?raw=true)
![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/install2.png?raw=true)
![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/install3.png?raw=true)
![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/install4.png?raw=true)

## Импорт данных

Для ознакомления с MongoDB я выбрал простенький датасет [Titanic](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/dataset/titanic.csv)
Далее скачиваю ее и добавляю в коллекцию `titanic` в базе `mydb`. Аргумент `--headerline` подсказывает Монге, чтобы первая строчка датасета - названия таблиц.

![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/import1.jpg?raw=true)

Проверяем, что коллекция загрузилась

![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/import2.jpg?raw=true)


var start = new Date();
db.titanic.find({ Age: 30 }).toArray();
var end = new Date();
print("Без индекса: " + (end - start) + " мс");

var start = new Date();
db.titanic.find({ Age: 30 }).toArray();
var end = new Date();
print("С индексом: " + (end - start) + " мс");



