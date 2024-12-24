from __main__ import app

@app.route("/network_nodes")
def get_network_nodes():
    return "network_nodes"