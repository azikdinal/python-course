from __main__ import app

@app.route("/sessions")
def get_sessions():
    return "sessions"