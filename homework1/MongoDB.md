# Mongo DB

## Установка

Устанавливал я следуя [инструкциям](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/#import-the-public-key-used-by-the-package-management-system) официального сайта

![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/install1.png?raw=true)
![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/install2.png?raw=true)
![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/install3.png?raw=true)
![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/install4.png?raw=true)

## Импорт данных

Для ознакомления с MongoDB я выбрал простенький датасет [Titanic](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/dataset/titanic.csv). Далее скачиваю ее и добавляю в коллекцию `titanic` в базе `mydb`. Аргумент `--headerline` подсказывает Монге, чтобы первая строчка датасета - названия таблиц.

![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/import1.jpg?raw=true)

Проверяем, что коллекция загрузилась

![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/import_test.jpg?raw=true)

## CRUD операции

Добавим пассажира

![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/insert1.jpg?raw=true)

Так-как его не было на Титанике, все же удалим, попутно научившись ставить условия. Как видно на скрине, удачей увенчалась только последняя попытка, условиям которой наш пассажир соответствовал.

![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/delete1.jpg?raw=true)


Получим же статистику соответствия класса пассажиров и средней стоимости их поездки

![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/read1.jpg?raw=true)

Вмешаемся в эту статистику, сделав одного из пассажиров миллионером

![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/update_read.jpg?raw=true)

Отпразднуем победу среднего класса индексацией таблицы.

## Индексация
Временные метрики запросов будем получать следующим сниппетом кода

```
var start = new Date();
db.titanic.find({ Age: 30 }).toArray();
var end = new Date();
```
До введения индексации запустив вышеупомянутый сниппет 5 раз получаем среднее время $86.6 = (95 + 83 + 90 + 89 + 76) / 5$

![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/noindex.png?raw=true)

Индексируем по возрасту командой `db.titanic.createIndex({ Age: 1 })
`

Повторно засылаем код с измерением времени ответа и получаем $89.4 = (90 + 109 + 80 + 84 + 84) / 5$
![alt text](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework1/images/index.png?raw=true)

Разница 3.2%, ввиду малого объема и простоты данных думаю, что это в пределах погрешности и индексация не показала себя во всей красе.
