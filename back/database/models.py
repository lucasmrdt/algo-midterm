from enum import unique
from sqlalchemy import inspect
from .db import db


class Serealizer(object):
    def serealize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}


class RawData(db.Model, Serealizer):
    __tablename__ = "allData"
    id = db.Column(db.Integer, primary_key=True)
    opening = db.Column(db.Float)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    closing = db.Column(db.Float)
    date = db.Column(db.Date, unique=True)
