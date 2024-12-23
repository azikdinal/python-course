from __main__ import app

@app.route("/alert_settings")
def get_alert_settings():
    return "alert_settings"


@app.route("/alert_settings/<int:alert_setting_id>")
def get_alert_setting(alert_setting_id):
    return f"alert_setting with {alert_setting_id} id"