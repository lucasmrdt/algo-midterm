from flask import jsonify, request
from algo import query_test_data
from database import post_data_in_db
from database import import_all_dates
from database import import_data_between_dates
from .app import app


@app.route("/test2", methods=["GET"])
def get_test():
    return jsonify(query_test_data())


@app.route("/test", methods=["GET"])
def send_data_to_db():
    post_data_in_db()
    return "Ok, data pushed."


@app.route("/data", methods=["GET"])
def get_data_interval():
    begin = request.args.get('begin')
    end = request.args.get('end')
    if end == 'null':
        end = begin
    try:
        print(begin, end)
        begin = int(begin)
        end = int(end)
    except ValueError:
        raise Exception("Invalid params")
    data = import_data_between_dates(begin, end)
    return jsonify(data)


@app.route("/test3", methods=["GET"])
def get_all_data_from_db():
    import_all_dates()
    return "All data fetched"


@ app.errorhandler(Exception)
def exception_handler(error):
    return jsonify({"error": str(error)}), 400
