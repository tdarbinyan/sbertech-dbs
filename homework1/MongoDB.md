# Mongo DB

## Установка

Устанавливал я следуя [инструкциям](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/#import-the-public-key-used-by-the-package-management-system) официального сайта

![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/install1.png?raw=true)
![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/install2.png?raw=true)
![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/install3.png?raw=true)
![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/install4.png?raw=true)


var start = new Date();
db.titanic.find({ Age: 30 }).toArray();
var end = new Date();
print("Без индекса: " + (end - start) + " мс");

var start = new Date();
db.titanic.find({ Age: 30 }).toArray();
var end = new Date();
print("С индексом: " + (end - start) + " мс");

