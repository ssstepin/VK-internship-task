# VK-internship-task
API django-сервиса друзей

## Тех. средства
- Python
- Фреймворки Django и drf (django rest framework)
- Спецификация OpenAPI (находится в корневой директории в файле openapi.yaml)

## Запуск
- Активировать виртальное окружение
- В директории ```.\vk_friends_api``` запустить ```python manage.py runserver```
- Наслаждаться

## Paths

Перед всеми запросами добавлять http://127.0.0.1:8000/api

- /register/<username: str> - регистрация
- /friend_request/<user1_id:int>/<user2_id:int> - user1 -> user2 отправляет реквест
- /requests_incoming_lsit/<user_id:int> - посмотреть лист входящих реквестов для user_id
- /requests_outgoing_lsit/<user_id:int> - посмотреть лист исходящих реквестов для user_id
- /friends_list/<user_id:int> - список друзей uder_id
- /status/<user1_id:int>/<user2_id:int> - статус дружбы user1_id и user2_id
- /delete/<user1_id:int>/<user2_id:int> - user1 удаляет user2 из друзей

## Примеры

/register/aboba - Создаст пользователя с ником aboba и вернет следующий JSON объект:

```json
{
  "new_user": {
    "id": 1,
    "username" : "aboba"
  }
```

Представим, что у нас есть пользователи с id 1 и 2. Тогда запрос в друзья будет выглядеть так:
/friend_request/1/2 - user с id = 1 посылает запрос в друзья пользователю с id = 2

## Модели
User - поля: id - идентификатор пользователя, username - имя пользователя
FriendRequest - user1_id, user2_id - кто и кому отправил запрос на добавление в друзья
FriendsPair - user1_id, user2_id - два пользователя - друзья (порядок id не важен)

Создан суперпользователь
- login: admin
- password: 12345678