from .db import db


class PushData(db.Model):
    __tablename__ = "allData"
    id = db.Column(db.Integer, primary_key=True)
    opening = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    closing = db.Column(db.Float)
    date = db.Column(db.Date)

class PushDataBetweenDates(db.Model):
    __tablename__ = "test"
    id = db.Column(db.Integer, primary_key=True)
    dateStart = db.Column(db.Date)
    dateEnd = db.Column(db.Date)