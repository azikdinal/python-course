from __main__ import app

@app.route("/device_types")
def get_device_types():
    return "device_types"

@app.route("/device_types/<int:device_type_id>")
def get_device_type(device_type_id):
    return f"device_types with {device_type_id} id"