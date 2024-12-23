from __main__ import app
from flask import request

@app.route("/regions")
def get_regions():
    # вернуть регион с указанным id
    if 'id' in request.args:
        region_id = request.args.get('id')
        return f"region with {region_id} id"
    # если нет аргумента, вернуть данные всех сессий
    else:
        return "all regions"
