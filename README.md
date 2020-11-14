Исходный код "NextTrends"
=============================

Для локального запуска

#. Создать виртуальное окружение Python 3.8.5

#. Установить зависимости
    
    pip install -r requirements.txt

#. Выполнить миграции

    ./trends/manage.py makemigrations

    ./trends/manage.py migrate

#. Создать суперпользователя

   ./trends/manage.py createsuperuser

#. Запуск проекта

   ./trends/manage.py runserver
