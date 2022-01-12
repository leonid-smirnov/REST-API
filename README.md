REST API DEV Django + MYSQL + DOCKER
Проверка через POSTMAN
Django: POST, PUT, GET, DELETE requests 

1. Собрать и запустить докер-контейнер:
1.1 Собрать контейнер
> docker-compose -f docker-compose.yml build

1.2 Запустить контейнер
> docker-compose -f docker-compose.yml up

#### Остановка контейнера (можно повторно запустить):
> docker-compose -f docker-compose.yml stop

#### Остановка контейнера с удалением контейнера
> docker-compose -f docker-compose.yml down

#### Остановка контейнера с удалением контейнера и волюмов БД
> docker-compose -f docker-compose.yml down -v (нужно будет пересоздать суперпользователя)

#### Добавить суперпользователя (для захода в админку):
1. Смотрим список запущенных контейнеров командой:
> docker-compose ps -a
2. Находим контейнер с "web" в имени. Добавляем суперпользователя командой (web_1 - имя контейнера из п.1):
> docker exec -it web_1 python manage.py createsuperuser
