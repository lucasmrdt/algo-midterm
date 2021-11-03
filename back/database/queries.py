from .models import RawData
from .db import db
import datetime
import csv


def get_all_content_of_test():
    return Test.query.all()


def import_all_dates():
    dataList = []
    for i in RawData.query.all():
        opening = i.opening
        high = i.high
        low = i.low
        closing = i.closing
        date = i.date
        dataList.append([opening, high, low, closing, date])

    return dataList


def import_data_between_dates(start, end):
    dateTimeObjS = datetime.datetime.fromtimestamp(start)
    dateTimeObjE = datetime.datetime.fromtimestamp(end)

    dataList = []
    for i in RawData.query.filter(RawData.date.between(dateTimeObjS, dateTimeObjE)):
        opening = i.opening
        high = i.high
        low = i.low
        closing = i.closing
        date = i.date
        dataList.append([opening, high, low, closing, date])
    print(dataList)
    return dataList


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
