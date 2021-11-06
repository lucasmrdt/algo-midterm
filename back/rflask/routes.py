from datetime import datetime
import time
from flask import json, jsonify, request, g
from database import insert_data_from_file, select_all_data, select_data_between_dates, create_db, select_data_at_date
from algo import get_data_by_date, get_data_between_date
from .app import app
from .constants import CSV_FILE_PATH


@app.route("/init-db", methods=["POST"])
def send_data_to_db():
    create_db()
    insert_data_from_file(CSV_FILE_PATH)
    return "DB successfully created."


@app.route("/data/db", methods=["GET"])
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
    if begin == end:
        return jsonify(select_data_at_date(begin))
    return jsonify(select_data_between_dates(begin, end))


@app.route("/data/algo", methods=["GET"])
def get_data_interval_algo():
    begin = request.args.get('begin')
    end = request.args.get('end', begin)
    k = request.args.get('k')
    if end == 'null':
        end = begin
    try:
        begin = datetime.fromtimestamp(int(begin)).date()
        end = datetime.fromtimestamp(int(end)).date()
        k = int(k)
    except ValueError:
        raise Exception("Invalid params")
    if k < 0:
        k = float('-infinity')
    if begin == end:
        return jsonify(get_data_by_date(begin))
    return jsonify(get_data_between_date(begin, end, k))


@app.route("/flush", methods=["GET"])
def flush():
    data = [data.serealize() for data in select_all_data()]
    return jsonify(data)


@app.errorhandler(Exception)
def exception_handler(error):
    return jsonify({"error": str(error)}), 400


@app.before_request
def before_request():
    g.begin_time = time.time()


@app.after_request
def after_request(response):
    end_time = time.time()
    response.data = json.dumps(
        {'time': end_time - g.begin_time, 'data': response.get_json()})
    return response
