from __main__ import app
from flask import request

@app.route("/metrics")
def get_metrics():
    # вернуть метрику с указанным id
    if 'id' in request.args:
        metric_id = request.args.get('id')
        return f"metric with {metric_id} id"
    # если нет аргумента, вернуть данные метрик
    else:
        return "all metrics"
