from __main__ import app

@app.route("/events")
def get_events():
    return "events"


@app.route("/device_types/<int:event_id>")
def event(event_id):
    return f"event with {event_id} id"