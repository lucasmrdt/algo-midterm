from .app import app
from .routes import *
from database import create_db
import os


def main():
    port = os.environ.get('PORT', 5000)
    create_db()
    app.run(debug=True, port=port, host='0.0.0.0')
