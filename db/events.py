from __main__ import app

@app.route("/events")
def get_events():
    return "events"