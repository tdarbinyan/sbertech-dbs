# Redis

## Установка

```bash
sudo snap install redisinsight
```
Запуск осуществляется простой командой 
```bash
redisinsight
```

## Импорт данных и сравнение скорости

Скачал [json](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/dataset/large-file.json) размером 26MB с историей действий на `github.com`

Внутри графического интерфейса RedisInsight создал базу данных
![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image1.png?raw=true)

Для загрузки в нее данных было решено воспользоваться библиотекой ```redis``` на ```python```

Все скрипты лежать в папке [/scripts](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/scripts), для чистоты эксперимента между их запусками запускал ```FLUSHDB``` в CLI, так любезно предоставленной в Redisinsight

Их работа и сравнение времени

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image2.jpg?raw=true)

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image3.png?raw=true)

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image4.png?raw=true)

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image5.png?raw=true)

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image6.png?raw=true)

## Кластер

Кластер я создавал по инструкциям с [официального сайта](https://developer.redis.com/operate/redis-at-scale/scalability/exercise-1/).

Настраиваем конфигурацию для каждой ноды и запускаем их по отдельности, передав конфигурацию как аргумент командной линии.

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image7.png?raw=true)

Запускаем кластер, указав все ноды

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image8.png?raw=true)

Система сама определяет 3 мастер ноды и назначает им по одной реплике

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image9.png?raw=true)

## Сравнение загрузки данных на кластер

Загрузка данных на кластер ожидаемо оказалась более чем в 2 раза медленне, с учетом как минимум репликации - не мудрено.

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image10.png?raw=true)

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image11.png?raw=true)

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image12.png?raw=true)

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image13.png?raw=true)

В итоге получаем распределенную базу данных на 3-х нодах, каждая из которых имеет свою реплику

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image14.png?raw=true)

## Отказоустойчивость кластера
Отключив мастер ноду, в терминале его соответственной слейв ноды видим, что он победил в выборах и стал новой мастер нодой на замену старому.

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image15.png?raw=true)

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image16.png?raw=true)

Возвращаем отключенную ноду, которая становится слейвом нового мастера. При отключении слейва мастер нода просто сообщает об этом, но кластер не суетится, выборы не проводятся.

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image17.png?raw=true)

Но если вслед за отключенным слейвом отключить его мастера, то есть вырубить полностью одну ветку данных, ожидаемым образом кластер перестает отвечать.

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework2/images/image18.png?raw=true)

Итог проверки:
Частичное отключение ветки(мастер + его реплики) совершенно спокойно воспринмается Redis-ом, полное же отключение ломает бд. 