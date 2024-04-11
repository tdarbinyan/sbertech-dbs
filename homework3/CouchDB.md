# CouchDB

## Установка

Для установки следовал инструкциям на [официальном сайте](https://docs.couchdb.org/en/stable/install/windows.html).
После установки проследовал по адресу `http://127.0.0.1:5984/_utils#setup`, где получил доступ к графическому интерфейсу `Fauxton`

## Пользование

Захожу с указанными мною при установке, не угадываемыми, не взламываемыми логином и паролем - `admin` и `admin`

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework3/images/image1.png?raw=true)

Для поставленных в домашнем задании задач нам хватит и одной ноды

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework3/images/image2.png?raw=true)

Создаю документ с полем `name` и вписываю туда свою фамилию

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework3/images/image3.png?raw=true)

После сохранения в документе появляется номер ревизии, первая часть которого(до тире), как окажется в дальнейшем, инкрементируется при изменении документа

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework3/images/image4.png?raw=true)

## Выполнение задания

Получилось у меня полностью разобраться не с первой попытки, так что для чистоты эксперимента локальная база данных джаваскрипта переименовывалась.

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework3/images/image5.png?raw=true)

С такой ссылкой подключение нам ничего не дает, даже если указать `admin:admin@` перед `localhost`.
Понимая, что проблема кроется в настройках базы данных, следуем в настройки и находим там `CORS`, который нужно включить, а так же указать разрешенные домены. В моем случае я указал все домены

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework3/images/image6.png?raw=true)

Желаемый результат получен

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework3/images/image7.png?raw=true)

## Исследование настроек доступа

Для полного понимания как устроен доступ к базе данных, я переименовал локальную базу джаваскрипта, включил `CORS`, но ссылку оставил без данных для аутентификации. Такое не сработало благодаря настройкам ролевого доступа внутри CouchDB

![alt image](https://github.com/tdarbinyan/sbertech-dbs/blob/main/homework3/images/image8.png?raw=true)

Вывод: Пользователь, пытающийся получить доступ к базе данных, должен пройти аутентификацию для роли(если они есть) с достаточными правами для его задач, в то же время база данных должна принимать от его домена запросы. Без хотя бы одной части этого требования доступ к данным не получить

## Offline

Выключив `CouchDB` и перезагрузив джаваскрипт все еще вижу свою фамилию, задание на этот благополучно выполнено



