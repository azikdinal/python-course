from __main__ import app
from flask import request

@app.route("/alerts")
def get_alerts():
    # вернуть алерт с указанным id
    if 'id' in request.args:
        alert_id = request.args.get('id')
        return f"alert with {alert_id} id"
    # если нет аргумента, вернуть данные всех алертов
    else:
        return "all alerts"
    