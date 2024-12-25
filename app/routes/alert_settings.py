from __main__ import app
from flask import request


@app.route("/alert_settings")
def get_alert_settings():
    # вернуть настройку алертов с указанным id
    if 'id' in request.args:
        alert_setting_id = request.args.get('id')
        return f"alert setting with {alert_setting_id} id"
    # если нет аргумента, вернуть данные всех настроек алертов
    else:
        return "all alert settings"
    
# все alert_settings по алерт_id TODO