from typing import List
import datetime
import csv
from .models import RawData
from .db import db


def select_all_data() -> List[RawData]:
    return RawData.query.all()


def select_data_between_dates(start, end) -> List[RawData]:
    dateTimeObjS = datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d')
    dateTimeObjE = datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d')
    rows = RawData.query.filter(
        RawData.date <= dateTimeObjE).filter(RawData.date >= dateTimeObjS)

    return [row.serealize() for row in rows]


def insert_data_from_file(file: str):
    file = open(file, encoding='utf-8')
    csvreader = csv.reader(file)
    rows = [row for row in csvreader]

    for date, closing, opening, high, low, *_ in rows[1:]:
        rawData = RawData(
            date=datetime.datetime.strptime(date, '%b %d, %Y').date(),
            opening=float(opening.replace(',', '')),
            high=float(high.replace(',', '')),
            low=float(low.replace(',', '')),
            closing=float(closing.replace(',', '')))
        db.session.add(rawData)
    db.session.commit()
