# Фан блог
![picture](https://crownenglishclub.ru/wp-content/uploads/2020/02/76723bac02e0e6a353f3ade7aab8906c.png)

### Инструкции по запуску приложения:

1. Установите в систему Redis:\
$ sudo apt-get update\
$ sudo apt-get install redis\
затем запустите его:\
$ redis-server

2. Создайте виртуальное окружение и установите необходимые пакеты для работы приложения:\
pip3 install -r requirements.txt\
Дождитесь окончания установки всех зависимостей.

3. Перейдите в папку ad_board/secret

3. Из корня проекта запустите сервер. Корнем считается тот каталог, где находиться файл manage.py:\
python3 manage.py runserver

4. Из корня проекта запустите Celery:\
celery -A slackbot worker -l INFO -B

5. Откройте браузер и перейдите на адрес:\
http://127.0.0.1:8000/

На этом приложение установлено и запущено. 
