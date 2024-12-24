from __main__ import app

@app.route("/regions")
def get_regions():
    return "regions"