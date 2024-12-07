# Task-queue

Сервис по организации очереди задач

## Стэк
* Python 3.10
* FastApi
* Redis

## Запуск

```bash
docker compose -f docker-compose.prod.yaml up pd
```

Swagger доступен по адресу http://0.0.0.0:8000/docs

## Статусы задач:
- In Queue -- задача ждёт своей очереди на выполнение;
- Run -- произошел запуск задачи;
- Completed -- задача выполнена.
