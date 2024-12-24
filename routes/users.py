from __main__ import app
from flask import request

# получить всех пользователей
@app.route("/users")
def get_users():
    # вернуть пользователя с указанным именем
    if 'name' in request.args:
        user_name = request.args.get('name')
        return f"user with {user_name} name"
    # если нет аргумента, вернуть всех пользователей
    else:
        return "all users"
