# Restaurant Booking API
REST API для бронирования столиков в ресторане, разработанное как тестовое задание для позиции Junior Python Developer в Хайталент.

## Описание
Сервис позволяет создавать, просматривать и удалять столики и брони, с проверкой конфликтов по времени для бронирований.

## Технологии
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic (миграции)
- Docker & Docker Compose
- Pytest (тесты)

## Запуск
1. Убедитесь, что Docker и Docker Compose установлены.
2. Склонируйте репозиторий:
```bash
   git clone https://github.com/Kanres-GH/Hightalent-Gaisin-Temirlan.git
   cd hightalent-junior-python-dev
```
3. Установите необходимые зависимости:
```bash
pip install -r requirements.txt  
```

4. Запустите проект:
```bash
    docker-compose up --build -d
```
5. API будет доступно на http://localhost:8000. Swagger UI доступен на http://localhost:8000/docs

## Эндпоинты
- GET /tables/ - получить список всех столиков
- POST /tables/ - создать новый столик
- DELETE /tables/{id} - удалить столик
- GET /reservations/ - получить список всех броней
- POST /reservations/ - создать новую бронь
- DELETE /reservations/{id} - удалить бронь

## Примеры запросов
Создание столика:
```bash
curl -X POST http://localhost:8000/tables/ -H "Content-Type: application/json" -d '{"name": "Table 1", "seats": 4, "location": "window"}'
```

Создание брони:
```bash
curl -X POST http://localhost:8000/reservations/ -H "Content-Type: application/json" -d '{"customer_name": "John", "table_id": 1, "reservation_time": "2025-04-10T12:00:00", "duration_minutes": 60}'
```

Получение списка броней:
```bash
curl http://localhost:8000/reservations/
```

Удаление брони:
```bash
curl -X DELETE http://localhost:8000/reservations/1
```

## Тестирование
Локально (требуется установить зависимости из requirements.txt):
```bash
pytest
```

