from flask import jsonify
from algo import query_test_data
from database import import_test_data
from .app import app


@app.route("/test", methods=["GET"])
def get_test():
    return jsonify(query_test_data())


@app.route("/test", methods=["POST"])
def import_test():
    import_test_data()
    return "OK"
