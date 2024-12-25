from __main__ import app
from flask import request

@app.route("/traffic_statictics")
def get_traffic_statictics():
    # вернуть данные статистики с указанным id
    if 'id' in request.args:
        traffic_statictic_id = request.args.get('id')
        return f"traffic statistic with {traffic_statictic_id} id"
    # если нет аргумента, вернуть все статистические данные
    else:
        return "all traffic statictics"
