from __main__ import app

@app.route("/alerts_settings")
def get_alert_settings():
    return "alerts_settings"