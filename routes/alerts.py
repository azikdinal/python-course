from __main__ import app

@app.route("/alerts")
def get_alerts():
    return "alerts"
    
@app.route("/alerts/<int:alert_id>")
def get_alert(alert_id):
    return f"user with {alert_id} id"