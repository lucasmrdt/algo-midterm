from .models import RawData
from .db import db
import datetime
import csv


def get_all_content_of_test():
    return Test.query.all()


def import_all_dates():
    getAllData = []

    # content = select(allData)
    # result = conn.execute(content)
    # for row in result:
    #     getAllData.append(row)

    return getAllData


def import_data_between_dates(start, end):
    # getDataBetweenDates = [
    #     PullDataBetweenDates(dateStart=start, dateEnd=end)
    # ]
    # for data in getDataBetweenDates:
    #     db.session.add(data)
    db.session.commit()


def post_data_in_db():
    file = open('data.csv', encoding='utf-8')
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)

    for i in rows[1:]:
        line_history = RawData(**{
            'date': datetime.datetime.strptime(i[0], '%b %d, %Y').date(),
            'opening': float(i[1].replace(',', '')),
            'high': float(i[2].replace(',', '')),
            'low': float(i[3].replace(',', '')),
            'closing': float(i[4].replace(',', '')),
        })
        db.session.add(line_history)
    db.session.commit()
    return "Ok"
