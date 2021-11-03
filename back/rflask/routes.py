from flask import jsonify
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

@app.route("/test3", methods=["GET"])
def get_all_data_from_db():
    import_all_dates()
    return "All data fetched"

@app.route("/", methods=["GET"])
def get_data_interval():
    import_data_between_dates(20120814, 20160926)
    return "All data fetched between dates"