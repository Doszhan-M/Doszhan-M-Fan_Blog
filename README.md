
# Фан блог

## Инструкции по запуску приложения:

### 1.Установить Redis:
```bash
sudo apt-get update
sudo apt-get install redis
redis-server
```

### 2.Установить необходимые пакеты:
```bash
pip3 install -r requirements.txt
```

### 3.Настроить почтовый сервер:
В директории `ad_board/secret` Создать 4 текстовых файла с названием:

- **ADMINS.txt**  
  почта администраторов в виде кортежа:  
  `('John', 'john@example.com'), ('Mary', 'mary@example.com')`

- **EMAIL_HOST.txt**  
  smtp сервер почты

- **EMAIL_HOST_PASSWORD.txt**  
  пароль от почтового ящика

- **EMAIL_HOST_USER.txt**  
  логин от почтового ящика

### 3.Запустить сервер:
```bash
python3 manage.py migrate
python3 manage.py runserver
```

### 4.Запустить celery:
```bash
celery -A slackbot worker -l INFO -B
```
