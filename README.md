# api_final
### Описание проекта
Данный проект реализует API для проекта yatube. Такого вот живого журнала в
миниатюре.

Автор: Юрий Филатов
### Стек технологий
* Python 3.9
* Django 3.2
* DRF 3.12

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:fyurikon/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры использования API
1. Сначала следует создать суперпользователя:
```
python3 manage.py createsuperuser
```
Вводим логин и пароль. Пользователь создан.
2. Теперь получаем токен через API (можно использовать Postman
или то, что Вам удобно). Если мы используем Postman, тогда выбираем POST-запрос
Далее выбираем body -> raw -> JSON. В JSON-e нам нужно передать логин и пароль
для пользователя, которого мы создали.
```
http://127.0.0.1:8000/api/v1/jwt/create/
```
```json
{
    "username": "John",
    "password": "ChangeMe!1"
}
```
Копируем полученный токен, он нам пригодиться для следующих шагов.
3. Теперь создадим простой пост через API, не забыв предварительно добавить 
токен в HEADERS. Выбираем HEADERS, в поле Key вводим Authorization в поле
Value вводим Bearer пробел и наш токен, полученный на предыдущем шаге.
Примерно так:
```
Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXB...
```
```
http://127.0.0.1:8000/api/v1/posts/
```
```json
{
    "text": "Новый тестовый пост для проверки работоспособности API."
}
```

Выполняем POST-запрос - готово!
В ответ мы получим примерно следующее:
```json
{
    "id": 1,
    "text": "Новый тестовый пост для проверки работоспособности API.",
    "pub_date": "2023-05-08T17:25:43.741698Z",
    "author": "fyuriko",
    "image": null,
    "group": null
}
```

Помимо текста, при создании поста, можно ещё ввести группу и добавить картинку.
JSON для создания поста, в общем виде, выглядит так:
```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
4. Мы можем получить все посты используя GET-запрос.
```
http://127.0.0.1:8000/api/v1/posts/
```

5. С полной документацией к API можно всегдя ознакомиться по адресу.
```
http://127.0.0.1:8000/redoc/
```