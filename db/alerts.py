from __main__ import app

@app.route("/alerts")
def get_alerts():
    return "alerts"