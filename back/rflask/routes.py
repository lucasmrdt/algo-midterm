from datetime import datetime
from flask import jsonify, request
from database import insert_data_from_file, select_all_data, select_data_between_dates, create_db
from algo import get_data_by_date
from .app import app
from .constants import CSV_FILE_PATH


@app.route("/init-db", methods=["POST"])
def send_data_to_db():
    create_db()
    insert_data_from_file(CSV_FILE_PATH)
    return "DB successfully created."


@app.route("/data", methods=["GET"])
def get_data_interval():
    begin = request.args.get('begin')
    end = request.args.get('end')
    if end == 'null':
        end = begin
    try:
        begin = int(begin)
        end = int(end)
    except ValueError:
        raise Exception("Invalid params")
    data = select_data_between_dates(begin, end)
    return jsonify(data)


@app.route("/data/algo", methods=["GET"])
def get_data_interval_algo():
    begin = request.args.get('begin')
    end = request.args.get('end', begin)
    if end == 'null':
        end = begin
    try:
        begin = int(begin)
        end = int(end)
    except ValueError:
        raise Exception("Invalid params")
    if begin == end:
        begin = datetime.fromtimestamp(begin).date()
        return jsonify(get_data_by_date(begin))
    raise NotImplementedError("Not implemented yet")


@app.route("/flush", methods=["GET"])
def flush():
    data = [data.serealize() for data in select_all_data()]
    return jsonify(data)


@ app.errorhandler(Exception)
def exception_handler(error):
    return jsonify({"error": str(error)}), 400
