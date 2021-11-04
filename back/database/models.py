from functools import total_ordering
from enum import unique
from sqlalchemy import inspect
from .db import db


class Serealizer(object):
    def serealize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}


@total_ordering
class RawData(db.Model, Serealizer):
    __tablename__ = "allData"
    id = db.Column(db.Integer, primary_key=True)
    opening = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    closing = db.Column(db.Float)
    date = db.Column(db.Date, unique=True)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, RawData):
            return NotImplemented
        return self.date == o.date

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, RawData):
            return NotImplemented
        return self.date < o.date
