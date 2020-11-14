Исходный код "NextTrends"
=============================

Для локального запуска

#. Создать виртуальное окружение Python 3.8.5

#. Установить зависимости
    
    pip install -r requirements.txt

#. Выполнить миграции

    python ./trends/manage.py makemigrations

    python ./trends/manage.py migrate

#. Создать суперпользователя

    python ./trends/manage.py createsuperuser

#. Запуск проекта

    python ./trends/manage.py runserver
