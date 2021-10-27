from .app import app
from .routes import *
from database import create_db


def main():
    create_db()
    app.run(debug=True)
