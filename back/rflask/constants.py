import os
import re

SQLALCHEMY_DATABASE_URI = os.environ.get(
    "DATABASE_URL", "sqlite:///sqlitedb.file")
SQLALCHEMY_DATABASE_URI = re.sub(
    r"^postgres://", "postgresql://", SQLALCHEMY_DATABASE_URI)

CSV_FILE_PATH = os.environ.get("CSV_FILE", "data.csv")
