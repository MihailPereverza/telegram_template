# Шаблон для телеграм бота (магазина)


/github/pipenv/locked/dependency-version/:user/:repo/:kind?/:packageName


## Задачи:
:white_check_mark: Хендлер на /start
:white_check_mark: Отображение профиля
:white_check_mark: Отображение баланса
:white_check_mark: Прием платежей QiWi

## Get start

1. Форкнуть проект
2. Склонировать себе
3. Разобраться с ключами сертификата ssl:  
   3.1 Сгенерировать ключи, например, с помощью openssl
по офф. гайду от телеги (https://core.telegram.org/bots/self-signed)  
   3.2 Указать путь к ним в полях .env `WEBHOOK_SSL_CERT`
и `WEBHOOK_SSL_PRIV`
4. Получить QiWi access token на сайте `https://qiwi.com/api`
5. Заполнить поля в .env:
    * `PG_USER` - имя пользователя postgres
    * `pg_pass` - пароль postgres
    * `pg_host` - хост сервера postgres
    * `PG_PORT` - порт сервера postgres
    * `PG_DB_NAME` - название базовой базы postgres
    * `TG_BOT_TOKEN` - токен от бота, полученный из BotFather
    * `TG_BOT_WEBHOOK_HOST` - хост для предоставления webhook адреса в telegram
    * `TG_BOT_WEBHOOK_PORT` - порт для предоставления webhook адреса в telegram
    * `TG_BOT_WEBHOOK_PATH` - базовая часть адреса для webhook
    * `QIWI_PHONE` - номер, на который зарегистрирован qiwi (опционально)
    * `QIWI_ACCESS_TOKEN` - токен api аккаунта qiwi (опционально)
6. Выполнить `pip install -r requirements.txt` (могут быть стандартные проблемы
с psycopg2: решение - psycopg2-binary и aiogram: решение - в pycharm через 
настройки интерпритатора напрямую установить требуемую версию)

