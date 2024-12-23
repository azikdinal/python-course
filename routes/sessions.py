from __main__ import app
from flask import request

@app.route("/sessions")
def get_sessions():
    # вернуть сессию с указанным id
    if 'id' in request.args:
        session_id = request.args.get('id')
        return f"session with {session_id} id"
    # если нет аргумента, вернуть данные всех сессий
    else:
        return "sessions"
