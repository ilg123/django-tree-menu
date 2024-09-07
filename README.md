# Django Tree Menu

Этот проект представляет собой Django-приложение для реализации древовидного меню с использованием template tag.

## Требования

- Docker
- Docker Compose

## Установка

1. Клонируйте репозиторий:
   git clone https://github.com/ilg123/django-tree-menu.git
   cd django-tree-menu

2. Создайте файл .env в корневой директории проекта и добавьте следующие строки пример -> env_example.txt

3. Соберите Docker-образ:
    docker-compose build

4. Выполните миграции и создайте суперпользователя:
    docker-compose run web python manage.py makemigrations
    docker-compose run web python manage.py migrate
    docker-compose run web python manage.py createsuperuser

5. Выполните миграции и создайте суперпользователя:
    docker-compose up


6. Откройте браузер и перейдите по адресу http://127.0.0.1:8000/admin/, чтобы добавить пункты меню через админку.





