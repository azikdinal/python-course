from __main__ import app

@app.route("/metrics")
def get_metrics():
    return "metrics"