from .db import db


class Test(db.Model):
    __tablename__ = "test"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(50))
