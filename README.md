REST API DEV Django + MYSQL + DOCKER
Проверка через POSTMAN
Django: POST, PUT, GET, DELETE requests 

1. Собрать и запустить докер-контейнер (по инструкции ниже)
1.1 Собрать контейнер
> docker-compose -f docker-compose.yml build

2. Запустить контейнер
> docker-compose -f docker-compose.yml up
* при первом запуске может возникнуть ошибка сервиса web - 
> web_1  | django.db.utils.OperationalError: (2002, "Can't connect to MySQL server on 'db' (115)")
> 
лечится следующим образом:
дожидаетесь, пока db_1 загрузится и в логе db_1 будет: 
> "/usr/sbin/mysqld: ready for connections."

нажимаете 1 раз ctrl+c, дожидаетесь остановки сервиса:
> Stopping web_1 ... done 

> Stopping db_1  ... done 

Снова запускаете контейнер (п.2)

#### Остановка контейнера (можно повторно запустить):
> docker-compose -f docker-compose.yml stop

#### Остановка контейнера с удалением контейнера
> docker-compose -f docker-compose.yml down

#### Остановка контейнера с удалением контейнера и волюмов БД
> docker-compose -f docker-compose.yml down -v (нужно будет пересоздать суперпользователя)

#### Добавить суперпользователя (для захода в админку):
1. Смотрим список запущенных контейнеров командой:
> docker-compose ps
2. Находим контейнер с "web" в имени. Добавляем суперпользователя командой (web_1 - имя контейнера из п.1):
> docker exec -it web_1 python manage.py createsuperuser
