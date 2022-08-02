# Тренировочный проект автотестов на API REQRES (https://reqres.in/)

## <img src="https://github.com/ioomoon/QA-guru-graduation/blob/master/img/icon5.png?raw=true" width="25"> Реализованы проверки:

API:
- Проверка статус кода запроса пользователей
- Проверка статус кода запроса конкретного пользователя
- Проверка статус кода запроса несуществующего пользователя
- Проверка количества пользователей, полученных при запросе
- Валидация полей
- Проверка статус кода отправки данных пользователя

## <img src="https://github.com/ioomoon/QA-guru-graduation/blob/master/img/icon4.png?raw=true" width="25"> Запуск проекта:
- Запуск проекта локально:
```bash
pytest -v -k development tests
```