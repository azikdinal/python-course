from __main__ import app
from flask import request

@app.route("/network_nodes")
def get_network_nodes():
    # вернуть узел сети с указанным id
    if 'id' in request.args:
        network_node_id = request.args.get('id')
        return f"network node with {network_node_id} id"
    # если нет аргумента, вернуть данные всех узлов сети
    else:
        return "all network nodes"
