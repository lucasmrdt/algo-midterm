from .models import PushData
from .db import db
import csv


def get_all_content_of_test():
    return Test.query.all()


def import_data_between_dates(start, end):
    getDataBetweenDates = [
        PullDataBetweenDates(dateStart=start, dateEnd=end)
        ]
    for data in getDataBetweenDates:
        db.session.add(data)
    db.session.commit()

def post_data_in_db():
    try:
        file = 'data.csv'
        data = genfromtxt(file, delimiter=',', skip_header=1, converters={0: lambda s: str(s)}).tolist()

        for i in data:
            line_history = PushData(**{
                'date' : datetime.strptime(i[0], '%d-%b-%y').date(),
                'open' : i[1],
                'high' : i[2],
                'low' : i[3],
                'closing' : i[4],
                'vol' : i[5]
            })
            db.session.add(line_history)
        db.session.commit()
        return jsonify({'message', 'data pushed in db'}), 200
