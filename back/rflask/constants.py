import os

SQLALCHEMY_DATABASE_URI = os.environ.get(
    "DATABASE_URL", "sqlite:///sqlitedb.file")
CSV_FILE_PATH = os.environ.get("CSV_FILE", "data.csv")
