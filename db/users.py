from __main__ import app

# Получить всех пользователей
@app.route("/users")
def get_users():
    return "users"

