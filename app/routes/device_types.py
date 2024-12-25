from __main__ import app
from flask import request

@app.route("/device_types")
def get_device_types():
    # вернуть тип устройства с указанным id
    if 'id' in request.args:
        device_type_id = request.args.get('id')
        return f"device type with {device_type_id} id"
    # если нет аргумента, вернуть данные всех типов устройств
    else:
        return "all device types"
    