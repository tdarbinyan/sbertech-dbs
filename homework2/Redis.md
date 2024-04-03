# Mongo DB

## Установка

```
sudo snap install redisinsight
```
Запуск осуществляется простой командой ```redisinsight```

## Импорт данных и сравнение скорости

Скачал [json](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/large-file.json) размером 26MB с историей действий на `github.com`

Внутри графического интерфейса RedisInsight создал базу данных
[alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image1.png)

Для загрузки в нее данных было решено воспользоваться библиотекой ```redis``` на ```python```

Все скрипты лежать в папке [/scripts](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/scripts), для чистоты эксперимента между их запусками запускал ```FLUSHDB``` в CLI, так любезно предоставленной в Redisinsight

Их работа и сравнение времени
[alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image2.png)
[alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image3.png)
[alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image4.png)
[alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image5.png)
[alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image6.png)