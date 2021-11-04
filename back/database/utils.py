from .db import db


def fill_from_file(file_name: str):
    """
    Fill the database from a file.
    """
    raise NotImplementedError


def create_db():
    db.drop_all()
    db.create_all()
