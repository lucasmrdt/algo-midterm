from flask import jsonify
from algo import query_test_data
from database import post_data_in_db
from .app import app


@app.route("/test", methods=["GET"])
def get_test():
    return jsonify(query_test_data())

@app.route("/test", methods=["POST"])
def send_data_to_db():
    post_data_in_db()
    return "OK"


