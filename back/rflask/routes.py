from flask import jsonify, request
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


@app.route("/data", methods=["GET"])
def get_data():
    begin = request.args.get('begin')
    end = request.args.get('end')
    if end == 'null':
        end = begin
    try:
        begin = int(begin)
        end = int(end)
    except ValueError:
        raise Exception("Invalid params")
    return "Ok, data pushed."


@ app.errorhandler(AssertionError)
def exception_handler(error):
    return jsonify({"error": str(error)}), 400
