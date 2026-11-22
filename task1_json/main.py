# Задание 1. FastAPI endpoint, возвращающий JSON.
#
# Запуск (из папки task1_json):
#   uvicorn main:app --reload
# Проверка в браузере:
#   http://127.0.0.1:8000/api/hello            -> JSON по умолчанию
#   http://127.0.0.1:8000/api/hello?name=Анна  -> JSON с вашим именем
#   http://127.0.0.1:8000/docs                 -> автодокументация Swagger UI

from fastapi import FastAPI

# Экземпляр приложения — главная точка входа для uvicorn (main:app означает
# «файл main.py, переменная app»). title показывается на странице Swagger.
app = FastAPI(title="Лабораторная 6 - задание 1")


# Декоратор регистрирует функцию как обработчик GET-запроса на путь /api/hello.
# Для POST было бы @app.post("/api/hello"), есть и put/delete/patch.
@app.get("/api/hello")
def hello(name: str = "мир"):
    # name — query-параметр: FastAPI сам читает его из URL (?name=...),
    # сам приводит к типу str и сам подставит значение по умолчанию.
    # Возвращаемый словарь FastAPI автоматически превращает в JSON
    # и сам ставит заголовок ответа Content-Type: application/json —
    # вручную вызывать json.dumps() не нужно.
    return {
        "message": f"Привет, {name}!",
        "lab": 6,
        "stack": ["FastAPI", "uvicorn"],
    }
