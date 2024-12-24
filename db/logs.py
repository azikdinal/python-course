from __main__ import app

@app.route("/logs")
def get_logs():
    return "logs"