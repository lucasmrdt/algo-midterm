from flask import jsonify
from algo import query_test_data
from database import post_data_in_db
from .app import app


@app.route("/test2", methods=["GET"])
def get_test():
    return jsonify(query_test_data())


@app.route("/", methods=["GET"])
def send_data_to_db():
    post_data_in_db()
    return "Ok, data pushed."
