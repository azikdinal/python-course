from __main__ import app
from flask import request

@app.route("/events")
def get_events():
    # вернуть событие с указанным id
    if 'id' in request.args:
        event_id = request.args.get('id')
        return f"event with {event_id} id"
    # если нет аргумента, вернуть данные всех событий
    else:
        return "all events"
    

# Отбор событий в промежутке времени TODO