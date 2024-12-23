from __main__ import app

@app.route("/users")
def get_users():
    return "users"


@app.route("/users/<int:user_id>")
def get_user(user_id):
    return f"user with {user_id} id"