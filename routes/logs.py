from __main__ import app
from flask import request

@app.route("/logs")
def get_logs():
    # вернуть лог с указанным id
    if 'id' in request.args:
        log_id = request.args.get('id')
        return f"log with {log_id} id"
    # если нет аргумента, вернуть данные всех логов
    else:
        return "all logs"