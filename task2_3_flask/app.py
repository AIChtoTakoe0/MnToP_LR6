# Задания 2 и 3. Flask: шаблон Jinja2 с данными + статическая страница и CSS.
#
# Запуск (из папки task2_3_flask):
#   python app.py
# Проверка в браузере:
#   http://127.0.0.1:5000/students  -> таблица, построенная из данных Jinja2 (задание 2)
#   http://127.0.0.1:5000/about     -> статическая страница с CSS (задание 3)

import os

from flask import Flask, render_template

# Flask(__name__) создаёт приложение. По умолчанию Flask ищет шаблоны
# в подпапке templates/, а статические файлы раздаёт по адресу /static/<путь>
# из подпапки static/ — обе папки надо создать рядом с app.py.
app = Flask(__name__)

# Данные, которые отдадим в шаблон (в реальном приложении брались бы из БД).
STUDENTS = [
    {"id": 1, "name": "Иванов Иван",  "group": "ИТ-21", "grade": 4.5},
    {"id": 2, "name": "Петрова Анна", "group": "ИТ-22", "grade": 4.9},
    {"id": 3, "name": "Сидоров Пётр", "group": "ИТ-21", "grade": 3.7},
]


# @app.route регистрирует маршрут. GET — метод по умолчанию;
# явно можно так: @app.route("/students", methods=["GET", "POST"])
@app.route("/students")
def students():
    # render_template(name, **переменные) подставляет данные в шаблон:
    # в students.html станут доступны переменные title и students.
    # Внутри шаблона: {{ title }} — вывод значения,
    # {% for %}...{% endfor %} — циклы, {% if %} — условия.
    return render_template("students.html", title="Список студентов", students=STUDENTS)


@app.route("/about")
def about():
    # Страница почти без динамики — демонстрирует подключение CSS из static/.
    return render_template("about.html", title="О работе")


if __name__ == "__main__":
    # debug=True даёт авто-перезапуск при правках кода и отладчик в браузере.
    # Только для разработки: в продакшене так включать нельзя (риск безопасности).
    # Порт берётся из переменной окружения PORT (её задают хостинги, например
    # Heroku), локально по умолчанию — 5000.
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
