from __main__ import app

@app.route("/metrics")
def get_metrics():
    return "metrics"

from flask import request

@app.route("/metrics")
def get_network_nodes():
    # вернуть узел сети с указанным id
    if 'id' in request.args:
        metric_id = request.args.get('id')
        return f"region with {metric_id} id"
    # если нет аргумента, вернуть данные всех узлов сети
    else:
        return "all regions"
