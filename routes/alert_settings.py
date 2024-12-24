from __main__ import app
from flask import request


@app.route("/alerts")
def get_alert_settings():
    # вернуть настройку алертов с указанным id
    if 'id' in request.args:
        device_type_id = request.args.get('id')
        return f"event with {device_type_id} id"
    # если нет аргумента, вернуть данные всех настроек алертов
    else:
        return "all alert setting"
    
# все alert_settings по алерт_id TODO